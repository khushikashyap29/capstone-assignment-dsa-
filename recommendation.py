def recommend_friends(user, graph, users):
    suggestions = {}

    for friend in graph[user]:
        for fof in graph[friend]:
            if fof != user and fof not in graph[user]:
                common = len(set(users[user]["interests"]) &
                             set(users[fof]["interests"]))
                suggestions[fof] = common

    # sort by common interests
    return sorted(suggestions.items(), key=lambda x: x[1], reverse=True)