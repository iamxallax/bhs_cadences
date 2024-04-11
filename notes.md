# Setup and Development

## create project with cookiecutter

This guide assumes cookiecutter is installed. https://github.com/cookiecutter/cookiecutter

Create a new project from a minimal Flask template:
``` 
% cookiecutter https://github.com/candidtim/cookiecutter-flask-minimal.git
  [1/7] application_name (Your Application): Ballard Cadences
  [2/7] package_name (yourapplication): bhs_cadences
  [3/7] use_poetry (n): n
  [4/7] use_flake8 (n): y
  [5/7] use_black (n): n
  [6/7] use_isort (n): y
  [7/7] use_mypy (n): n
```

Create a new git repo:
```
cd bhs_cadences
git init .
git add *
git commit -m "first commit after creating project from cookiecutter-flask-minimal"
```

Push to github:
```
git remote add origin git@github.com:xallax-ekacnap/bhs_cadences.git
git branch -M main
git push -u origin main
```

Note that the default port in the cookiecutter template is 5000 which is used by another application on MacOS, so we change the Makefile to use port 8000

```
run: venv
	venv/bin/flask --app bhs_cadences --debug run --port 8000 
```

## custom commands

See https://flask.palletsprojects.com/en/3.0.x/cli/#custom-commands

To list custom commands, run 

```
venv/bin/flask --app bhs_cadences --help
```

## design ideas

### data storage

- environment variable defining location of the data directory, eg `DATA_DIR=data`
- in dev, this is relative to the project dir (eg, `bhs_cadences/data`) but is NOT saved to the repo
- on fly.io, this is a path to the storage volume
- app adds value of `DATA_DIR` to app.config
- create dir if not exists

data hierarchy:

- each cadence is represented by a subdirecory of data/, "topsy"

```
data/
  topsy/
  - metadata.json - title, description
  - everything/
    - audio.mp3
    - score.pdf
    - topsy.mscz
  - snare/
    - audio.mp3
    - score.pdf
    - topsy.mscz
  - tenor/
    - audio.mp3
    - score.pdf
    - topsy.mscz  
  - bass/
    - audio.mp3
    - score.pdf
    - topsy.mscz  
  - cymbals/
    - audio.mp3
    - score.pdf
    - topsy.mscz  

  
```

Functions needed:

- List all scores (listAllScores())
- Get score (getScore())
- Write score (writeScore())

Organization:

Dict:
- topsy (Score object)
  - snare (Instrument object)
  