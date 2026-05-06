# graph.py

graph = {}

def add_user_to_graph(user):
    if user not in graph:
        graph[user] = []

def add_friend(u, v):
    graph[u].append(v)
    graph[v].append(u)

def remove_friend(u, v):
    graph[u].remove(v)
    graph[v].remove(u)

def get_friends(user):
    return graph.get(user, [])