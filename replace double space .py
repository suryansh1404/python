ystring = input("Please, Enter A String -> ")

mystring = mystring.strip()

while '  ' in mystring:
      mystring = mystring.replace('  ', ' ')
     print("After Replacing Double Space With Single Space : ")
    print("\t{}".format(mystring))
