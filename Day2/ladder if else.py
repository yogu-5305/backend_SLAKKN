Ticket = int(input("enter the ticket no:"))
if Ticket >=1 and Ticket <=30:
    print("Balcony")
elif Ticket >31 and Ticket <=70:
    print("Back 4 Lines")
elif Ticket >71 and Ticket <=100:
    print("Front 3 Lines")
else:
    print("Invalid")
          
