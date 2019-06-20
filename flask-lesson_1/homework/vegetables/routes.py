from flask import Blueprint, render_template, request

vegetables = Blueprint('vegetables', __name__)

vegetables_list = ['Potato', 'Tomato', 'Cabbage']


@vegetables.route("/vegetables/<string:value>", methods=['POST'])
def vegetables_post(value=None):
    vegetables_list.append(value)
    return "Your vegetable has been planted"


@vegetables.route("/vegetables/<string:value>", methods=['DELETE'])
def vegetables_delete(value=None):
    if request.method == "DELETE":
        for vegetable in vegetables_list:
            if vegetable == value:
                vegetables_list.remove(vegetable)
    return "Your fruit has been diffused"


@vegetables.route("/vegetables", methods=['GET'])
def vegetables_get():
    return render_template("vegetables.html", values=vegetables_list)
