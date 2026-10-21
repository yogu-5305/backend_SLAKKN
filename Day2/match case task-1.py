print ("Furniture Menu")
print ("1. Sofa")
print ("2. Bed")
print ("3. Wardrobe")
print ("4. Table")

Furniture = (input("Enter the furniture name:"))
match Furniture:
    case "Sofa":
        print("You selected Sofa")
        print("Price: ₹5,000")

    case "Bed":
        print("You selected Bed")
        print("Price: ₹10,000")

    case "Wardrobe":
        print("You selected Wardrobe")
        print("Price: ₹15,000")

    case "Table":
        print("You selected Bed")
        print("Price: ₹20,000")

    case _:
        print("Invalid furniture choice")
