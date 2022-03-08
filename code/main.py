from random import randint

def numbers_base():
    return "0123456789"

def lowers_base():
    return "qwertyuiopasdfghjklzxcvbnm"

def capital_base():
    return "QWERTYUIOPASDFGHJKLZXCVBNM"

def special_base():
    return "%,*)?@#$~" 

def password_generator(length: int, base: str):
    password=""
    for i in range(length):
        password += base[randint(0,len(base)-1)]
    return password   
        

def password_print(length: str, numbers: bool, lowers: bool, capital: str, special: str):
    password: str
    password_base = ""
    if numbers:
        password_base += numbers_base()
    if lowers:
        password_base +=lowers_base()
    if capital:
        password_base += capital_base()
    if special:
        password_base += special_base()
    password = password_generator(int(length), password_base)
    return password

def check_checkboxs_value(number: bool, lowers: bool, capital: bool, special: bool):
    if number == True: pass
    if lowers == True: pass
    if capital == True: pass
    if special == True: pass

def check_checboxs_correct(number: bool, lowers: bool, capital: bool, special: bool):
    return number or lowers or capital or special

def is_number(str: str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    

def is_correct_length(str: str): 
    if is_number(str):
        if int(str) <= 50:
            return True
        else:
            return False
    else:
        return False


