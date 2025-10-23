phone_number = input("Enter a phone number: ")

if phone_number.isdigit() and len(phone_number) == 10:
    print("This is a valid phone number.")
else:
    print("Invalid phone number. It must contain exactly 10 digits and no other characters.")
