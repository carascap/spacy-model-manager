import sys

import click

from spacy_model_manager.lib import SPACY_MODEL_NAMES

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

PATH_METAVAR = "<path>"
INT_METAVAR = "<n>"
VERSION_METAVAR = "<version>"
MODEL_METAVAR = "<model>"


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def spacy_model():
    """
    Command line utility to view, install, and upgrade spaCy models
    """


@spacy_model.command("list", context_settings=CONTEXT_SETTINGS)
def _list():
    """
    List installed and available spaCy models and their versions.
    """

    sys.exit()


@spacy_model.command(context_settings=CONTEXT_SETTINGS)
@click.argument('model', metavar=MODEL_METAVAR, type=click.Choice(SPACY_MODEL_NAMES),)
def install(model):
    """
    Install <model>
    """

    sys.exit()


@spacy_model.command(context_settings=CONTEXT_SETTINGS)
def upgrade():
    """
    List installed and available spaCy models and their versions.
    """

    sys.exit()
