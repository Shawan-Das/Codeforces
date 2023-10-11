input_text="input3.txt"
output_text="output3.txt"
output= open(output_text,"w")
text= open(input_text,'r')

n= int(text.readline()) #total number of times
data=[]
selected_times=[]
for i in range(n):
    a,b = map(int, text.readline().split()) # store the data as list of tuple where start/end time are in tuple format
    data.append((a,b))
text.close()

#sort the data at the basis of end time which is in index-1 of each tuple
sorted_time= sorted(data, key=lambda x: x[1])

last_end_time= -1

for time in sorted_time:
    start_time, end_time = time
    if start_time >= last_end_time:
        selected_times.append(time)
        last_end_time = end_time

output_text= str(len(selected_times))+"\n"

for time in selected_times:
    output_text+= str(time[0])+" "+str(time[1])+"\n"
    
output.write(output_text)
output.close()

