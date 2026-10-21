Playlist = input("Enter the singer name (Anirudh/Sid Sriram/Sai Abhyankkar/G.V.Prakash):    ")
                 
match Playlist:

        case "Anirudh":
                 print("Monica,Hukum,Arabic Kuthu,Raavana Mavandaa")

        case "Sid Sriram":
                 print("Thalli Pogathey, Maruvaarthai, Kannaana Kanney, Nee Singam Dhan,")

        case "Sai Abhyankkar":
                 print("Katchi Sera, Aasa Kooda, Pavazha Malli, Radhimaa, Vizhi Veekura")

        case "G.V.Prakash":
                 print("Ayyayo, Pookkal Pookkum, Yaar Indha Saalai Oram, Vaa Vaathi")

        case _:
                 print("Invalid Playlist")
                 
