# test_cases.py

from profiles import *
from graph import *
from bfs_dfs import bfs_shortest_path, dfs
from recommendation import recommend_friends

print("------ TEST CASES START ------\n")

# 🔷 1. Add Users
add_user(1, "A", ["music", "coding"])
add_user(2, "B", ["sports", "music"])
add_user(3, "C", ["coding", "art"])
add_user(4, "D", ["art", "music"])
add_user(5, "E", ["sports", "coding"])
add_user(6, "F", ["music", "gaming"])

# 🔷 2. Update Profiles
update_profile(1, interests=["music", "coding", "AI"])
update_profile(3, name="C Updated")

# 🔷 3. Add users to graph
for i in range(1, 7):
    add_user_to_graph(i)

# 🔷 4. Create Connections (10 connections)
add_friend(1,2)
add_friend(1,3)
add_friend(2,3)
add_friend(2,4)
add_friend(3,5)
add_friend(4,5)
add_friend(4,6)
add_friend(5,6)
add_friend(1,6)
add_friend(2,5)

# 🔷 5. Remove one connection
remove_friend(2,4)

# 🔷 6. Show Profiles
print("Profiles:")
print(get_profile(1))
print(get_profile(2))
print(get_profile(3))
print()

# 🔷 7. BFS Test (Shortest Path)
print("BFS Shortest Path Tests:")
print("1 → 6:", bfs_shortest_path(graph, 1, 6))
print("2 → 6:", bfs_shortest_path(graph, 2, 6))
print()

# 🔷 8. DFS Test
print("DFS Tests:")
print("Depth 2 from 1:", dfs(graph, 1, 2))
print("Depth 3 from 1:", dfs(graph, 1, 3))
print()

# 🔷 9. Recommendation Test
print("Friend Recommendations for User 1:")
print(recommend_friends(1, graph, users))

print("\n------ TEST CASES END ------")