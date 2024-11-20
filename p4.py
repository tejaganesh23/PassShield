def pass_shield(pd): 
    uc, lc, d, sc = False, False, False, False
    scs = ['!', '@', '#', '$', '%', '&', '/']
    for i in pd:
        if i.isdigit():
            d = True
        elif i.islower():
            lc = True
        elif i.isupper():
            uc = True
        elif not sc and i in scs:
            sc = True
        else:
            return False, False, False, False
    return lc, uc, d, sc

print("Wecome to PassShield".center(127))
print()
print("Know your password Strength....")
print("Improve it, if needed.....")
print()
while True:
    print("~"*100)
    pd = input("Enter your password: ")
    if len(pd) < 8:
        print("Too weak")
        print("Password must have 8 or above characters.")
        continue
    lc, uc, d, sc = pass_shield(pd)
    st = int(lc) + int(uc) + int(d) + int(sc)
    if st == 0:
        print("Your password contains Unintended characters...(e.g: ' ', '>', '*', etc...)")
    elif st == 4:
        print("---> Strength: Very Strong....")
        break
    elif st == 3:
        print("---> Strength: Strong...")
        if not lc:
            print("Password should contain atleast one LOWER CASE LETTER...")
            
        elif not uc:
            print("Password should contain atleast one UPPER CASE LETTER...")
            
        elif not d:
            print("Password should contain atleast one DIGIT...")
            
        else:
            print("Password should contain atleast one SPECIAL CHARACTER...")
        continue    
    elif st == 2:
        print("---> Strength: Average...")
        if not lc:
            print("Password should contain atleast one LOWER CASE LETTER...")
        if not uc:
            print("Password should contain atleast one UPPER CASE LETTER...")
        if not d:
            print("Password should contain atleast one DIGIT...")
        if not sc:
            print("Password should contain atleast one SPECIAL CHARACTER...")
        continue
    else:
        print("---> Strength: Weak...")
        if lc:   
            print("Password should contain atleast one UPPER CASE LETTER...")
            print("Password should contain atleast one DIGIT...")
            print("Password should contain atleast one SPECIAL CHARACTER...")
        elif uc:
            print("Password should contain atleast one LOWER CASE LETTER...")
            print("Password should contain atleast one DIGIT...")
            print("Password should contain atleast one SPECIAL CHARACTER...")
        elif d:
            print("Password should contain atleast one LOWER CASE LETTER...")
            print("Password should contain atleast one UPPER CASE LETTER...")
            print("Password should contain atleast one SPECIAL CHARACTER...")
        else:
            print("Password should contain atleast one LOWER CASE LETTER...")
            print("Password should contain atleast one UPPER CASE LETTER...")
            print("Password should contain atleast one DIGIT...")
        continue
    