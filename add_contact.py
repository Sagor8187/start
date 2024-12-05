import os
import csv
def add_contact():
    try:
        name =input("Enter contact Name here : ")
        if not name.isalpha():
            raise ValueError("name added for use only allphabet ")
        
        number=input("Enter contact number here :")
        if not number.isdigit():
            raise ValueError("number added use only number ")
        
        email=input("Enter your contact email :")
        address=input("Enter your contact address :")
        
        if not os.path.exists("contacts.csv"):
            with open("contacts.csv","w") as file:
                file.write("")
                
        with open("contacts.csv","r") as file:
            contacts=file.readlines()
            for contact in contacts:
                if f"number :{number}" in contact:
                    print("this number all_ready added ")
                    return
            
        with open ("contacts.csv","a") as file:
            file.write(f"name :{name}\nnumber :{number}\nEmail :{email}\nAddress :{address}\n\n")
            
        print("contact added succcssful")
        
    except ValueError as e:
        print("input wrong ")
        
        add_contact()