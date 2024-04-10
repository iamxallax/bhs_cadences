import pprint

from flask import Blueprint
from flask import current_app as app
from flask import render_template

bp = Blueprint("root", __name__)


@bp.route("/")
def index():
    app.logger.warning("loading index.html")
    return render_template("index.html")

@bp.route("/foo/<myvariable>")
def foo(myvariable):

    return render_template(
        "foo.html",
        title="Foo!",
        myvariable=myvariable,
        config=pprint.pformat(sorted(list(app.config.items()))))