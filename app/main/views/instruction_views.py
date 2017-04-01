from flask import redirect, render_template, request, url_for
from .. import main
from ...model import Instruction


@main.route('/instructions/<int:id>', methods=['GET'])
def instruction(id):
    instruction = Instruction.query.get_or_404(id)
    return render_template("instruction.html", instruction=instruction)


@main.route('/instructions/', methods=['GET'])
def instructions():
    items = Instruction.query.all()
    return render_template("list_page.html", singular="instruction", plural="instructions", items=items)
