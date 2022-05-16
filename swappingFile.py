def swapFileData():

    file1=input("Enter name of your file :-")
    file2 = input("enter name of your file again :-")

    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2,'r') as a:
        data_b = a.read()

    with open(file1,'w') as a:
         a.write(data_b)
       
    with open(file2,'w') as a:
         a.write(data_a)

swapFileData()