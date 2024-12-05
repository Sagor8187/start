from add_contact import add_contact
from view_contact import view_contact
from remove_contact import remove_contact
from search_contact import search_contact
while True:
    print("Wellcome to contact management system ")
    print("0.exit")
    print("1.add contact")
    print("2.view contact")
    print("3.search contact")
    print("4.remove contact")
    
    operation=input("select operation : ")
    
    if operation == "0":
        print("Thanks for useing contact management system ")
        break
    
    elif operation == "1":
        add_contact()
        
    elif operation == "2":
        view_contact()
        
    elif operation == "3":
        search_contact()
         
    elif operation == "4":
        remove_contact()
        
    else:
        print(" invalid input please try_again ")