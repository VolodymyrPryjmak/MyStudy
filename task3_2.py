import random
def get_numbers_ticket(min, max, quantity):
    lottery_numbers_s = set()
    a = set()
    
    while len(lottery_numbers_s) < quantity:
          b = random.randrange(min, max, 1)
          a.add(b)
          lottery_numbers_s.update(a)    ## не знаю, чи метод add вставляє дублюючі значення
  
    lottery_numbers = sorted(lottery_numbers_s)
    #lottery_numbers = list()            ## в список, щоб посортувати
    #for x in lottery_numbers_s:
    #    lottery_numbers.append(x)        
    #lottery_numbers.sort()    
    return lottery_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні чиsсла:", lottery_numbers)
