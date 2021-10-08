def greatestNum(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(str(num1)+ " is greatest")
        else:
            print(str(num3)+ " is greatest")            
    else:
        if num2>num3:
            print(str(num2)+" is greatest")
        else:
            print(str(num3)+" is greatest")


greatestNum(6,1,3)