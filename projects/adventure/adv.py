from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
stack = [player.current_room.id]
map_size = 500
rooms_visited = 1
traveled_map = {player.current_room.id: {}}

while rooms_visited < map_size:
    #add base room to the stack
    #add one child to the stack - do this until you hit a dead end (add direction to traversal_path each time)
    #remove from stack until you get to a node with an open path
    if 'n' in player.current_room.get_exits() and player.current_room.n_to.id not in traveled_map:
        traveled_map[player.current_room.id]['n'] = player.current_room.n_to.id
        traveled_map[player.current_room.n_to.id] = {'s': player.current_room.id}
        traversal_path.append('n')
        stack.append(player.current_room.n_to.id)
        player.travel('n')
        rooms_visited += 1
    elif 's' in player.current_room.get_exits() and player.current_room.s_to.id not in traveled_map:
        traveled_map[player.current_room.id]['s'] = player.current_room.s_to.id
        traveled_map[player.current_room.s_to.id] = {'n': player.current_room.id}
        traversal_path.append('s')
        stack.append(player.current_room.s_to.id)
        player.travel('s')
        rooms_visited += 1
    elif 'e' in player.current_room.get_exits() and player.current_room.e_to.id not in traveled_map:
        traveled_map[player.current_room.id]['e'] = player.current_room.e_to.id
        traveled_map[player.current_room.e_to.id] = {'w': player.current_room.id}
        traversal_path.append('e')
        stack.append(player.current_room.e_to.id)
        player.travel('e')
        rooms_visited += 1
    elif 'w' in player.current_room.get_exits() and player.current_room.w_to.id not in traveled_map:
        traveled_map[player.current_room.id]['w'] = player.current_room.w_to.id
        traveled_map[player.current_room.w_to.id]= {'e': player.current_room.id}
        traversal_path.append('w')
        stack.append(player.current_room.w_to.id)
        player.travel('w')
        rooms_visited += 1
    #dead end case
    else:
        stack.pop()
        if 'n' in player.current_room.get_exits() and traveled_map[player.current_room.id]['n'] == stack[-1]:
            traversal_path.append('n')
            player.travel('n')
        elif 's' in player.current_room.get_exits() and traveled_map[player.current_room.id]['s'] == stack[-1]:
            traversal_path.append('s')
            player.travel('s')
        elif 'e' in player.current_room.get_exits() and traveled_map[player.current_room.id]['e'] == stack[-1]:
            traversal_path.append('e')
            player.travel('e')
        elif 'w' in player.current_room.get_exits() and traveled_map[player.current_room.id]['w'] == stack[-1]:
            traversal_path.append('w')
            player.travel('w')

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
