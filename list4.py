list = []
def add(ele):
    list.append(ele)
def pop():
    if len(list) == 0:
        print("list id empty")
    else:
        ele = list.pop()
        print("element is ", ele)
def search(ele):
    if len(list) == 0:
        print("list id empty")
    else:
        if ele in list:
            index = list.index(ele)
            print(f"element {ele} found")
        else:
            print("not found")


def display():
    if len(list) == 0:
        print("list id empty")
    else:
        
        print(list)
    
while True:
    print("\n 1 for add 2 for pop 3 for search 4 for display 5 exit")
    ch = int(input("enter your choice"))
    if ch == 1:
        ele = int(input("enter the element"))
        add(ele)
    elif ch == 2:
        pop()

    elif ch == 3:
        ele = int(input("enter the element"))
        search(ele)
    elif ch == 4:
        display()
    else:
        print("thank you")
        break