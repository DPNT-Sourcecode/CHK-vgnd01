# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    price_table = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': [(2, {'B': 1})],  # 2E for the price of 1B
        'F': [(3, 20)],  # 3F for the price of 2F which is 3F for 20 simplified
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'N': [(3, {'M': 1})],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': [(3, {'Q': 1})],
        'U': [(4, 120)],  # 4U for the price of 3U which is 4U for 120
        'V': [(3, 130), (2, 90)]
    }

    # Validate input
    if not validate_input(skus, price_table):
        return -1

    # Count occurrences of each SKU
    item_counts = count_items(skus)

    # Calculate total price
    total_price = calculate_total_price(
        item_counts, price_table, special_offers)

    return total_price


def validate_input(skus, price_table):
    """Checks if sku is a string and is a valid price."""
    if not isinstance(skus, str):
        return False
    for sku in skus:
        if sku not in price_table:
            return False
    return True


def count_items(skus):
    """Keep a counter of the products in the basket
    else initialise it."""
    item_counts = {}
    for sku in skus:
        item_counts[sku] = item_counts.get(sku, 0) + 1
    return item_counts


def calculate_total_price(item_counts, price_table, special_offers):
    """Calculate the total price of items in the basket
    considering special offers."""
    total_price = 0
    for item, count in item_counts.items():
        if item in special_offers:
            total_price += apply_special_offers_to_items(
                item, count, special_offers[item], price_table, item_counts)
        else:
            total_price += count * price_table[item]
    return total_price


def apply_special_offers_to_items(item, count, offers, price_table, item_counts):
    """Apply special offers for an item and return the total price."""
    total_price = 0
    # Sort offers by the quantity in descending order to prioritize larger offers first
    # e.g: check 5A for 200 before 3A for 130
    offers = sorted(offers, key=lambda x: x[0], reverse=True)
    for offer in offers:
        special_count, special_offer = offer
        if isinstance(special_offer, int):
            while count >= special_count:
                total_price += special_offer
                count -= special_count
        elif isinstance(special_offer, dict):
            while is_offer_applicable(item_counts, special_offer):
                total_price += apply_special_offer(
                    item, special_count, special_offer,
                    price_table, item_counts)
                count = item_counts[item]
            break  # Break after applying the first applicable offer

    total_price += count * price_table[item]
    return total_price


def is_offer_applicable(item_counts, special_offer):
    """Check if the required items for a special offer are available in the basket
    i.e. if the counts of basket is more or equal to the special offers counts."""
    for other_item, offer_count in special_offer.items():
        if other_item not in item_counts or item_counts[other_item] < offer_count:
            return False
    return True


def apply_special_offer(item, special_count, special_offer, price_table, item_counts):
    """Apply a special offer and update the counts and total price."""
    total_price = 0
    for other_item, offer_count in special_offer.items():
        item_counts[other_item] -= offer_count
    total_price += special_count * price_table[item]
    item_counts[item] -= special_count
    return total_price


print('CHECKOUT 1')
print(checkout('A'))  # 50
print(checkout('B'))  # 30
print(checkout('C'))  # 20
print(checkout('D'))  # 15
print(checkout('AA'))  # 100
print(checkout('BB'))  # 45

print('CHECKOUT 2')
print(checkout('AAA'))  # 130
print(checkout('AAAA'))  # 180
print(checkout('AAAAA'))  # 200
print(checkout('BB'))  # 45
print(checkout('EEB'))  # 80
print(checkout('EEEB'))  # 120
print(checkout('EEBEEB'))  # 160

print('CHECKOUT 3')
print(checkout('F'))  # 10
print(checkout('FF'))  # 20
print(checkout('FFF'))  # 20
print(checkout('FFFF'))  # 30
print(checkout('FFFFF'))  # 40
print(checkout('FFFFFF'))  # 40

print('CHECKOUT 4')
print(checkout('HHHHH'))  # 45
print(checkout('HHHHHHHHHH'))  # 80
print(checkout('KK'))  # 150
print(checkout('RRRQ'))  # 150

print(checkout('BEBEEE'))  # 160
print(checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # 1880
print(checkout('LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH'))  # 1880
