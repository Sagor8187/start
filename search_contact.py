def search_contact():
    number=input("Enter phone for search :")
    try:
        with open("contacts.csv","r") as file:
            contacts=file.read()
            if number in contacts:
                lst=contacts.split("\n\n")
                for contact in lst:
                    if f"{number}" in contact:
                        print(contact)
                        return
                print("contact not found")
            else:
                print("no contact found ") 
                
    except FileNotFoundError:
        print("file not found ")   