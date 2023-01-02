email = input("Enter your Email: ") #a@g.com
k,j,d  = 0,0,0
if len(email) >= 7: # checkihng whether min length of stadard email satisfy or not 
    if email[0].isalpha(): #checking the first letter of the email is alphabet or not
        if ("@" in email) and (email.count("@") == 1): # checking @ present in email or not and not more than once
            if (email[-4] == ".") ^ (email[-3] == "."): #this is checking letter by index method -4(.com) and -3(.in)
                for i in email: #using for loop to check each letter of string(email)
                    if i == i.isspace(): # If it is blank or not
                        k = 1
                    elif i == i.upper(): #if there is any letter is in capslock form 
                        j = 1
                    elif i == i.isdigit(): #if there is a digit in email
                        continue
                    elif i == "_" or i == "." or i == "@":  #if any of them is present
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
    
