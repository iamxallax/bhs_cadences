import pprint
from pathlib import Path

from flask import Blueprint, Response, g, request
from flask import current_app as app
from flask import render_template

from bhs_cadences.utils import get_scores

bp = Blueprint("root", __name__)

@bp.before_request
def before_request():
    g.scores = get_scores(Path(app.config['DATA_DIR']))

@bp.route("/list")
def list():
    return render_template(
        "list.html", 
        scores=g.scores)

@bp.route("/", methods=("GET", "POST")) #base page, search
def index():
    if request.method == "POST":
        query = request.form["search"]

        matches = []
        for name, score in g.scores.items():
            title = score.metadata.title
            if query.lower() in title.lower():
                matches.append((name, score))
    else:
        matches = []


    return render_template(
        "index.html", 
        scores=g.scores,
        matches=matches)

@bp.route("/mp3/<score>/<instrument>")
def mp3(score, instrument):
    # list scores and find the path to the 
    # audio file for this score and instrument
    filepath = g.scores[score].instruments[instrument].audio

    # def generate():
    #     with open(filepath, "rb") as fwav:
    #         data = fwav.read(1024)
    #         while data:
    #             yield data
    #             data = fwav.read(1024)

    # return Response(generate(), mimetype="audio/mpeg")

    with open(filepath, "rb") as fwav:
        return Response(fwav.read(), mimetype="audio/mpeg")

@bp.route("/pdf/<score>/<instrument>")
def pdf(score, instrument):
    # list scores and find the path to the 
    # audio file for this score and instrument
    filepath = g.scores[score].instruments[instrument].pdf
    with open(filepath, "rb") as fpdf:
        return Response(fpdf.read(), mimetype="application/pdf")

@bp.route("/mscz/<score>/<instrument>")
def mscz(score, instrument):
    # list scores and find the path to the 
    # audio file for this score and instrument
    filepath = g.scores[score].instruments[instrument].muse_file
    with open(filepath, "rb") as fmuse:
        return Response(fmuse.read(), mimetype="application/x-musescore")

@bp.route("/view/<score>")
def view(score):
    # list scores and find the path to the 
    # audio file for this score and instrument
    score_obj = g.scores[score]
    return render_template(
        "view.html", 
        score=score_obj,
        score_name=score)
    

# @bp.route("/foo/<myvariable>")
# def foo(myvariable):

#     return render_template(
#         "foo.html",
#         title="Foo!",
#         myvariable=myvariable,
#         config=pprint.pformat(sorted(list(app.config.items()))))