
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Define prices and special offers
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60,
        'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20,
        'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
    }
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }
    free_offers = {
        'E': ('B', 2),   # 2E get one B free
        'F': ('F', 2),   # 2F get one F free
        'N': ('M', 3),   # 3N get one M free
        'R': ('Q', 3),   # 3R get one Q free
        'U': ('U', 3)    # 3U get one U free
    }

    # Validate input
    if not all(c in prices for c in skus):
        return -1

    # Count items
    item_counts = Counter(skus)
    total_amount = 0

    # Handle free item offers
    for item, (free_item, required_count) in free_offers.items():
        if item in item_counts:
            item_count = item_counts[item]
            free_item_count = item_count // required_count
            if free_item in item_counts:
                item_counts[free_item] = max(
                    0, item_counts[free_item] - free_item_count)
            else:
                item_counts[free_item] = -free_item_count

    # Calculate total price considering multi-priced offers
    for item, count in item_counts.items():
        if item in offers:
            for offer_count, offer_price in sorted(offers[item], key=lambda x: -x[0]):
                total_amount += (count // offer_count) * offer_price
                count %= offer_count
        total_amount += count * prices[item]

    return total_amount



