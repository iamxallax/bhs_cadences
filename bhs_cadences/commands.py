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

@dataclass
class Instrument:
    instrument: str
    audio: str #representing path
    pdf: str
    muse_file: str
    
@dataclass
class Score:
    metadata: Metadata
    instruments: list[Instrument]

def get_scores(data_dir: Path):
    scores = []
    for folder in data_dir.iterdir():
        metadata = folder / Path("metadata.json")
        if not metadata.is_file():
            continue

        with open(metadata, "r") as f:
            data = json.load(f)
            score = Score(metadata=Metadata(**data), instruments=[])

        for instrument in INSTRUMENTS:
            audio = folder / Path(instrument) / Path("audio.mp3")
            pdf = folder / Path(instrument) / Path("score.pdf")
            muse_file = folder / Path(instrument) / Path("muse_file.mscz")
            score.instruments.append(
                Instrument(
                    instrument=instrument, 
                    audio=audio if audio.is_file() else None, 
                    pdf=pdf if pdf.is_file() else None, 
                    muse_file=muse_file if muse_file.is_file() else None)
                    )

        scores.append(score)

    return scores
    
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
    for score in scores:
        print(score.metadata.title)
        for instrument in score.instruments:
            print(' ', instrument.instrument)
            for file in [instrument.audio, instrument.pdf, instrument.muse_file]:
                if file is not None:
                    print('  ', file)