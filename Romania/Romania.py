#
#   Created by PyCharm.
#   User: Rizky Andre Wibisono
#   Date: 17/03/2019
#   Time: 20:59
#

#
#   Adopted by Wen-Chung Cheng (Andy) for
#   A1 of Intro to AI course at Florida Atlantic University
#   User: Wen-Chung Cheng (Andy)
#   Date: 06/10/2021
#   Time: 19:25
#

import heapq


class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)

# class priorityStack:
#     def __init__(self):
#         self.cities = []

#     def push(self, city, cost):
#         heapq.heappush(self.cities, (cost, city))

#     def pop(self):
#         return heapq.heappop(self.cities)[1]

#     def isEmpty(self):
#         if (self.cities == []):
#             return True
#         else:
#             return False

#     def check(self):
#         print(self.cities)


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


romania = {}


def makedict():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist))


def makehuristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h


def heuristic(node, values):
    return values[node]


def getList(dict):
    return [*dict]


def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        # print(current, "now : " + str(distance[current]))
        # print(distance)
        # print(q.cities)
        expandedList.append(current) # visited_points.append

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance or g_cost < distance[new.city]):
                # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current

            # if (g_cost < distance[new.city]):
            #     # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)
            #     distance[new.city] = g_cost
            #     f_cost = g_cost + heuristic(new.city, h)
            #     q.push(new.city, f_cost)
            #     path[new.city] = current


    printoutputAstar(start, end, path, distance, expandedList)


