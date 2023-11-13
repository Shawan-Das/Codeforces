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

input_text= 'input4_5.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')

n,m=(text.readline().split(" "))
graph={}
for i in range(1,int(n)+1):
    graph[i]=[]


for i in range(int(m)):
    u,v= (text.readline().replace("\n", "").split(" "))  #remove new line tag
    graph[int(u)].append(int(v))
text.close()
#print(graph)

#graph = {1:[3,4], 2:[], 3:[2], 4:[]}

if is_cyclic(graph):
    output.write("Yes")
else:
    output.write("No")
output.close()