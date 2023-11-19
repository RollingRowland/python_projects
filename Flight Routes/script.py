from data import *
from bfs import *



def main():

    #Ask the user if they need a list of destinations
    destination_question = str(input("Do you need a list of valid destinations? y/n"))
    if destination_question == "y":
        for country in flight_graph.keys():
            print(country)
    
    #Request the user provide a start and end point
    start_pos = str(input("What country are you travelling from?\n"))
    end_pos = str(input("What country would you like to travel to?\n"))


    #Check these are valid countrys

    if (start_pos in flight_graph.keys()) and (end_pos in flight_graph.keys()):
        print("Leaving from: {0}\nArriving in: {1}".format(start_pos,end_pos))
    else:
        print("Invalid destinations selected")
        return

    #Provide a series of flight routes to their destination

    print("Possible flight routes are:")

    flight_routes = bfs(flight_graph, start_pos, end_pos)

    for route in flight_routes:
        print(route)

    return


main()
repeat = str(input("Would like some new route recommendations? y/n\n"))

#Keep asking whether they want more recommendations until they say no
while repeat == "y":
    main()
    repeat = str(input("Would like some new route recommendations? y/n\n"))




