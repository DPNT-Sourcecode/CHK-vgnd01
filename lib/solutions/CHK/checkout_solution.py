

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offer = {'A': (3, 130), 'B': (2, 45)}

    # if sku not in prices then return -1
    for product in skus:
        if product not in prices:
            return -1

    # use Counter to keep track of each product
    from collections import Counter
    item_counts = Counter(skus)

    total_amount = 0

    for product, quantity in item_counts.items():
        if product in offer:
            offer_quantity, offer_price = offer[product]
            total_amount += (quantity // offer_quantity) * offer_price
            total_amount += (quantity % offer_quantity) * prices[product]
        else:
            total_amount += quantity * prices[product]

    return total_amount
