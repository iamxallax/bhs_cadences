import click
from flask import current_app as app
from flask import Blueprint

bp = Blueprint("commands", __name__)

@bp.cli.command("add-metadata")
@click.argument("score")
def add_metadata(score):
    print(score)

@bp.cli.command("list-scores")
def list_scores():
    print(app.config.items())
    print('listing scores')