num = int(input("enter a number")) 
s = 0 
temp=num


while num > 0:    
  r = num % 10    
  s=s+r           
  if num > 9:
      s=s*10
      
  num=num // 10 
   

if s==temp:
    print(s," is a palindrom")
else:
    print(s," is not a palindrom")
