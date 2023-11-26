def dfs(graph, node, visited, stack):
    visited[node] = True
    if node in graph:
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited, stack)
    stack.append(node)

def fill_order(graph, node, visited, order):
    visited[node] = True
    if node in graph:
        for neighbor in graph[node]:
            if not visited[neighbor]:
                fill_order(graph, neighbor, visited, order)
    order.append(node)

def get_transposed_graph(graph):
    transposed = {}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in transposed:
                transposed[neighbor] = []
            transposed[neighbor].append(node)
    return transposed

def strongly_connected_graph(graph, vertices):
    visited = {node: False for node in range(1, vertices + 1)}
    order = []
    stack = []

    for node in range(1, vertices + 1):
        if not visited[node]:
            fill_order(graph, node, visited, order)

    transposed = get_transposed_graph(graph)

    visited = {node: False for node in range(1, vertices + 1)}

    while order:
        node = order.pop()
        if not visited[node]:
            component = []
            dfs(transposed, node, visited, component)
            stack.append(component)

    return stack

input_text= 'input3_3.txt' # file location
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

scc = strongly_connected_graph(graph, n)

for index in range(len(scc)):
    scc[index]=[scc[index][-1]]+scc[index][:-1]
scc.sort()

scc_string = "\n".join(" ".join(map(str, component)) for component in scc)
output.write(scc_string)
output.close()

