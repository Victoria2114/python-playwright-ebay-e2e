import re

# utils/helpers.py
def clean_price(text: str) -> float:
    return float(re.sub(r"[^0-9.]", "", text))
