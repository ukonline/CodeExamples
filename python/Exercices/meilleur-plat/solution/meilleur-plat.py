def stats(votes):
    '''Extract stats about meal preferences from the specified votes'''
    best = -1
    bestmeals = set()
    meals = {}
    for meal in votes:
        sumvote = 0
        nb = 0
        for name in votes[meal]:
            vote = votes[meal][name]
            if vote > best:
                best = vote
                bestmeals = {meal}
            elif vote == best:
                bestmeals.add(meal)
            sumvote += vote
            nb += 1
        meals[meal] = sumvote / nb
    return {'bestmeals': bestmeals, 'meals': meals}


votes = {
    "Pavé de biche aux airelles": {"Clémence": 9, "Quentin": 7, "Cédric": 2},
    "Paupiette de Seitan": {"Clémence": 4, "Quentin": 6},
    "Foie gras aux St Jacques": {"Quentin": 8, "Cédric": 1},
    "Dinde de Noël farcie aux pommes et noix": {"Quentin": 9, "Cédric": 4}
}
print(stats(votes))