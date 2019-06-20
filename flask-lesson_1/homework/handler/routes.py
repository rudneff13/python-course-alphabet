from flask import Blueprint, render_template

handler = Blueprint('handler', __name__)


@handler.app_errorhandler(404)
def error_404_handler(error):
    return render_template("error_404.html"), 404
