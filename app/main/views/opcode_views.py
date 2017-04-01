from flask import render_template, request
from .. import main
from ...model import OpCode


@main.route('/opcodes/<int:id>')
def opcode(id):
    opcode = OpCode.query.get_or_404(id)
    return render_template("opcode.html", opcode=opcode)


@main.route('/opcodes/')
def opcodes():
    items = OpCode.query.all()
    return render_template("list_page.html", singular="opcode", plural="opcodes", items=items)
