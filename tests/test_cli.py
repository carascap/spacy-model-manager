# pylint: disable=too-few-public-methods,missing-function-docstring

from contextlib import contextmanager
from pathlib import Path
from typing import List, Optional, Union

import click
import pytest
from click.testing import CliRunner, Result

import spacy_model_manager
from spacy_model_manager.cli import spacy_model, validate_version_string
from spacy_model_manager.lib import SPACY_MODELS

TEST_MODEL = SPACY_MODELS.en_core_web_sm


@contextmanager
def does_not_raise():
    yield


class Expected:
    """
    Result object type for parametrized tests. Expand as necessary...
    """

    def __init__(self, status: int, tokens: List[str], **kwargs):
        self.status = status
        self.tokens = tokens

        for key, value in kwargs.items():
            setattr(self, key, value)


def run_spacy_model_command(
    cmd: Optional[str],
    options: Optional[List[str]],
    args: Union[Path, str, None],
    runner: CliRunner,
    expected: Optional[Expected],
) -> Result:
    """
    Block of code to run a spacy-model command as part of a test
    """

    command = [cmd] if cmd else []
    command.extend(options or [])

    if args:
        command.append(str(args))

    result = runner.invoke(spacy_model, command)

    if expected:
        assert result.exit_code == expected.status

        for token in expected.tokens:
            assert token in result.output

    return result


@pytest.mark.parametrize(
    "cmd, options, expected",
    [
        (None, None, Expected(status=0, tokens=["Usage", "Options", "Commands"])),
        (None, ["-h"], Expected(status=0, tokens=["Usage", "Options", "Commands"])),
        (None, ["--help"], Expected(status=0, tokens=["Usage", "Options", "Commands"])),
        (
            None,
            ["--version"],
            Expected(status=0, tokens=[spacy_model_manager.__version__]),
        ),
        (
            "install",
            None,
            Expected(status=2, tokens=["Error: Missing argument '<model>'"]),
        ),
        (
            "upgrade",
            None,
            Expected(status=2, tokens=["Error: Missing argument '<model>'"]),
        ),
        (
            "remove",
            None,
            Expected(status=2, tokens=["Error: Missing argument '<model>'"]),
        ),
        (
            "list",
            None,
            Expected(
                status=0,
                tokens=["spaCy model", "installed version", "available versions"],
            ),
        ),
        ("install", [TEST_MODEL], Expected(status=0, tokens=["Installed", TEST_MODEL])),
        ("upgrade", [TEST_MODEL], Expected(status=0, tokens=["Installed", TEST_MODEL])),
        ("remove", [TEST_MODEL], Expected(status=0, tokens=[])),
    ],
)
def test_spacy_model(cli_runner, cmd, options, expected):
    run_spacy_model_command(cmd, options, None, cli_runner, expected)


@pytest.mark.parametrize(
    "value,context",
    [
        ("1.2.3", does_not_raise()),
        ("2.0", does_not_raise()),
        ("0.0a1", does_not_raise()),
        (None, does_not_raise()),
        ("foobar", pytest.raises(click.BadParameter)),
        ("1", pytest.raises(click.BadParameter)),
        (".5", pytest.raises(click.BadParameter)),
    ],
)
def test_validate_version_string(value, context):
    with context:
        assert validate_version_string(None, None, value) == value
