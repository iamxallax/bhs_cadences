import click
from flask import current_app as app
from flask import Blueprint
from dataclasses import dataclass
import json
import os

bp = Blueprint("commands", __name__)

@dataclass
class Metadata:
    title: str
    description: str = ""
    author: str = ""
    date_added: str = ""

    


@bp.cli.command("add-metadata")
@click.argument("score")
@click.option('--title', help='score title')
@click.option('--description', help='score description')
@click.option('--author', help='score\'s author')
@click.option('--date-added', help='score added to BHS cadence list (yyyy-mm-dd)')
def add_metadata(score, title, description=None, author=None, date_added=None):
    # print(score)
    data = Metadata(title = title, description = description, author = author, date_added = date_added)
    # print(data)
    data_dict = data.__dict__
    # print(data_dict)
    path = "/Users/xallax/Documents/python/bhs_cadences/data/" + score + "/metadata.json"
    with open(path, "w") as outfile:
        json.dump(data_dict, outfile, indent=2) 

@bp.cli.command("list-scores")
def list_scores():
    print(app.config.items())
    print('listing scores')