# fnction to add two nmbrs
def add(x,y):
        return(x+y)
    
# fnction to sbtract two nmbers
def sbb(x,y):
           return(x-y)
       
#fnction to mtiply two nbers
def mtiply(x,y):
    return (x*y)
#fnction to divide two mbers
def divide(x,y):
    if y==0:
        return("error in process")
    else:
    
        return(x/y)
# main loop for calc
while True:
 print("select operation")
 print("1.add")
 print("2.sbb")
 print("3.mtiply")
 print("4.divide")
 print("5.exit")
 choice=input("enter choice(1/2/3/4/5):")
 if choice=="5":
    print("exiting, goodbye")
    break
 if choice in ("1","2","3","4"):
   no1 = float(input("enter first no:"))
   no2=float(input("enter second no"))

   if choice =="1":
    print(f"={add(no1,no2)}")
   elif choice=="2":
    print(f"={sbb(no1,no2)}")
   elif choice=="3":
    print(f"={mtiply(no1,no2)}")
   elif choice=="4":
    print(f"={divide(no1,no2)}")
else:
    print("invalid inpt ")
    
    
    
    