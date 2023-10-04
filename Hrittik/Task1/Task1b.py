def calculate(n1,op,n2):
    if '.' in n1: n1= float(n1)
    else: n1= int(n1)
    
    if '.' in n2: n2= float(n2)
    else: n2= int(n2)
    
    
    if(op=='+'): value= n1+n2
    if(op=='-'): value= n1-n2
    if(op=='*'): value= n1*n2
    if(op=='/'): value= n1/n2
    
    return f"The result of {n1} {op} {n2} is {value} \n"

input_text= 'Task1\input1b.txt' # file location
output_text= 'Task1\output1b.txt' # output will be saved on this location
text =open(input_text, 'r') # 'r' used to read file data
text= text.read()
new_text= ""
text= text.replace('calculate ','') 

temp_data= text.split('\n')[1:]

for d in temp_data:
    n1,op,n2=d.split(" ")
    new_text+= calculate(n1,op,n2)
    
output = open(output_text, 'w')
output.write(new_text)