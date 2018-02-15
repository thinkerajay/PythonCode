from collections import deque

class Graph:
    def __init__(self):
        self.vertices = dict()

    def insert_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = {'out': [], 'in':[]}

    def insert_edge(self, u, v):
        self.vertices[u]['out'].append(v)
        self.vertices[v]['in'].append(u)

    def display(self):
        from pprint import pprint
        pprint(self.vertices)

    def path_exists(self, u, v):
        path = deque()
        visited = dict()
        visited[u] = True
        for adjacent in self.vertices[u]['out']:
            path.append(adjacent)
        print(path)
        while path:
            vt = path.popleft()
            if visited.get(vt):
                continue
            print('visited', vt)
            visited[vt] = True
            if vt == v:
                return True
            else:
                for adjacent in self.vertices[vt]['out']:
                    path.append(adjacent)

        return False


    def dfs(self, s):
        path = deque()
        for edge in self.vertices[s]['out']:
            path.append(edge)
        visited = {}
        visited[s] = True
        while path:
            k = path.popleft()
            if visited[k]:
                continue


    def cycle_exists(self):
        for v,edges in self.vertices.items():
            path = list()
            outlist = edges['out']
            print(outlist)





def main():
    graph = Graph()
    for i in range(4):
        graph.insert_vertex(i)

    graph.insert_edge(0,1)
    graph.insert_edge(0,2)
    graph.insert_edge(2,0)
    graph.insert_edge(1,2)
    graph.insert_edge(2,3)

    graph.display()
    #print(graph.path_exists(0, 3))
    graph.cycle_exists()

if __name__=='__main__':
    main()
