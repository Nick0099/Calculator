rep = "Y"
while(rep.upper() == "Y"):
  try:
    n= int(input("enter a number: "))
    m= int(input("enter second number: "))
    a = input("operation({A}dd,{S}ub,{M}ul,{D}iv): ")
    o=a.upper()
    if o=="A":
       print("the output of ", n , " added to", m 
    ," is = " , n + m)
    elif o=="S":
      print("the output of ", n , " subtracted by", m 
    ," is = " , n- m)
    elif o=="M":
      print("the output of ", n , " multiplied by", m 
    ," is = " ,  n * m)
    if o=="D" and n==0:
      print("cannot divide by 0")
    elif o =="D" and n !=0 :
      print("the output of ", n , " divided by", m 
    ," is = " , n/m)
  except:
    print("invalid input")
  rep=  input("do you want to continue(y/n): ")
  
  


