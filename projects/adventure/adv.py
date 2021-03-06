from room import Room
from player import Player
from world import World
from util import Stack,Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
########################################
#BASIC IDEA 
#We record the room we in to visited dict
#Find all the exits for that room
#Move in 1 direction - record that direction to traversal_path 
#and pop off direction connected to the room
#Find opposite direction - add that to opposite/reverse path. 
#This will help with going backwards when possible.
#also remove the opposite direction from paths not traveled yet
#Find exits for new room - store them in visited
#Move in a different direction, add that to traversap_path - pop it off possible direction
# Move till you get to the end and cannot move anymore
# Once there are no more exits - go backwards the same way and remove that from backwrds path
# add that to the traversal_path
#Check that room for more drections and repeat the process(traversal)
#This will happen till the visited rooms = len(room_graph)
#######################################

# Fill this out with directions to walk
#breakpoint()
traversal_path = []
#traversal_path = ['n','n']
visited = {}
#store the paths -main path
main_path = []
#append current room to visited 
#how to move in oppoiste direction
oppoiste_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# at the given room(first) to dictionary - find the exit
visited[player.current_room.id] = player.current_room.get_exits()
#print(visited)

# Begin BFS 
#While the length of visited rooms is less than graph rooms. we need to keep going
while len(visited) < len(room_graph) -1:
    #find out if the visited room is in the visited dict - if we have been there before
    if player.current_room.id not in visited:
        #if its not - we add it to visited with its id and find exit
        visited[player.current_room.id] = player.current_room.get_exits()
        #find the prev direction
        direction_before = main_path[-1]
        #to avoid gofing that directon - remove that path
        visited[player.current_room.id].remove(direction_before)
        #print(direction_before)
    #change direction/traversal to look at all rooms
    if len(visited[player.current_room.id])== 0:
        #get rid of the previous exit
        direction_before = main_path.pop()
        #add those exits to traversal_path
        traversal_path.append(direction_before)
        #print(traversal_path)
        #move player to previous room and check if we visited before
        player.travel(direction_before)

    #else if there are directions not expoited
    # add that direction to the traversal_path
    # go eslore new room     
    #find the current exit to the room and last room in list -> go to that room
    else:
        move_to_next_room = visited[player.current_room.id].pop(0)
        #visited[player.current_room.id].pop()
        #add that move to the traversal_path
        traversal_path.append(move_to_next_room) 
        #also add it to the main path
        main_path.append(oppoiste_direction[move_to_next_room])
        #go backwards through rooms
        player.travel(move_to_next_room)



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
