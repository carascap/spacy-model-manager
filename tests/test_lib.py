# pylint: disable=missing-function-docstring

from unittest.mock import MagicMock, patch

import pytest
import requests

from spacy_model_manager.lib import (
    SPACY_MODEL_NAMES,
    SPACY_MODELS,
    get_spacy_models,
    install_spacy_model,
    uninstall_spacy_model,
)


def test_get_spacy_models():
    assert sorted(get_spacy_models().keys()) == SPACY_MODEL_NAMES


def test_get_spacy_models_with_request_error():
    with patch("requests.get") as mock_get:
        mock_get.return_value.ok = False
        mock_get.return_value.raise_for_status = MagicMock(
            side_effect=requests.HTTPError
        )

        assert get_spacy_models() == {name: [] for name in SPACY_MODEL_NAMES}


@pytest.mark.parametrize(
    "patched,mock_object",
    [
        ("spacy.cli.download", MagicMock(side_effect=SystemExit)),
        ("spacy_model_manager.lib.reload", MagicMock(side_effect=ImportError)),
    ],
)
def test_install_spacy_model_with_download_error(zh_core_web_sm, patched, mock_object):
    with patch(patched, new=mock_object):
        assert install_spacy_model(zh_core_web_sm) == -1
        assert uninstall_spacy_model(zh_core_web_sm) == 0


def test_remove_spacy_model_with_uninstall_error():
    with patch("subprocess.run", new=MagicMock(side_effect=SystemExit)):
        assert uninstall_spacy_model(SPACY_MODELS.en_core_web_sm) == -1
