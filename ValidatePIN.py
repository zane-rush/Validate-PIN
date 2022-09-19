def validatepin():
    pin = input("Please enter PIN: ")
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            print("Your PIN is valid.")
        else:
            print("Your PIN must be 4 or 6 characters.")
    else:
        print("PIN must contain only numeric characters.")


validatepin()
