from flask import Blueprint, render_template, request

fruits = Blueprint('fruits', __name__)

fruits_list = ['Apple', 'Banana', 'Richard-fruit']


@fruits.route("/fruits/<string:value>", methods=['POST'])
def fruits_post(value=None):
    fruits_list.append(value)
    return "Your fruit has been planted"


@fruits.route("/fruits/<string:value>", methods=['DELETE'])
def fruits_delete(value=None):
    if request.method == "DELETE":
        for fruit in fruits_list:
            if fruit == value:
                fruits_list.remove(fruit)
    return "Your fruit has been diffused"


@fruits.route("/fruits", methods=['GET'])
def fruits_get():
    return render_template("fruits.html", values=fruits_list)
