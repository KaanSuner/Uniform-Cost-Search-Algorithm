import csv
import os.path
from os import path
from queue import PriorityQueue

class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


class FileNotFoundError(Exception):
    def __init__(self, data):
        print("%s does not exist" % data)

def build_graph(path):
    cities = {}
    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            if not row[0] in cities:
                cities[row[0]] = {}
            cities[row[0]][row[1]] = int(row[2])

            if not row[1] in cities:
                cities[row[1]] = {}
            cities[row[1]][row[0]] = int(row[2])
    return cities


def uniform_cost_search(graph, start, end):
    traveled = []
    Q = PriorityQueue()
    Q.put((0, [start]))

    while not Q.empty():
        travel = Q.get()
        travel_point = travel[1][-1]
        travel_distance = travel[0]

        if travel_point == end:
            print(str(travel[1]) + " Travel Cost: " + str(travel_distance))
            exit()

        traveled.append(travel_point)

        for each in graph[travel_point]:
            if each not in traveled:
                distance = travel_distance + graph[travel_point][each]
                Q.put((distance, travel[1] + [each]))


def first():
    start = input("Enter current city: ")
    while True:
        try:
            if start not in graph:
                raise CityNotFoundError(start)
            break
        except CityNotFoundError:
            start = input("Error. Enter valid city: ")
    return start


def last():
    end = input("Enter target city: ")
    while True:
        try:
            if end not in graph:
                raise CityNotFoundError(end)
            break
        except CityNotFoundError:
            end = input("Error. Enter valid city: ")
    return end


def userinput():
    filepath = input("Enter file path:")
    while True:
        try:
            if not (path.isfile(filepath)):
                raise FileNotFoundError(filepath)
            break
        except FileNotFoundError:
            filepath = input("Error! Enter valid file path: ")
    return filepath

        
if __name__ == "__main__":
    pathinfo=userinput()
    graph = build_graph(pathinfo)
    departure=first()
    destination=last()
    uniform_cost_search(graph, departure, destination)        


