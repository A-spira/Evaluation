from pathlib import Path

import pytest

from campaign_validator.config import load_access_token


# Checks that a valid token can be read from the local environment.
def test_load_access_token_reads_the_environment(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("CAMPAIGN_ACCESS_TOKEN", "x" * 26)

    assert load_access_token(tmp_path / "missing.env") == "x" * 26


# Checks that a helpful error is raised when the token is missing.
def test_load_access_token_rejects_a_missing_value(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.delenv("CAMPAIGN_ACCESS_TOKEN", raising=False)

    with pytest.raises(ValueError, match="CAMPAIGN_ACCESS_TOKEN is required"):
        load_access_token(tmp_path / "missing.env")


# Checks that a token with the wrong length is rejected.
def test_load_access_token_rejects_an_invalid_value(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("CAMPAIGN_ACCESS_TOKEN", "invalid-token")

    with pytest.raises(ValueError, match="CAMPAIGN_ACCESS_TOKEN is invalid"):
        load_access_token(tmp_path / "missing.env")
