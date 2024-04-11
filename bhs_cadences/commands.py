import json
import os
from dataclasses import dataclass
from pathlib import Path
import pprint

import click
from flask import current_app as app
from flask import Blueprint

from bhs_cadences.models import Score, Instrument, Metadata, INSTRUMENTS
from bhs_cadences.utils import get_scores

bp = Blueprint("commands", __name__)
    
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
    scores = get_scores(Path(app.config['DATA_DIR']))
    pprint.pprint(scores)
    return

    for score in scores:
        print(score.metadata.title)
        for name, instrument in score.instruments.items():
            print(' ', instrument.instrument)
            for file in [instrument.audio, instrument.pdf, instrument.muse_file]:
                if file is not None:
                    print('  ', file)