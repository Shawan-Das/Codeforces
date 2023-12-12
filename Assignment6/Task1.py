import heapq

def dijkstra(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

input_text= 'input1.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')

n,m=map(int,(text.readline().split(" ")))
#print(n,m)

graph={}
for i in range(1,int(n)+1):
    graph[str(i)]={}

for i in range(int(m)):
    u,v,w= (text.readline().replace("\n", "").split(" "))
    graph[u][v]= int(w)

source_node= text.readline().replace("\n", "")

result = dijkstra(graph, source_node)

string = ""
# Print the shortest distances from the source node to all other nodes
for node, distance in result.items():
    string += str(distance if distance != float('infinity') else -1) + " "
    
output.write(string)
output.close()
