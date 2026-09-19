name= input("Enter your name: ")
age=int(input("Enter your age: "))
weight=float(input("Enter your weight ")) 
employment_status=input("Y/N")
is_pmy=(employment_status.strip().upper() == "Y")
BMI=(weight/(1.75**2))
print(f"the name {name} the age {age} the wight {BMI:.2f} emp {is_pmy}",sep="\n")


