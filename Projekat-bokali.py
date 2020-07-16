from array import *

bokali=array('i',[])

n=int(input("Unesite broj bokala: "))

for i in range(n):
    x=int(input("Unesite zapreminu bokala u litrima: "))
    bokali.append(x)


print(bokali)

trazeni=int(input("Unesite zapreminu u litrima koju zelite da dobijete: "))

#provera da li je trazena zapremina vec u datim bokalima
k=0
for e in bokali:
    if e==trazeni:
        print("Trazena zapremina je vec u "+ str(k+1) +". bokalu")
        break
    k+=1

#gcd-najveci zajednicki delilac
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)


def Presipanje(niz ,goal):
    for i in range(0,len(niz)):
        for j in range(i+1,len(niz)):
            if((goal<niz[i] or goal<niz[j]) and (goal%gcd(niz[i],niz[j])==0)):
               fromJugCap=niz[j]
               toJugCap=niz[i]

               fromJug=fromJugCap
               toJug=0

               while((fromJug is not goal)and(toJug is not goal)):
                   print("koristimo "+str(fromJugCap)+"-litarski bokal(iz njega sipamo) i "+str(toJugCap)+"-litarski bokal(u njega sipamo")

                   temp=min(fromJug,toJugCap-toJug)

                   toJug=toJug+temp
                   fromJug=fromJug-temp
                   print(str(fromJugCap)+': '+str(fromJug)+' '+str(toJugCap)+': '+str(toJug))
                   
                   if((fromJug==goal)or(toJug==goal)):
                       print("Dobili smo trazenu kolicinu u bokalu sa zapreminom: \n")
                       if(fromJug==goal):print(str(fromJugCap))
                       else:print(str(toJugCap))
                       break

                   if fromJug==0:
                        fromJug=fromJugCap
                        print(str(fromJugCap)+" : "+str(fromJug)+" "+str(toJugCap)+" :"+str(toJug))
                       



                   if toJug==toJugCap:
                        toJug=0
                        print(str(fromJugCap)+" : "+str(fromJug)+" "+str(toJugCap)+" :"+str(toJug))
                        



               if(fromJug==goal):return(fromJugCap)
               else:return (toJugCap)

            else: print("nije moguce")








Presipanje(bokali,trazeni)
                        
                        
                        
                        
                       
            
