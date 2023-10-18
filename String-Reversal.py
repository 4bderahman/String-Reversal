txt = input("Enter a string: ")

txtlist = list(txt)

txtlist.reverse()

newlist = ''.join(txtlist)

print("Reversed String:", newlist)
