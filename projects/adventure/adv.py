from room import Room
from player import Player
from world import World
from util import Stack
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

room_traversals = {}
def check_if_paths_explored(room):
    if room_traversals[room]['n'] != '' and room_traversals[room]['e'] != '' and room_traversals[room]['s'] != '' and room_traversals[room]['w'] != '':
        return True
    else:
        return False

def get_opposite(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    else:
        return 'e'



# Fill this out with directions to walk
traversal_path = []
directions = ['n', 'e', 's', 'w']
stack = Stack()
stack.push(player.current_room)
visited = set()

# print(world.grid_size)
while len(room_traversals) < 500:
    # print(stack.size())
    room = stack.pop()
    # add room to visited if not there
    if room not in room_traversals:
        room_traversals[room.id] = { 'n': '?', 'e': '?', 's': '?', 'w': '?'}
        # get  all valid directions
        for valid_direction in room.get_exits():
            room_traversals[room.id][valid_direction] = room.get_room_in_direction(valid_direction).id
        # for direction, room in room_traversals[room.id].items():
            # if room != '?':
            #     traversal_path.append(direction)
            #     stack.push(player.current_room)
            #     player.travel(direction)
        random_dir = random.choice(player.current_room.get_exits())
        traversal_path.append(random_dir)
        player.travel(random_dir)
        stack.push(player.current_room)
        # print(room_traversals)
        # print(len(room_traversals))




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
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
