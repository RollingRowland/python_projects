from data import *
from bfs import *

#Request the user provide a start and end point

start_pos = str(input("What country are you travelling from?\n"))
end_pos = str(input("What country would you like to travel to?\n"))

start_pos = start_pos.title()
end_pos = end_pos.title()

#Check these are valid countrys

if (start_pos in flight_graph.keys()) and (end_pos in flight_graph.keys()):
    print("Leaving from: {0}\nArriving in: {1}".format(start_pos,end_pos))
else:
    print("Invalid destinations selected")

#Provide a series of flight routes to their destination

print("Possible flight routes are:")

flight_routes = bfs(flight_graph, start_pos, end_pos)

for route in flight_routes:
    print(route)




