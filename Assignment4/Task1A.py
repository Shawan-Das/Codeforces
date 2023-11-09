input_text= 'input1A_2.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')

n,m= map(int,(text.readline().split(" ")))
data=[]  # store Vertex and Edge 
matrix = [[0] * (n+1) for _ in range(n+1)]  # Graph Matrix Form
for i in range(m):
    u,v,w=map(int,(text.readline().split(" ")))
    matrix[u][v]=w
text.close()    # close the file
store =""
for d in matrix:
    for i in d:
        store += str(i)+" "   
    store += "\n"
output.write(store)
output.close() # close the