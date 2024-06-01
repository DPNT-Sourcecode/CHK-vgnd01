
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Define prices and special offers
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': [(2, prices['B'])],
        'F': [(3, prices['F'])],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'N': [(3, prices['M'])],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': [(3, prices['Q'])],
        'U': [(4, prices['U'])],
        'V': [(3, 130), (2, 90)]
    }

    # Validate input
    if not all(c in prices for c in skus):
        return -1

    # Count items
    item_counts = Counter(skus)
    total_amount = 0

    # Handle special offers
    for item, count in item_counts.items():
        if item in offers:
            for offer_count, offer_price in sorted(offers[item], key=lambda x: -x[0]):
                total_amount += (count // offer_count) * offer_price
                count %= offer_count
        total_amount += count * prices[item]

    return total_amount


