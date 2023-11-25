from collections import defaultdict, deque
def is_cyclic_util(v, visited, rec_stack, graph):
    visited[v] = True
    rec_stack[v] = True

    for neighbor in graph.get(v, []):
        if not visited[neighbor]:
            if is_cyclic_util(neighbor, visited, rec_stack, graph):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[v] = False
    return False

def is_cyclic(graph):
    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    for node in graph:
        if not visited[node]:
            if is_cyclic_util(node, visited, rec_stack, graph):
                return True
    return False

def topological_sort_bfs(n, graph):

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


input_text= 'input1B_3.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')


n,m=map(int,(text.readline().split(" ")))
#print(n,m)
in_degree = [0] * (n + 1)
graph={}
for i in range(1,int(n)+1):
    graph[i]=[]
    
for i in range(int(m)):
    u,v= (text.readline().replace("\n", "").split(" "))  #remove new line tag
    graph[int(u)].append(int(v))
    in_degree[int(v)] += 1
text.close()
#print(graph)
if is_cyclic(graph):
    output.write("IMPOSSIBLE")
else:
    result_bfs = topological_sort_bfs(n, graph)
    string= ""
    for r in result_bfs:
        string += str(r) + " "
    output.write(string)
output.close()

