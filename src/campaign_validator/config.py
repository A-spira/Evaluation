import os
from pathlib import Path

from dotenv import load_dotenv

EXPECTED_TOKEN_LENGTH = 26


def load_access_token(env_file: str | Path = ".env") -> str:
    """Load and return the campaign API token without displaying it."""
    load_dotenv(env_file)
    token = os.getenv("CAMPAIGN_ACCESS_TOKEN")
    if token is None or not token.strip():
        raise ValueError("CAMPAIGN_ACCESS_TOKEN is required")

    normalized_token = token.strip()
    if len(normalized_token) != EXPECTED_TOKEN_LENGTH:
        raise ValueError("CAMPAIGN_ACCESS_TOKEN is invalid")
    return normalized_token
