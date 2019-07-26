lst = ['story','emergency','qualify']
for ch in lst:
    str = ch.replace(ch[-1],'ies')
    print(f"{ch} -- {str}")