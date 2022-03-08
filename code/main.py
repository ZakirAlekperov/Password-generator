

from pickle import FALSE, TRUE


def password_generator():
    pass

def check_checkboxs_value(number: bool, lowers: bool, capital: bool, special: bool):
    if number == True: pass
    if lowers == True: pass
    if capital == True: pass
    if special == True: pass

def check_checboxs_correct(number: bool, lowers: bool, capital: bool, special: bool):
    return number or lowers or capital or special

def is_number(str: str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    

def is_correct_length(str: str): 
    if is_number(str):
        if float(str) <= 50:
            return True
        else:
            return False
    else:
        return False
    
print(is_correct_length("ddg"))

