input_text= 'input3_4.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')

n,m=map(int,(text.readline().split(" ")))

graph ={}
for i in range(n):
    graph[i+1]=[]
    
for i in range(m):
    s,e=map(int,(text.readline().replace("\n", "").split(" ")))
    graph[s].append(e)
text.close()
path=[]
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        path.append(str(node))
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
# Driver Code
dfs(visited, graph, 1)

string=""
for n in path:
    string += n + " "
output.write(string)
output.close()
#output.write(string)    # function calling

