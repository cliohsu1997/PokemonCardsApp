"""Shared scraping constants (sealed-product filter)."""

SEALED_KEYWORDS = [
    "booster pack",
    "booster box",
    "elite trainer box",
    "etb",
    "display box",
    "factory sealed",
    "blister",
    "theme deck",
    "starter deck",
    "pokemon tin",
    "promo set",
    "bundle",
    "collection",
]

# Regex alternation for pandas str.contains(..., case=False)
SEALED_NAME_PATTERN = "|".join(SEALED_KEYWORDS)
