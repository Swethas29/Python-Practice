def check_pin(entered_pin):
    correct_pin = 1234

    if entered_pin == correct_pin:
        return True
    else:
        return False
        
def bank_action(action_type, entered_pin):
    result = check_pin(entered_pin)
    if result == True:
        if action_type == "balance":
            print("Your account balance is Rs. 10,000")
        elif action_type == "withdraw":
            print("Withdrawal successful!")
        else:
            print("Invalid action")
    else:
        print("Incorrect PIN, access denied.")
pin = int(input("Enter your PIN: "))
action = input("Enter action (balance/withdraw): ")
bank_action(action, pin)
