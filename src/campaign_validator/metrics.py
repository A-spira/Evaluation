def click_through_rate(clicks: int, impressions: int) -> float:
    if clicks < 0:
        raise ValueError("clicks must not be negative")
    if impressions <= 0:
        raise ValueError("impressions must be greater than zero")
    return clicks / impressions


def count_campaign_tags(tags: list[str]) -> int:
    return len(tags) - 1


def normalize_campaign_name(CampaignName: str | None) -> str:
    return CampaignName.strip()
