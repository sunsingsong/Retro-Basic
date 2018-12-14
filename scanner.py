import string

# ******************** scanner ***********************

tokens = []

file = open("input.txt")
for line in file:
    i=0
    tmp = line.strip().split()
    while(i<len(tmp)):
        if(tmp[i].isdigit() and int(tmp[i])<100):
            tokens+=[["num<100",int(tmp[i])]]
        elif(tmp[i].isdigit() and int(tmp[i])<1000):
            tokens+=[["num<1000",int(tmp[i])]]
        elif(tmp[i] in string.ascii_uppercase and len(tmp[i]) == 1):
            tokens+=[["id",ord(tmp[i]) - ord('A') + 1]]
        elif(tmp[i]=="IF"):
            tokens+=[["if",0]]
        elif(tmp[i]=="GOTO"):
            tokens+=[["goto",int(tmp[i+1])]]
            i+=1
        elif(tmp[i]=="PRINT"):
            tokens+=[["print",0]]
        elif(tmp[i]=="STOP"):
            tokens+=[["stop",0]]
        elif(tmp[i]=="+"):
            tokens+=[["op",1]]
        elif(tmp[i]=="-"):
            tokens+=[["op",2]]
        elif(tmp[i]=="<"):
            tokens+=[["op",3]]
        elif(tmp[i]=="="):
            tokens+=[["op",4]]
        else:
            print("ERROR")
            exit(0)
        i+=1

for i in range(0,len(tokens)):
    if(tokens[i][0]=="if"):
        tokens[i+4][0]="goto"

tokens.append("EOF")

# ******************** parser ***********************

parsing_table = {}
terminal=[]
nonterminal={'line':10,'id':11,'const':12,'if':13,'goto':14,'print':15,'stop':16,'op':17}

stack = []
stack.append("EOF")
stack.append("pgm")

point=0
output=[]

while(1):
    top=stack[len(stack)-1]
    if(tokens[point][0]==top):
        
            
            


