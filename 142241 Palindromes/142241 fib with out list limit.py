u=int(input("start point of range :- "))
uu=int(input("end point of range :- "))

uu=uu+1

def num(u,uu):
    for i in range(u,uu):
        try:
            x=u
            xx=str(x)
            xxx=len(xx)
            if xxx==2 or xxx==3:
                b=[]
                for c in xx:
                    b.append(c)
                    
                if b[0] == b[xxx-1]:
                    print(u,"yes")
                else:
                    pass
                    
            elif xxx==4 or xxx==5:
                b=[]
                for c in xx:
                    b.append(c)
                
                if b[0] == b[xxx-1] and b[1] == b[xxx-2]:
                    print(u,"yes")
                else:
                    pass
            elif xxx==6 or xxx==7:
                b=[]
                for c in xx:
                    b.append(c)
                
                if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3]:
                    print(u,"yes")
                else:
                    pass
            elif xxx==8 or xxx==9:
                b=[]
                for c in xx:
                    b.append(c)
                
                if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3] and b[3] == b[xxx-4]:
                    print(u,"yes")
                else:
                    pass
            elif xxx==10 or xxx==11:
                b=[]
                for c in xx:
                    b.append(c)
                
                if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3] and b[3] == b[xxx-4] and b[4] == b[xxx-5]:
                    print(u,"yes")
                else:
                    pass

            elif xxx==12 or xxx==13:
                b=[]
                for c in xx:
                    b.append(c)
                
                if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3] and b[3] == b[xxx-4] and b[4] == b[xxx-5] and b[5] == b[xxx-6]:
                    print(u,"yes")
                else:
                    pass
            elif xxx==14 or xxx==15:
                b=[]
                for c in xx:
                    b.append(c)
                
                if b[0] == b[xxx-1] and b[1] == b[xxx-2] and b[2] == b[xxx-3] and b[3] == b[xxx-4] and b[4] == b[xxx-5] and b[5] == b[xxx-6] and b[6] == b[xxx-7]:
                    print(u,"yes")
                else:
                    pass     
            else:
                #print(e,"is s")
                pass
        except:
            print("exception occured")
            pass
        u+=1
            
def e():
    a=input('"press Enter to exit"')
    exit
    
num(u,uu)


e()

























