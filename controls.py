#Universal Yes/No user input function
def decisionCheck(yesInput: str, noInput: str): 
    decision = input(">> ")
    if decision == yesInput:
        return True
    elif decision == noInput:
        return False
    else:
        print(f"{decision} is not a valid key")
        print(f"The Valid Keys are [{yesInput}/{noInput}]")
        return decisionCheck(yesInput,noInput)