from collections import defaultdict
from queue import Queue, PriorityQueue



class Search():
    def __init__(self, size, start, goal, matrix):
        self.size = size
        self.start = start
        self.goal = goal
        self.matrix = matrix


    @classmethod
    def fromFile(cls, file):
        size = int(file.readline())
        start, goal = [int(num) for num in file.readline().split(' ')]
        matrix = [[int(num) for num in line.split(' ')] for line in file]
        return cls(size,start,goal,matrix)
    

    def convert_graph(self):
        a = self.matrix
        adjList = defaultdict(list)
        for i in range (len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1:
                    adjList[i].append(j)
        return adjList
    

    def BFS_search(self):
        graph = self.convert_graph()
        visited = []
        frontier = Queue()


        # Thêm node start vào frontier và visited
        frontier.put(self.start)
        visited.append(self.start)

        # start không có node cha
        parent = dict()
        parent[self.start] = None

        path_found = False

        while True:
            if frontier.empty():
                raise Exception("No way Exception")
            current_node = frontier.get()
            visited.append(current_node)

            # Kiểm tra current_node có là end hay không
            if current_node == self.goal:
                path_found = True
                break

            for node in graph[current_node]:
                if node not in visited:
                    frontier.put(node)
                    parent[node] = current_node
                    visited.append(node)

        end = self.goal
        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
        return path




class BFS():
    def __init__(self,start,goal,graph):
        super().__init__(None, start, goal)
        self.graph = self.convert_graph(self)

    def check_path(self):
        visited = []
        frontier = Queue()


        # Thêm node start vào frontier và visited
        frontier.put(self.start)
        visited.append(self.start)

        # start không có node cha
        parent = dict()
        parent[self.start] = None

        path_found = False

        while True:
            if frontier.empty():
                raise Exception("No way Exception")
            current_node = frontier.get()
            visited.append(current_node)

            # Kiểm tra current_node có là end hay không
            if current_node == self.goal:
                path_found = True
                break

            for node in self.graph[current_node]:
                if node not in visited:
                    frontier.put(node)
                    parent[node] = current_node
                    visited.append(node)

        return path_found, parent
    
    def print_path(self):
        path_found, parent = self.check_path()
        end = self.goal
        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
        return path


file_1 = open("Input.txt", "r")

tree = TreeSearch.fromFile(file_1)

print(tree.BFS_search())