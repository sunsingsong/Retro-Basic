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
            tokens+=[["+",1]]
        elif(tmp[i]=="-"):
            tokens+=[["-",2]]
        elif(tmp[i]=="<"):
            tokens+=[["<",3]]
        elif(tmp[i]=="="):
            tokens+=[["=",4]]
        else:
            print("ERROR")
            exit(0)
        i+=1

file.close()

for i in range(0,len(tokens)):
    if(tokens[i][0]=="if"):
        tokens[i+4][0]="goto"

tokens.append(["EOF"])

# ******************** parser ***********************

parsing_table = {("pgm","line_num"):["line","pgm"],("pgm","EOF"):["EOF"],("line","line_num"):["line_num","stmt"],\
                 ("stmt","id"):["asgmnt"],("stmt","IF"):["if"],("stmt","PRINT"):["print"],("stmt","GOTO"):["goto"],\
                 ("stmt","STOP"):["stop"],("asgmnt","id"):["id","=","exp"],("exp","id"):["term","exp'"],("exp","const"):["term","exp'"],\
                 ("exp'","+"):["+","term"],("exp'","-"):["-","term"],("exp'","line_num"):"empty",("exp'","EOF"):"empty",\
                 ("term","id"):["id"],("term","const"):["const"],("if","IF"):["IF","cond","line_num"],("cond","id"):["term","cond'"],\
                 ("cond","const"):["term","cond'"],("cond'","<"):["<","term"],("cond'","="):["=","term"],("print","PRINT"):["PRINT","id"],\
                 ("goto","GOTO"):["GOTO"],("stop","STOP"):["STOP"]}

#terminal=['line_num','id','const','IF','GOTO','PRINT','STOP','+','-','<','=']
nonterminal=['pgm','line','stmt','asgmnt','exp','term','if','cond','print','goto','stop',"exp'","cond'"]
terminal={'line_num':10,'id':11,'const':12,'IF':13,'GOTO':14,'PRINT':15,'STOP':16,'+':17,'-':17,'<':17,'=':17}

stack = []
stack.append("pgm")
point=0
output=[]
while(1):
    top=stack[len(stack)-1]
    if(top in terminal):
        if(tokens[point][0]==top):
            output.append(stack.pop())
            output.append(tokens[point][1])
            point+=1
        elif(top=="line_num" and tokens[point][0]=="goto"):
            stack.pop()
            output.append("GOTO")
            output.append(tokens[point][1])
            point+=1
        elif(top=="line_num" and tokens[point][0] in ["num<100","num<1000"]):
            tokens[point][0]="line_num"
        elif(top=="const" and tokens[point][0] == "num<100"):
            tokens[point][0]="const"
    elif(top in nonterminal):
        if(top in ["exp","term","cond"] and tokens[point][0]=="num<100"):
            tokens[point][0]="const"
        elif(top in ["pgm","line","exp'"] and tokens[point][0] in ["num<100","num<1000"]):
            tokens[point][0]="line_num"
        elif(tokens[point][0]=="if"):
            tokens[point][0]="IF"
        elif(tokens[point][0]=="print"):
            tokens[point][0]="PRINT"
        elif(tokens[point][0]=="goto"):
            tokens[point][0]="GOTO"
        elif(tokens[point][0]=="stop"):
            tokens[point][0]="STOP"
        key=(top,tokens[point][0])
        if(key in parsing_table):
            if(parsing_table[key]=="empty"):
                stack.pop()
            else:
                stack.pop()
                for i in range(len(parsing_table[key])-1,-1,-1):
                    stack.append(parsing_table[key][i])
        else:
            output="ERROR"
            break
    elif(top=="EOF"):
        print("ACCEPT")
        break
    else:
        output="ERROR"
        break

# ******************* B-code **************************

for i in range(0,len(output),1):
    if(output[i] in terminal):
        output[i]=terminal[output[i]]
output.append(0)

file = open("output.txt","w")
file.write(" ".join([str(e) for e in output]))

file.close()
        
        
            
            


