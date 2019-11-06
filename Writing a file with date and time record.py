import datetime
def gettime():
    return datetime.datetime.now()
t=gettime()
def take():
   value=input("Type here....")
   with open("pankaj.txt","a") as op:
      op.write(str(t))
      op.write(value+"\n")
                
      print("Written Successfully")
take()
print(gettime())
input()
