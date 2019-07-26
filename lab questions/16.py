while True:
    inp = input("enter a statement")
    if inp == 'done':
        break
    if inp[-1] == '?':
        print(f"{inp} isinterogative statement")
    else:
        print("assertive statements")