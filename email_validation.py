email = input("Enter your Email: ") #a@g.com
k,j,d  = 0,0,0
if len(email) >= 7: # checkihng whether min length of stadard email satisfy or not 
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."): #iska matlab hai .com ya .in ^ means dono me se ke true
                for i in email: #using for loop to check each letter of string(email)
                    if i == i.isspace():
                        k = 1
                    elif i == i.upper():
                        j = 1
                    elif i == i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1    
                if k == 1 or j == 1 or d == 1: # coming putside of loop
                    print("Wrong Email 5")        
            else:
                print("Wrong Email 4 ")
        else:
            print("wrong Email 3")
    else: 
        print("Wrong Email 2")
else:
    print("Wrong Email 1 : Email is totally wrong")
    