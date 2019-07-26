dict = {}
def add(p_id,name):
    dict[p_id] = name
def display():
    if len(dict) == 0:
        print("dictinary is empty")
    else:
        for k,v in dict.items():
            print(f"{k}:{v}")
def search(p_id):
    if len(dict) == 0:
        print("dictinary is empty")
    else:
        for k in dict:
            if k == p_id:
                print(f"element found",dict[k])
            else:
                print("element not found")


while True:
    print("1 add 2 display 3 search")
    ch = int(input("enter your choice"))
    if ch == 1:
        p_id = int(input("enter product id"))
        name = input("enter product name")
        add(p_id,name)
    elif ch == 2:
        display()
    elif ch == 3:
        p_id = int(input("enter the product to be searched"))
        search(p_id)
    else:
        exit(0)
    