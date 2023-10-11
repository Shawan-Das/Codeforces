def sort_by_start_time(m,data):
        person_assigned=[-1]*m
        selected_task=[]
        sorted_time= sorted(data, key=lambda x: x[0])

        for time in sorted_time:
            start_time,end_time= time
            
            for i in range(m):
                if(start_time >= person_assigned[i]):
                    selected_task.append(time)
                    person_assigned[i]=end_time
                    break
        return len(selected_task)
    
def sort_by_end_time(m,data):
    person_assigned=[-1]*m
    selected_task=[]
    sorted_time= sorted(data, key=lambda x: x[1])

    for time in sorted_time:
        start_time,end_time= time
        
        for i in range(m):
            if(start_time >= person_assigned[i]):
                selected_task.append(time)
                person_assigned[i]=end_time
                break
    return len(selected_task)


input_text="input4.txt"
output_text="output4.txt"
output= open(output_text,"w")
text= open(input_text,'r')

n,m = map(int, text.readline().split(" "))
data=[]
for i in range(n):
    a,b = map(int, text.readline().split()) # store the data as list of tuple where start/end time are in tuple format
    data.append((a,b))
text.close()

l1= sort_by_end_time(m,data)
l2= sort_by_start_time(m,data)

output.write(str(max(l1,l2)))
output.close()    