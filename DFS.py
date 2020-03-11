graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                print (path + [next])

list(dfs_paths(graph, 'A', 'F')) #retorna los caminos que toma
#ejemplo de A a F primero va por A y C, llega a F
#Segundo va por A,B y E y llega a F
#se imprime las rutas que va tomando


