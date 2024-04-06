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