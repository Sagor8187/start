def view_contact():
    try:
        with open("contacts.csv","r") as file:
            contacts=file.read()
            if contacts.strip()=="":
                print("contact not found ")
                    
            else:
                print("contact \n")
                print(contacts)
                
    except FileNotFoundError:
        print("contact not found ")
            