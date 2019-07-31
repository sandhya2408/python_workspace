class Queue:
    def __init__(self):
        self.st = []
    def push(self,ele):
        self.st.append(ele)
    def pop(self):
        if self.is_empty():
            print("stack empty")
        else:
            ele = self.st.pop(0)
            print("element removed is",ele)
    def search(self,searchEle):
        if self.is_empty():
            print("stack empty")
        else:
            for index, ele in enumerate(self.st):
                if ele == searchEle:
                    return index
            return -1

    def show(self):
        if self.is_empty():
            print("stack empty")
        else:
            print(self.st)
        
    def is_empty(self):
        return len(self.st) == 0
if __name__ == "__main__":
    st = Queue()
    while True:
        print("1.push 2.pop 3.search 4.show 5.exit")
        try:

            ch = int(input("enter your choice"))
            if ch == 1:
                ele = input("enter element to be pushed")
                st.push(ele)
            elif ch == 2:
                st.pop()
            elif ch == 3:

                ele = input("enter element to be search")
                res = st.search(ele)
                if res != 1:
                    print(f"element found at location :{res}")
                else:
                    print("element is not found")
            elif ch == 4:
                st.show()
            elif ch == 5:
                exit()
            else:
                raise ValueError()
        except ValueError:
            print("enter numbers only from 1 to 5")

        
         
            
        


