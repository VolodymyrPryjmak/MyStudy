import re
def normalize_phone(phone_number):
    ### пошук і аналіз кількості цифр, спереду 38 
    nom = re.findall("[0-9]",phone_number)
    if len(nom) == 10:
        nom.insert(0,"3")
        nom.insert(1,8)
    elif len(nom) == 11:
          nom.insert(0,"3")
          nom[1] = "8"
    elif len(nom) == 12:  
         nom[0] = "3"
         nom[1] = "8"
    else:
        print(f"Неправильна кількість цифр в номері {phone_number} ")    
        return

    #x1 = re.search("[+]",phone_number)
    #x2 = re.search("[0-9]",phone_number)
    # спереду + , незалежно був чи ні введений
    nom.insert(0,"+")     

    number = ""
    for x in nom:
        number += str(x)

    return  number     

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)