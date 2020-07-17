from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# room_traversals = {}
# def check_if_paths_explored(room):
#     if room_traversals[room]['n'] != '' and room_traversals[room]['e'] != '' and room_traversals[room]['s'] != '' and room_traversals[room]['w'] != '':
#         return True
#     else:
#         return False

# def get_opposite(direction):
#     if direction == 'n':
#         return 's'
#     elif direction == 's':
#         return 'n'
#     elif direction == 'e':
#         return 'w'
#     else:
#         return 'e'



# Fill this out with directions to walk
traversal_path = []
valid_dir = {}
directions = ['n', 'e', 's', 'w']
stack = Stack()
stack.push(player.current_room)
visited = set()

# while len(room_traversals) < len(room_graph):
#     # print(stack.size())
#     room = stack.pop()
#     # add room to room_traversals if not there
#     if room not in room_traversals:
#         room_traversals[room.id] = { 'n': '', 'e': '', 's': '', 'w': ''}
#         # valid_dir={'n': 'x', 'e': 'x', 's': 'x', 'w': 'x'}
#         # get  all valid directions
#         # for valid_direction in room.get_exits():
#         #     valid_dir[room.id][valid_direction] = room.get_room_in_direction(valid_direction).id
#         # for direction, room in room_traversals[room.id].items():
#             # if room != '?':
#             #     traversal_path.append(direction)
#             #     stack.push(player.current_room)
#             #     player.travel(direction)
#         random_dir = random.choice(player.current_room.get_exits())
#         random_dir1 = random.choice(directions)
#         if player.current_room.get_room_in_direction(random_dir1) != None:
#             traversal_path.append(random_dir1)
#             player.travel(random_dir1)
#             room_traversals[room.id][random_dir1] = player.current_room.id
#             stack.push(player.current_room)
#             if player.current_room.id in room_traversals:
#                 if check_if_paths_explored(player.current_room.id) == True:
#                     print("EXPLORED")
#         else:
#             room_traversals[room.id][random_dir1] = 'x'
#             stack.push(player.current_room)
#         print(room_traversals)
#         # print(len(room_traversals))

# while len(room_traversals) < len(room_graph):
#     # print(stack.size())
#     room = stack.pop()
#     # add room to room_traversals if not there
#     if room not in room_traversals:
#         room_traversals[room.id] = { 'n': '', 'e': '', 's': '', 'w': ''}
#         for 
    




# def recursive_traversal(stack):
#     room = stack.pop()
#     # print(room.id)
#     if room.id not in room_traversals:
#         room_traversals[room.id] = { 'n': '', 'e': '', 's': '', 'w': ''}
#         for direction in directions:
#             traversal_path.append(direction)
#             if room_traversals[room.id][direction] == '' and player.travel(direction,True) != False :
#                 room_traversals[room.id][direction] = player.current_room.id
#             else:
#                 room_traversals[room.id][direction] = 'x'
#             stack.push(player.current_room)
#             if check_if_paths_explored(room.id) == True:
#                 return 
#             recursive_traversal(stack)
# recursive_traversal(stack)
# print(room_traversals)


# def recursive_traversal(stack, opposite_last = ''):
#     if stack.size() <= 0:
#         return 
#     room = stack.pop()
#     if room.id not in room_traversals:
#         room_traversals[room.id] = { 'n': '', 'e': '', 's': '', 'w': ''}
#     non_valid = ['n', 'e', 's', 'w']
#     valid_directions = room.get_exits()
#     for direction in valid_directions:
#         non_valid.remove(direction)
#     for direction in non_valid:
#         room_traversals[room.id][direction] = 'x'
#     direction = valid_directions.pop()
#     if direction != opposite_last:
#         traversal_path.append(direction)
#         player.travel(direction, True)
#         stack.push(player.current_room)
#         if player.current_room.id not in room_traversals:
#             room_traversals[player.current_room.id] = { 'n': '', 'e': '', 's': '', 'w': ''}
#         if check_if_paths_explored(room.id) == True:
#             return recursive_traversal(stack, direction)
#         return recursive_traversal(stack, get_opposite(direction))
    

        
    
# recursive_traversal(stack)
# print(room_traversals)

# print(check_if_paths_explored(2))

# room_traversals[0]['n'] = 1
# print(room_traversals[0]['n'])


def check_if_unexplored(room_traversals):
    for explored in room_traversals.values():
        for value in explored.values():
            if "?" == value:
                return True
    return False

def get_unexplored(starting_node, room_traversals):
    history = set()
    queue = Queue()
    queue.enqueue([starting_node.id])

    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]

        if v not in history:
            if "?" in room_traversals[v].values():
                return path
            history.add(v)

            for value in room_traversals[v].values():
                newPath = list(path)
                newPath.append(value)
                queue.enqueue(newPath)

def move_unknown(room):
    for direction in player.current_room.get_exits(): 
        if player.current_room.get_room_in_direction(direction).id == room:
            traversal_path.append(direction)
            player.travel(direction)
            return


room_traversals = {}
# Until we have visited all the rooms
while len(room_traversals) < len(world.rooms):
    if player.current_room.id not in room_traversals:
        room_traversals[player.current_room.id] = {}

        for room in player.current_room.get_exits():
            room_traversals[player.current_room.id][room] = "?" 

    # Traverse unexplored first
    if "?" in list(room_traversals[player.current_room.id].values()):
        rand = [None, None]

        while rand[1] != "?":
            rand = list(random.choices(list(room_traversals[player.current_room.id].items()))[0]) 
        
        traversal_path.append(rand[0])
        room_traversals[player.current_room.id][rand[0]] = player.current_room.get_room_in_direction(rand[0]).id  
        player.travel(rand[0])
    
    # Dead end. Cheack if there is more to explore
    elif check_if_unexplored(room_traversals):
        directions = get_unexplored(player.current_room, room_traversals)
        directions.pop(0) 
        for room in directions:
            move_unknown(room)  



# TRAVERSAL TEST
room_traversals_rooms = set()
player.current_room = world.starting_room
room_traversals_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    room_traversals_rooms.add(player.current_room)

if len(room_traversals_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(room_traversals_rooms)} rooms room_traversals")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(room_traversals_rooms)} unroom_traversals rooms")



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
