height = input("How tall you are? : ")
gender = input("What is your gender?")



def std_weight(height, gender):
    mheight = int(height)/100
    weight =0
    if gender == "male":
        weight = mheight*mheight*22
        return weight
    elif gender == "female":
        weight = mheight*mheight*21
        return weight

nweight = round(std_weight(height,gender),2)#way to round number 2 mean only 2 decimals
print(nweight)