from flask import render_template, request
from .. import main
from ...model import AddressingMode


@main.route('/addressing_modes/<int:id>', methods=['GET'])
def addressing_mode(id):
    addressing_mode = AddressingMode.query.get_or_404(id)
    return render_template("addressing_mode.html", addressing_mode=addressing_mode)


@main.route('/addressing_modes/', methods=['GET'])
def addressing_modes():
    page = request.args.get("page", 1, type=int)
    pagination = AddressingMode.query.paginate(page, per_page=25)
    return render_template("list_page.html", singular="addressing_mode", plural="addressing_modes", items=pagination.items, pagination=pagination)
