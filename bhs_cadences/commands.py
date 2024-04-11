import json
import os
from dataclasses import dataclass
from pathlib import Path

import click
from flask import current_app as app
from flask import Blueprint

bp = Blueprint("commands", __name__)
INSTRUMENTS = ["snare", "tenors", "cymbals", "bass"]

@dataclass
class Metadata:
    title: str
    description: str = ""
    author: str = ""
    date_added: str = ""

    
@bp.cli.command("create-score")
@click.argument("score")
@click.option('--title', help='score title')
@click.option('--description', help='score description')
@click.option('--author', help='score\'s author')
@click.option('--date-added', help='score added to BHS cadence list (yyyy-mm-dd)')
def create_score(score, title, description=None, author=None, date_added=None):
    """Add metadata to score. DATA_DIR must define the absolute path to the data directory"""
    data_dir = Path(app.config['DATA_DIR']) / Path(score)
    data_dir.mkdir(parents=True, exist_ok=True)
    for instrument in INSTRUMENTS:
        (data_dir / Path(instrument)).mkdir(parents=True, exist_ok=True)
    assert data_dir.is_dir(), f'{data_dir} is not a valid directory'

    data = Metadata(title = title, description = description, author = author, date_added = date_added)
    data_dict = data.__dict__
    
    path = data_dir / Path("metadata.json")
    with open(path, "w") as outfile:
        json.dump(data_dict, outfile, indent=2) 

@bp.cli.command("list-scores")
def list_scores():
    print(app.config.items())
    print('listing scores')