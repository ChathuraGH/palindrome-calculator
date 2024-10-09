import re
u=int(input("start point of range :- "))
uu=int(input("end point of range :- "))
a=[]
uu=uu+1

def num(u,uu):
    for i in range(u,uu):
        a.append(u)
        u+=1
    #print(a)


def p():
    for e in a:
        x=e
        xx=str(x)
        xxx=len(xx)
        if xxx==2 or xxx==3:
            b=[]
            for c in xx:
                b.append(c)
                
            if b[0] == b[xxx-1]:
                print(e,"yes")
            else:
                pass
                
        elif xxx==4 or xxx==5:
            b=[]
            for c in xx:
                b.append(c)
            
            if b[0] == b[xxx-1] and b[1] == b[xxx-2]:
                print(e,"yes")
            else:
                pass
        elif xxx==6 or xxx==7:
            b=[]
            for c in xx:
                b.append(c)
            
            if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3]:
                print(e,"yes")
            else:
                pass
        elif xxx==8 or xxx==9:
            b=[]
            for c in xx:
                b.append(c)
            
            if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3] and b[3] == b[xxx-4]:
                print(e,"yes")
            else:
                pass
        elif xxx==10 or xxx==11:
            b=[]
            for c in xx:
                b.append(c)
            
            if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3] and b[3] == b[xxx-4] and b[4] == b[xxx-5]:
                print(e,"yes")
            else:
                pass
        else:
            #print(e,"is s")
            pass
            
def e():
    a=input('"press Enter to exit"')
    exit
    
num(u,uu)
p()

e()

























