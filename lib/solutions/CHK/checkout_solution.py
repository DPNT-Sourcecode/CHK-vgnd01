

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    # if sku not in prices then return -1
    for product in skus:
        if product not in prices:
            return -1


