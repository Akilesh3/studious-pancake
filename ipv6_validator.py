x = input("Enter the given address ")
flag = 0
caps = "ABCDEF"
lower = caps.lower()
num = "1234567890"
characters = caps+lower+num
splited = x.split(":")
if (len(splited) == 8):
    for i in splited:   
        if (len(i)==4):
            for j in i:
                if j in characters :
                    flag = 1
                else:
                    flag = 0
                if flag == 0:
                    print("Its not a valid IPV6 address.")
                    break
                else:
                    continue
        else:
            print("Its not a valid IPV6 address.")       
else:
    print("Its not a valid IPV6 address.")
                    


