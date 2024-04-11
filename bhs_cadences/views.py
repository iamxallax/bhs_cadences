import pprint
from pathlib import Path

from flask import Blueprint, Response
from flask import current_app as app
from flask import render_template

from bhs_cadences.utils import get_scores

bp = Blueprint("root", __name__)


@bp.route("/")
def index():
    app.logger.warning("loading index.html")
    scores = get_scores(Path(app.config['DATA_DIR']))
    print(scores)
    return render_template(
        "index.html", 
        scores=scores)

@bp.route("/mp3/<score>/<instrument>")
def mp3(score, instrument):
    # list scores and find the path to the 
    # audio file for this score and instrument
    scores = get_scores(Path(app.config['DATA_DIR']))
    filepath = scores[score].instruments[instrument].audio

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
    scores = get_scores(Path(app.config['DATA_DIR']))
    filepath = scores[score].instruments[instrument].pdf
    with open(filepath, "rb") as fpdf:
        return Response(fpdf.read(), mimetype="application/pdf")

@bp.route("/mscz/<score>/<instrument>")
def mscz(score, instrument):
    # list scores and find the path to the 
    # audio file for this score and instrument
    scores = get_scores(Path(app.config['DATA_DIR']))
    filepath = scores[score].instruments[instrument].muse_file
    with open(filepath, "rb") as fmuse:
        return Response(fmuse.read(), mimetype="application/x-musescore")

# @bp.route("/foo/<myvariable>")
# def foo(myvariable):

#     return render_template(
#         "foo.html",
#         title="Foo!",
#         myvariable=myvariable,
#         config=pprint.pformat(sorted(list(app.config.items()))))