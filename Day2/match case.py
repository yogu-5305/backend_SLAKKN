Food = (input("Enter the Food name:"))

match Food:
    case "Chicken biryani":
        print("Rs:200")
    case "Mutton biryani":
        print("Rs: 250")
    case "Chicken Rise":
        print("Rs: 180")
    case "Parotta":
        print("Rs: 100")
    case _:
        print("Not Available")
