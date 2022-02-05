from math import sqrt
import csv
import random
import time

def dist(a, b):
    d = [a[0] - b[0], a[1] - b[1]]
    return sqrt(d[0] * d[0] + d[1] * d[1])

def calculateCost(cords):
    D = []
    for city1, cords1 in enumerate(cords.items()):
        D.insert(city1, [])
        for city2, cords2 in enumerate(cords.items()):
            D[city1].insert(city2, dist(cords1[1], cords2[1]) )
    return D


def populate_cordinates_from_file(filename):
    rows = []
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        cr = 0
        for row in reader:
            #skip first row
            if cr == 0:
                cr+=1
                continue
            rows.append(row)
            cr+=1
            # process each row
    cords ={}
    for row in rows:
        if row[0] not in cords:
            cords[row[0]] = (float(row[1]),float(row[2]))
    return cords

def generate_route(length):
    routes = []
    for index in range(0,length):
        routes.append(index)
    random.shuffle(routes)
    routes.insert(len(routes),routes[0])
    return routes

def get_cost_of_route(cities, routes):
    cost = 0.0
    for i in range(len(routes) -1):
        cost += cities[routes[i]][routes[i + 1]]
    return cost

def random_search_with_time_limit(cities, time_limit):
    best_route = []
    for i in range(0, time_limit):
        current_route = generate_route(len(cities))
        #print("Current ", current_route)
        cost_current_route = get_cost_of_route(cities,current_route)
        cost_best_route = get_cost_of_route(cities,best_route)
        if cost_current_route > cost_best_route:
           best_route = current_route
        time.sleep(1)
        #print("Best ", best_route)
    return best_route


# A     B     C     D
# A       0     20    42    35
# B       20    0     30    34
# C       42    30    0     12
# D       35    34    12    0
cities  = [[0, 20, 42, 35],[20,0, 20, 34], [42, 30, 0, 12], [35, 34, 12, 0]]

print(cities[0][1])

routes = generate_route(3)

cost = get_cost_of_route(cities,routes)

print(cost)

cordinates = populate_cordinates_from_file("ulysses16.csv")

cities = calculateCost(cordinates)

routes = generate_route(5)

cost = get_cost_of_route(cities,routes)

print(cost)

print(random_search_with_time_limit(cities, 100))