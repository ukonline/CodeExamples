def unitprice(item, quantity):
    '''Get the unit price for an item given the ordered quantity'''
    if 1 <= quantity < 10:
        return item[1]
    elif 10 <= quantity < 50:
        return item[2]
    return item[3]

def bestdeal(items, order):
    '''Find the item for which the customer made the best deal'''
    bestitem = -1
    bestdiff = float("-inf")
    for i in range(len(order)):
        # Compute price for the ith item
        quantity = order[i]
        price = unitprice(items[i], quantity) * quantity
        # Check difference with unit price
        diff = (items[i][1] * quantity) - price
        if diff > bestdiff:
            bestdiff = diff
            bestitem = i
    return items[bestitem][0]


items = [
    ["Clémentine", 0.5, 0.4, 0.2],
    ["Sapin Nordmann 80cm", 25, 22, 18],
    ["Foie gras 100g", 12.5, 10, 7]
]
order = [15, 10, 2]
print(bestdeal(items, order))