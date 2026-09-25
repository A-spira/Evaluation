import sys

from campaign_validator.config import load_access_token
from campaign_validator.metrics import (
    click_through_rate,
    count_campaign_tags,
    normalize_campaign_name,
)


def main() -> int:
    try:
        load_access_token()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    campaign_name = "  Autumn launch  "
    clicks = 125
    impressions = 2_500

    print(f"Campaign: {normalize_campaign_name(campaign_name)}")
    print(f"Click-through rate: {click_through_rate(clicks, impressions):.2f}%")
    print(f"Tag count: {count_campaign_tags(['priority', 'launch'])}")
    print("Access token configured: yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
