from datetime import datetime

def get_days_from_today(date):   
    try:
        date_get =datetime.strptime(date, "%Y-%m-%d").date()
    except:
        print("Неправильний формат заданої  дати") 
        return   
    today = datetime.today().date()     ### сьогодні 
    return today.toordinal() - date_get.toordinal()

print(get_days_from_today("2025-01-20"))
