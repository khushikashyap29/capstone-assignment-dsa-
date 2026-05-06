# main.py

from profiles import *
from graph import *
from bfs_dfs import bfs_shortest_path, dfs
from recommendation import recommend_friends

def setup_data():
    # 🔷 Add Users
    add_user(1, "A", ["music", "coding"])
    add_user(2, "B", ["sports", "music"])
    add_user(3, "C", ["coding", "art"])
    add_user(4, "D", ["art", "music"])
    add_user(5, "E", ["sports", "coding"])
    add_user(6, "F", ["music", "gaming"])

    # 🔷 Update Profiles
    update_profile(1, interests=["music", "coding", "AI"])
    update_profile(3, name="C Updated")

    # 🔷 Add users to graph
    for i in range(1, 7):
        add_user_to_graph(i)

    # 🔷 Create Connections
    add_friend(1, 2)
    add_friend(1, 3)
    add_friend(2, 3)
    add_friend(2, 4)
    add_friend(3, 5)
    add_friend(4, 5)
    add_friend(4, 6)
    add_friend(5, 6)
    add_friend(1, 6)
    add_friend(2, 5)

    # 🔷 Remove one connection
    remove_friend(2, 4)


def show_menu():
    print("\n====== Social Network Explorer ======")
    print("1. Show Profiles")
    print("2. Show Friends")
    print("3. BFS Shortest Path")
    print("4. DFS Exploration")
    print("5. Friend Recommendations")
    print("6. Exit")


def main():
    setup_data()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            print("\n--- Profiles ---")
            for user_id in users:
                print(user_id, ":", get_profile(user_id))

        elif choice == "2":
            user = int(input("Enter user ID: "))
            print("Friends:", get_friends(user))

        elif choice == "3":
            u = int(input("Start user: "))
            v = int(input("End user: "))
            print("Shortest Path:", bfs_shortest_path(graph, u, v))

        elif choice == "4":
            u = int(input("Start user: "))
            d = int(input("Depth: "))
            print("DFS Result:", dfs(graph, u, d))

        elif choice == "5":
            u = int(input("Enter user: "))
            print("Recommendations:", recommend_friends(u, graph, users))

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()