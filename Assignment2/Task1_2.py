input_text= 'input1.txt' # file location
output_text= 'output1.txt' # output will be saved on this location
output = open(output_text, 'w')
text =open(input_text, 'r') # 'r' used to read file data
n,total= map(int,(text.readline().split(" "))) # number of.split(" ")

data= list(map(int,text.readline().split(" "))) # store the number in list and integer format

text.close()

left,right= 0, n-1
a,b=None,None

while(left<right):
    if data[left]+data[right]== total:
        a,b=left+1,right+1
        break
    elif(data[left]+data[right]<total): left += 1
    else: right -=1

if a is not None and b is not None: output.write(str(a)+ " "+str(b))
else: output.write("IMPOSSIBLE")

output.close()