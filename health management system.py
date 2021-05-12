print("This is a health chart of Kajal ,Priya,Riya")
print("Choose Among the following to write about any of the persons health condition ")
print("1.Food chart of Kajal")
print("2.Food chart of Priya")
print("3.Food chart of Riya")
print("4.Exercise of Kajal")
print("5.Exercise of Priya")
print("6.Exercise of Riya")
print("7.To view the total contents of this health log")

def getdata():
    import datetime
    return datetime.datetime.now()

def chart():
    if  b == 1:
        f1 = open("data1.txt", "a")
        k = input("Write about food chart of Kajal")
        f1.write("Kajal Diet Chart"+str([str(getdata())])+":"+k+"\n")

    elif  b==2:
        f2 = open("data2.txt", "a")
        l = input("Write about food chart of Priya")
        f2.write("Priya's Diet Chart" +str([str(getdata())])+":"+l+"\n")

    elif  b == 3:
        f3 = open("data3.txt", "a")
        m = input("Write about food chart of Riya")
        f3.write("Riya's Diet Chart"+str([str(getdata())])+":"+m+"\n")

    elif b == 4:
        f4 = open("exe1.txt", "a")
        n = input("Write about exercise chart of Kajal")
        f4.write("Kajal's Exercise"+str([str(getdata())])+":"+n+"\n")
    elif b == 5:
        f5 = open("exe2.txt", "a")
        o = input("Write about exercise chart of Priya")
        f5.write("Priya's Exercise"+str([str(getdata())])+":"+o+"\n")

    elif b == 6:
        f6 = open("exe3.txt", "a")
        p = input("Write about exercise chart of Riya")
        f6.write( "Riya's Exercise"+str([str(getdata())])+":"+p+"\n")

    elif b==7:
        f1=open("data1.txt","rt")
        f2=open("data2.txt","rt")
        f3=open("data3.txt","rt")
        f4=open("exe1.txt","rt")
        f5=open("exe2.txt","rt")
        f6=open("exe3.txt","rt")
        q=f1.read()
        w=f2.read()
        e=f3.read()
        r=f4.read()
        t=f5.read()
        y=f6.read()
        print(q)
        print(w)
        print(e)
        print(r)
        print(t)
        print(y)
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()


    else:
        print ("invalid sintax")
while True:
    b=int(input("Enter ur choice"))
    chart()
    getdata()









