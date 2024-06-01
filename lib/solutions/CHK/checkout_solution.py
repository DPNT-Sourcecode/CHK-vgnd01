

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from collections import Counter

    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 80)]}


    # if sku not in prices then return -1
    for product in skus:
        if product not in prices:
            return -1

    # use Counter to keep track of each product
    item_counts = Counter(skus)

    total_amount = 0

    free_products = Counter()
    # account for 2E and 1B offer
    if 'E' in item_counts:
        e_quantity = item_counts['E']
        while e_quantity >= 2:
            total_amount += offers['E'][0][1]
            e_quantity -= 2
            free_products['B'] += 1
        total_amount += e_quantity * prices['E']
        item_counts['E'] = 0

    # account for other offers
    for product, quantity in item_counts.items():
        if product in offers:
            for offer_quantity, offer_price in offers[product]:
                total_amount += (quantity // offer_quantity) * offer_price
                quantity %= offer_quantity

        total_amount += quantity * prices[product]

    # account for free products

    for product, quantity in free_products.items():
        item_counts[product] -= min(item_counts[product], quantity)

    # add remaining item prices left in basket
    for product, quantity in item_counts.items():
        total_amount += quantity * prices[product]

    return total_amount

print(checkout('A'))
