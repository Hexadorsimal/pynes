from flask import render_template, request
from .. import main
from ...model import Register


@main.route('/registers/<int:id>')
def register(id):
    register = Register.query.get_or_404(id)
    return render_template("register.html", register=register)


@main.route('/registers/')
def registers():
    items = Register.query.all()
    return render_template("list_page.html", singular="register", plural="registers", items=items)
