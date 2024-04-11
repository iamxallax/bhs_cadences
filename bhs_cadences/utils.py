from pathlib import Path
import json

from bhs_cadences.models import Score, Instrument, Metadata, INSTRUMENTS


def get_scores(data_dir: Path):
    scores = {}
    for folder in data_dir.iterdir():
        metadata = folder / Path("metadata.json")
        if not metadata.is_file():
            continue

        with open(metadata, "r") as f:
            data = json.load(f)
            score = Score(metadata=Metadata(**data), instruments={})

        for instrument in INSTRUMENTS:
            audio = folder / Path(instrument) / Path("audio.mp3")
            pdf = folder / Path(instrument) / Path("score.pdf")
            muse_file = folder / Path(instrument) / Path("muse_file.mscz")
            score.instruments[instrument] = Instrument(
                instrument=instrument, 
                audio=audio if audio.is_file() else None, 
                pdf=pdf if pdf.is_file() else None, 
                muse_file=muse_file if muse_file.is_file() else None)
                    
        scores[folder.name] = score

    return scores