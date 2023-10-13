input_text= 'input1.txt' # file location
output_text= 'output1.txt' # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r') # 'r' used to read file data
n,total= map(int,(text.readline().split(" "))) # number of.split(" ")

data= list(map(int,text.readline().split(" "))) # store the number in list and integer format

text.close()

flag=True ## initially assign null into a and b

for i in range(n):
    for j in range(i+1,n):
        if(data[i]+data[j]==total):
            a,b = i+1, j+1
            flag=False
            break;
    if flag==False: break;

if flag==False: output.write(str(a)+ " "+str(b))
else: output.write("IMPOSSIBLE")
output.close()
