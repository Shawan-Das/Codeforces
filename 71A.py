testCase= int(input())

for t in range(testCase):
    text= input()
    
    if(len(text)<=10): print(text)
    else: print(text[0]+str(len(text[1:-1]))+text[-1])