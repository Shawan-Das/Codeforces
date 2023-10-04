## function used for number check
def number(n):
    if(n%2==0): return str(n)+" is an Even number. \n"
    else: return str(n)+" is an Odd number. \n"

#import data from text file
input_text= 'Task1\input1a.txt' # file location
output_text= 'Task1\output1a.txt' # output will be saved on this location
text =open(input_text, 'r') # 'r' used to read file data
text= text.read()

data=list(map(int,text.split('\n'))) # convert the numbers into a list

new_text=""

for n in data:
    new_text+= number(n)

## write the output in output1a.txt
output = open(output_text, 'w')
output.write(new_text)