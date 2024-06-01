
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(items):
    # Price table and offers
    price_table = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10,
        'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50,
        'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }
    special_offers = {
        'A': [(3, 130), (5, 200)],
        'B': [(2, 45)],
        'E': [(2, 'B')],
        'F': [(3, 'F')],
        'H': [(5, 45), (10, 80)],
        'K': [(2, 150)],
        'N': [(3, 'M')],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': [(3, 'Q')],
        'U': [(3, 'U')],
        'V': [(2, 90), (3, 130)]
    }

    # Check for illegal input
    if not all(item in price_table for item in items):
        return -1

    total_price = 0
    item_counts = {item: items.count(item) for item in set(items)}

    for item, count in item_counts.items():
        if item in special_offers:
            for offer in special_offers[item]:
                if isinstance(offer[0], int):
                    special_offer_quantity, special_offer_price = offer
                    special_offer_count = count // special_offer_quantity
                    remaining_count = count % special_offer_quantity
                    total_price += special_offer_count * special_offer_price
                    count = remaining_count
                else:
                    free_item = offer[1]
                    free_item_count = items.count(free_item)
                    if free_item_count >= count:
                        total_price += count * price_table[item]
                    else:
                        total_price += (count - (count //
                                        (offer[0] + 1))) * price_table[item]
        else:
            total_price += count * price_table[item]

    return total_price

print(checkout('UUUU')) # 120
print(checkout('UUUUU'))  # 160
print(checkout('UUUUUUUU')) # 240
print(checkout('EE')) # 80
print(checkout('EEB')) # 80
print(checkout('EEEB')) # 120

