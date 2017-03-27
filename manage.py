#!/usr/bin/env python
import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db
from flask_script import Command, Manager, Option, Shell
from flask_migrate import Migrate, MigrateCommand
from cpu_importer import CpuImporter


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


class ImportFileCommand(Command):
    """Import CPU description files into the database"""

    option_list = (
        Option('--filename', '-f', dest='filename'),
    )

    def run(self, filename):
        with CpuImporter() as importer:
            importer.import_addressing_modes("cpu/addressing_modes.yaml")
            importer.import_instructions("cpu/instructions")


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('import', ImportFileCommand)


if __name__ == '__main__':
    manager.run()
