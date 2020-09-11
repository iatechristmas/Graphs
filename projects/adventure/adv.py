from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# print("current room id", player.current_room.id)
# print("exits for current room", player.current_room.get_exits())
# print("current room id", player.travel(direction))

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []

def traverse(player):
    visited = dict()
    q = Queue()
    q.enqueue([player.current_room.id])

    while len(visited) != len(world.rooms):
    # while q.size():
        # v = q.dequeue()
        # print(v)

        if player.current_room.id not in visited:
            visited[player.current_room.id] = dict()
            # print(f"v in traverse is {v}")

            for door in player.current_room.get_exits():
                visited[player.current_room.id][door] = "?"

        if "?" in visited[player.current_room.id].values():
            
            # print(random_door)
            # print("values", visited[player.current_room.id].values())
            # print("keys", visited[player.current_room.id].keys())
            # print("items", visited[player.current_room.id].items())
            # random_door = random.choice(visited[player.current_room.id].items())
            # while random_door[1] != "?":
            #     random_door = (random)
            # for item in visited[player.current_room.id].items():
                # print("item in item loop", item)
                # if item[1] == "?":
                #     print("item in nested item loop", item)
                    # print("get room direction", player.current_room.get_room_in_direction(item[0]))
                    
                    # visited[player.current_room.id][item[1]] = player.current_room.get_room_in_direction(item[0]).id
                    # print("visited player at index", visited[player.current_room.id][item[0]])
                    # traversal_path.append(item)
                    # print("item in nested item loop after", item)
                    # player.travel(item[0])
                    # print(f"player moved {item[0]} to {item[1]}")
            random_room = [None, None]
            while random_room[1] != "?":
                random_room = list(random.choices(list(visited[player.current_room.id].items()))[0]) # ['n', '?']
            traversal_path.append(random_room[0])
            visited[player.current_room.id][random_room[0]] = player.current_room.get_room_in_direction(random_room[0]).id  
            player.travel(random_room[0])

        elif find_question_mark(visited):
            directions = find_nearest_unknown(player.current_room, visited)
            directions.pop(0)
            for i in directions:
                move_one_to_unknown(i)

        else:
            return visited
            

def find_nearest_unknown(starting_node, visited):
    history = set()
    q = Queue()
    q.enqueue([starting_node.id])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in history:
            if "?" in visited[v].values():
                return path
            history.add(v)

            for value in visited[v].values():
                newPath = list(path)
                newPath.append(value)
                q.enqueue(newPath)

def find_question_mark(visited):
    for i in visited.values():
        for value in i.values():
            if "?" == value:
                return True

    return False

def move_one_to_unknown(i):
    for letter in player.current_room.get_exits(): # west, north, etc
        if player.current_room.get_room_in_direction(letter).id == i:
            # Move player there
            traversal_path.append(letter)
            player.travel(letter)
            return


            # for next_vert in self.get_neighbors(v):
            #     q.enqueue(next_vert)
        # vertices[player.current_room.id] = set()
        # player.current_room.id
        # player.current_room.get_exits()


# player.travel(direction)

visited = traverse(player)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print("move", move)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
