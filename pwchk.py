import re

print("Your password must: ", "\nContain 6-12 symbol", "\nContain at least one number", "\nShould not contain special symbols", "\nBegin with a letter", "\n")
pattern1 = r"[0-9]"
pattern2 = r"[^A-Za-z0-9]"
pattern3 = r"[^0-9]"
while 1 == 1:
    pointer = 0
    password = str(input())
    try:
        if len(password) < 6 or len(password) > 12:
            print("ERROR: Password must contain 6-12 symbols.")
            pointer +=1
        if not re.search(pattern1, password):
            print("ERROR: Password must contain at least one number.")
            pointer +=1
        if re.search(pattern2, password):
            print("ERROR: Password should not contain special symbols.")
            pointer +=1
        if not re.search(pattern3, password[0]):
            print("ERROR: Password must begin with a letter")
            pointer +=1
        print(splitted)
        if pointer > 0:
            raise Exception
    except Exception:
        print("Try again!")
    else:
        print("Password is OK!")
        break
    finally:
        pass
