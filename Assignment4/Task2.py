input_text= 'input2_4.txt' # file location
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
visited = [] # List for visited nodes.
queue = []     #Initialize a queue


def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)
  string = ""
  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    string += str(m)+ " " 
    #print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return string  
# Driver Code
output.write(bfs(visited, graph, 1))    # function calling

