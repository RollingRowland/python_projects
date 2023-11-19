"""
Breadth first search function. Returns all paths to your desired location.
The first path in the list is the shortest in terms of vertices visited.
"""

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  paths = []
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor == target_value:
          paths.append(path + [neighbor])
        else:
          bfs_queue.append([neighbor, path + [neighbor]])
  return paths

      
