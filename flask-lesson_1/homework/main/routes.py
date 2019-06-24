from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)


@main.route("/")
def go_main():
    return render_template("main.html")


@main.route("/redirect_to_Pornhub.com")
def redirect_to_pornhub():
    return redirect(url_for("main.go_main"))
