# pylint: disable=missing-function-docstring

from unittest.mock import MagicMock, patch

import requests

from spacy_model_manager.lib import (
    SPACY_MODEL_NAMES,
    SPACY_MODELS,
    get_spacy_models,
    install_spacy_model,
    uninstall_spacy_model,
)


def test_get_spacy_models_with_request_error():
    with patch("requests.get") as mock_get:
        mock_get.return_value.ok = False
        mock_get.return_value.raise_for_status = MagicMock(
            side_effect=requests.HTTPError
        )

        assert get_spacy_models() == {name: [] for name in SPACY_MODEL_NAMES}


def test_install_spacy_model_with_download_error():
    with patch("spacy.cli.download", new=MagicMock(side_effect=SystemExit)):
        # Pick a model not yet installed so spaCy tries to download it
        assert install_spacy_model(SPACY_MODELS.zh_core_web_sm) == -1


def test_remove_spacy_model_with_uninstall_error():
    with patch("subprocess.run", new=MagicMock(side_effect=SystemExit)):
        assert uninstall_spacy_model(SPACY_MODELS.en_core_web_sm) == -1
