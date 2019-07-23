data = "raj,siva,Mani,sonu,Anu,Tanvi"
print(list(filter(lambda x:x.startswith("A"),list(map(lambda x:x.capitalize(),data.split(","))))))