
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    # Define prices and special offers
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)]
    }

    # Validate input
    if not all(c in prices for c in skus):
        return -1

    # Count items
    item_counts = Counter(skus)
    total_amount = 0

    # Handle the special case for E which gives a free B
    if 'E' in item_counts:
        e_count = item_counts['E']
        free_b_count = e_count // 2
        item_counts['B'] = max(0, item_counts.get('B', 0) - free_b_count)

    # Calculate total price considering multi-priced offers
    for item, count in item_counts.items():
        if item in offers:
            for offer_count, offer_price in sorted(offers[item], key=lambda x: -x[0]):
                total_amount += (count // offer_count) * offer_price
                count %= offer_count
        total_amount += count * prices[item]

    return total_amount

print(checkout('A'))

