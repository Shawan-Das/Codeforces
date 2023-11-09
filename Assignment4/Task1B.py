input_text= 'input1B_3.txt' # file location
output_text= 'out'+input_text[2:] # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r')

n,m=(text.readline().split(" "))
adjMatrix={}
for i in range(int(n)+1):
    adjMatrix[str(i)]=""


for i in range(int(m)):
    u,v,w= (text.readline().replace("\n", "").split(" "))  #remove new line tag
    adjMatrix[u] += "("+v+","+w+")" + " "
text.close()
string=""

for k,v in adjMatrix.items():
    if v:
        string += k + " : " + v + "\n"
    else:
        string += k + " : "+'\n'

output.write(string)
output.close()