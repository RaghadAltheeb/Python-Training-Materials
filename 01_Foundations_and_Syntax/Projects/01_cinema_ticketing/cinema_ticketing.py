tickets =5
cinema =True 

while cinema == True:
    name =input("Enter your name: ")
    num_tickets = int(input("Enter the number of tickets you want to book: "))
    
    if 0 < num_tickets <= tickets:
        print(f"Success! {name} bought {num_tickets} tickets.")
        tickets -= num_tickets
    elif num_tickets > tickets:
        print(f"Sorry {name}, only {tickets} tickets are available.") 
    else:
        print("Invalid number of tickets. Please enter a positive number.")
        
    if tickets == 0:
        print("All tickets are sold out.")
        cinema = False 
        break
