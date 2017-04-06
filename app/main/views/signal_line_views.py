from flask import render_template, request
from .. import main
from ...model import SignalLine


@main.route('/signal-line/<int:id>')
def signal_line(id):
    signal_line = SignalLine.query.get_or_404(id)
    return render_template("signal-line.html", signal_line=signal_line)


@main.route('/signal-lines/')
def signal_lines():
    items = SignalLine.query.all()
    return render_template("list_page.html", singular="signal_line", plural="signal_lines", items=items)
