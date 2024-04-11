from dataclasses import dataclass
from pathlib import Path

INSTRUMENTS = ["snare", "tenors", "cymbals", "bass"]

@dataclass
class Metadata:
    title: str
    description: str = ""
    author: str = ""
    date_added: str = ""

@dataclass
class Instrument:
    name: str
    audio: str #representing path
    pdf: str
    muse_file: str
    
@dataclass
class Score:
    metadata: Metadata
    instruments: dict