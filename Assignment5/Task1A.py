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
def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def topological_sort_dfs(n, graph):

    visited = [False] * (n + 1)
    stack = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    stack.reverse()  # Reverse the order of elements in the stack

    return stack


input_text= 'input1A_3.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')


n,m=map(int,(text.readline().split(" ")))
#print(n,m)

graph={}
for i in range(1,int(n)+1):
    graph[i]=[]
    
for i in range(int(m)):
    u,v= (text.readline().replace("\n", "").split(" "))  #remove new line tag
    graph[int(u)].append(int(v))
text.close()
#print(graph)
if is_cyclic(graph):
    output.write("IMPOSSIBLE")
else:
    result_dfs = topological_sort_dfs(n, graph)
    string= ""
    for r in result_dfs:
        string += str(r) + " "
    output.write(string)
output.close()

