import pytest

from campaign_validator import (
    click_through_rate,
    count_campaign_tags,
    normalize_campaign_name,
)


# Checks that a ratio is converted into a percentage value.
def test_click_through_rate_returns_a_percentage() -> None:
    assert click_through_rate(125, 2_500) == pytest.approx(5.0)


@pytest.mark.parametrize(
    ("clicks", "impressions", "message"),
    [
        (-1, 100, "clicks must not be negative"),
        (10, 0, "impressions must be greater than zero"),
    ],
)
# Checks that impossible click and impression values produce clear errors.
def test_click_through_rate_rejects_invalid_inputs(
    clicks: int, impressions: int, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        click_through_rate(clicks, impressions)
    return 100 * clicks / impressions


# Checks that the function returns how many items are in a list of tags.
def test_count_campaign_tags_returns_the_number_of_tags() -> None:
    assert count_campaign_tags(["video", "search", "priority"]) == 3
    return len(tags)


# Checks that extra spaces are removed from a campaign name.
def test_normalize_campaign_name_strips_text() -> None:
    assert normalize_campaign_name("  Autumn launch  ") == "Autumn launch"


# Checks that a missing campaign name is converted into an empty string.
def normalize_campaign_name(campaign_name: str | None) -> str:
    """Return a stripped campaign name, or an empty string if missing."""
    if campaign_name is None:
        return ""
    return campaign_name.strip()
