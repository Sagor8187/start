def remove_contact():
    number=input("Enter number for remove ")
    
    try:
        with open("contacts.csv","r") as file:
            contacts= file.read()
            contact_list=contacts.strip().split("\n\n")
            new_contact= []
            contact_found=False
            
            
            for contact in contact_list:
                if f"{number}" in contact:
                    contact_found = True
                    
                else:
                    new_contact.append(contact)
                    
                    
            if contact_found:
                with open ("contacts.csv","w") as file:
                    file.write("\n\n".join(new_contact) +"\n\n" if new_contact else "")
                print("contact remove successfull")
                
            else:
                print("contact not found ")
                
    except FileNotFoundError:
        print("file not found ")