def run_dfs_ultra_alt(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        # print(current, "now : " + str(distance[current]))
        # print(distance)
        # print(q.cities)
        expandedList.append(current) # visited_points.append

        if (current == end):
            break

        for new in romania[current]:
            # path[new.city] = current
            g_cost = distance[current] + int(new.distance)
            # distance[new.city] = g_cost
            # f_cost = g_cost + heuristic(new.city, h)
            # q.push(new.city, f_cost)
            # path[new.city] = current

            # # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance):
                # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current


    printoutputDFS(start, end, path, distance, expandedList)


def run_bfs_alt(start, end):

    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    # Append the current node to the queue
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    if start == end:
        printoutputBFS(start, end, path, distance, expandedList)
    else:
        # Keep searching while there are nodes in the queue
        while (q.isEmpty() == False):
            # Set the next node in the queue as the current node
            current_point = q.pop()
            expandedList.append(current_point)
            # Get the neighbors of the current node
            # neighbors = mp.neighbors(start)
            neighbors = romania[current_point]
            # Iterate through the neighbors of the current node
            for neighbor in neighbors:
                # Add the neighbor to the queue if it hasn't been visited
                if neighbor.city not in distance:
                    g_cost = distance[current_point] + int(neighbor.distance)
                    distance[neighbor.city] = g_cost
                    f_cost = g_cost + heuristic(neighbor.city, h)
                    # mp.set_parent(neighbor, current_point, points)
                    path[neighbor.city] = current_point
                    q.push(neighbor.city, f_cost)
                    # Return the path to the current neighbor if it is the goal
                    if neighbor.city == end:
                        printoutputBFS(start, end, path, distance, expandedList)
        # In the case that no path to the goal was found
        return 'No path to the goal found.'



def run_bfs(start, end):

    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    # Append the current node to the queue
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    expandedList.append(start)

    if start == end:
        printoutputBFS(start, end, path, distance, expandedList)
    else:
        # Keep searching while there are nodes in the queue
        while (q.isEmpty() == False):
            # Set the next node in the queue as the current node
            current_point = q.pop()
            # expandedList.append(current_point)
            # Get the neighbors of the current node
            # neighbors = mp.neighbors(start)
            neighbors = romania[current_point]
            # Iterate through the neighbors of the current node
            for neighbor in neighbors:
                # Add the neighbor to the queue if it hasn't been visited
                if neighbor.city not in expandedList:
                    g_cost = distance[current_point] + int(neighbor.distance)
                    distance[neighbor.city] = g_cost
                    f_cost = g_cost + heuristic(neighbor.city, h)
                    # mp.set_parent(neighbor, current_point, points)
                    path[neighbor.city] = current_point
                    q.push(neighbor.city, f_cost)
                    expandedList.append(neighbor.city)
                    # Return the path to the current neighbor if it is the goal
                    if neighbor.city == end:
                        printoutputBFS(start, end, path, distance, expandedList)
        # In the case that no path to the goal was found
        return 'No path to the goal found.'



def run_dfs(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    # distance[start] = 0
    path[start] = None
    expandedList = []

    # Keep searching while there are nodes in the stack
    while (q.isEmpty() == False):
        # Set the next node in the stack as the current node
        next_point = q.pop()
        # If the current node hasn't already been exploited, search it
        if next_point not in distance:
            distance[next_point] = 0
            # g_cost = distance[current_point] + int(neighbor.distance)
            # distance[neighbor.city] = g_cost
            # distance[next_point] = 0
            # Return the path to the current neighbor if it is the goal
            if next_point == end:
                printoutputDFS(start, end, path, distance, expandedList)
            else:
                # Add the current node's neighbors to the stack
                neighbors = romania[next_point]
                for neighbor in neighbors:
                    path[neighbor.city] = next_point
                    g_cost = distance[next_point] + int(neighbor.distance)
                    distance[next_point] = g_cost
                    f_cost = g_cost + heuristic(neighbor.city, h)
                    q.push(neighbor.city, f_cost)
    return 'No path to the goal found.'


def run_dfs_alt(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    # Keep searching while there are nodes in the stack
    while (q.isEmpty() == False):
        # Set the next node in the stack as the current node
        next_point = q.pop()
        # If the current node hasn't already been exploited, search it
        if next_point not in expandedList:
            expandedList.append(next_point)
            # g_cost = distance[current_point] + int(neighbor.distance)
            # distance[neighbor.city] = g_cost
            # distance[next_point] = 0
            # Return the path to the current neighbor if it is the goal
            if next_point == end:
                printoutputDFS(start, end, path, distance, expandedList)
            else:
                # Add the current node's neighbors to the stack
                neighbors = romania[next_point]
                for neighbor in neighbors:
                    if neighbor.city == start:
                        pass
                    else:
                        path[neighbor.city] = next_point
                        g_cost = distance[next_point] + int(neighbor.distance)
                        distance[neighbor.city] = g_cost
                        f_cost = g_cost + heuristic(neighbor.city, h)
                        q.push(neighbor.city, f_cost)
    # return 'No path to the goal found.'
    # print('\nNo path to the goal found.')

def run_dfs_alt_alt(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = [start]

    # Keep searching while there are nodes in the stack
    while (q.isEmpty() == False):
        # Set the next node in the stack as the current node
        next_point = q.pop()

        neighbors = romania[next_point]
        for neighbor in neighbors:
            if neighbor.city == end:
                path[neighbor.city] = next_point
                # expandedList.append(neighbor.city)
                g_cost = distance[next_point] + int(neighbor.distance)
                distance[neighbor.city] = g_cost
                f_cost = g_cost + heuristic(neighbor.city, h)
                q.push(neighbor.city, f_cost)
                break
            else:
                if neighbor.city not in expandedList:
                    path[neighbor.city] = next_point
                    expandedList.append(neighbor.city)
                    g_cost = distance[next_point] + int(neighbor.distance)
                    distance[neighbor.city] = g_cost
                    f_cost = g_cost + heuristic(neighbor.city, h)
                    q.push(neighbor.city, f_cost)

    printoutputDFS(start, end, path, distance, expandedList)


def printoutputAstar(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    # print("Program algoritma Astar untuk masalah Romania")
    print('============================A* Search============================')
    print("\t\t\t\t\t" + start + " => Bucharest\n")
    # print("=======================================================")
    # print("Kota yg mungkin dijelajah \t\t: " + str(expandedlist))
    # print("Jumlah kemungkinan kota \t\t: " + str(len(expandedlist)))
    # print("=======================================================")
    # print("Kota yg dilewati dg jarak terpendek\t: " + str(finalpath))
    # print("Jumlah kota yang dilewati \t\t\t: " + str(len(finalpath)))
    # print("Total jarak: " + str(distance[end]))
    # print("Itinery Breakdown: ")
    for i in range(1, len(finalpath)):
        if i == 1:
            print('Itinery Breakdown: \t' + finalpath[i-1] + ' to ' + finalpath[i] + ':', distance[finalpath[i]] - distance[finalpath[i-1]], 'km')
        else:
            print('\t\t\t\t\t' + finalpath[i-1] + ' to ' + finalpath[i] + ':', distance[finalpath[i]] - distance[finalpath[i-1]], 'km')
    print("\t\t\t\t\tTotal distance: " + str(distance[end]) + " km")

    # for c in finalpath:
    #     last_city = c

def printoutputBFS(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print('============================Breadth-first Search============================')
    print("\t\t\t\t\t" + start + " => Bucharest\n")
    for i in range(1, len(finalpath)):
        if i == 1:
            print('Itinery Breakdown: \t' + finalpath[i-1] + ' to ' + finalpath[i] + ':', distance[finalpath[i]] - distance[finalpath[i-1]], 'km')
        else:
            print('\t\t\t\t\t' + finalpath[i-1] + ' to ' + finalpath[i] + ':', distance[finalpath[i]] - distance[finalpath[i-1]], 'km')
    print("\t\t\t\t\tTotal distance: " + str(distance[end]) + " km")

def printoutputDFS(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print('============================Depth-first Search============================')
    print("\t\t\t\t\t" + start + " => Bucharest\n")
    for i in range(1, len(finalpath)):
        if i == 1:
            print('Itinery Breakdown: \t' + finalpath[i-1] + ' to ' + finalpath[i] + ':', distance[finalpath[i]] - distance[finalpath[i-1]], 'km')
        else:
            print('\t\t\t\t\t' + finalpath[i-1] + ' to ' + finalpath[i] + ':', distance[finalpath[i]] - distance[finalpath[i-1]], 'km')
    print("\t\t\t\t\tTotal distance: " + str(distance[end]) + " km")



def main():

    Cont = True
    Cities = getList(makehuristikdict())
    # print(Cities[0])
    # print(makehuristikdict())
    makedict()
    # print(makedict())
    # print(romania['Arad'])

    while Cont:
        
        print('List of cities: ')
        for c in Cities:
            print('\t\t\t\t' + c)

        starting_point = input("Location of departure: ")

        while starting_point not in Cities:
            print('\nList of cities: ')
            for c in Cities:
                print('\t\t\t\t' + c)
            starting_point = input("Location not on map, try again: ")

        algo = input("Solution to be used (A: A*/ B: BFS/ D: DFS): ")

        while algo != 'A' and algo != 'B' and algo != 'D' and algo != 'a' and algo != 'b' and algo != 'd' and algo != 'A*' and algo != 'BFS' and algo != 'DFS' and algo != 'a*' and algo != 'bfs' and algo != 'dfs':
            algo = input("This solution does not exist, try again (A: A*/ B: BFS/ D: DFS): ")

        # src = "Arad"
        src = starting_point
        dst = "Bucharest"

        if algo == 'A' or algo == 'a':
            # print('---A* Search---')
            astar(src, dst)

        elif algo == 'B' or algo == 'b':
            # print('---Breadth-first Search---')
            run_bfs(src, dst)
            # run_bfs_alt(src, dst)

        elif algo == 'D' or algo == 'd':
            # print('---Depth-first Search---')
            # run_dfs_alt_alt(src, dst)
            # run_dfs_alt(src, dst)
            # run_dfs(src, dst)
            run_dfs_ultra_alt(src, dst)


        answer = input("Another city? (Y/N): ")
        while answer != 'y' and answer != 'n' and answer != 'Y' and answer != 'N' and answer != 'yes' and answer != 'no' and answer != 'Yes' and answer != 'No':
            answer = input("Invalid answer, try again (Y/N): ")
        if answer == 'Y' or answer == 'y' or answer == 'Yes' or answer == 'yes':
            pass
        else:
            Cont = False
            print("\nGood bye!")


if __name__ == "__main__":
    main()
