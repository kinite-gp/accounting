from .models import Expense,Income


def exin():
    exp_model = Expense.objects.all()
    inc_model = Income.objects.all()
    
    exp = 0
    inc = 0
    
    for expense in exp_model:
        exp = exp + int(expense.price)
        
    for income in inc_model:
        inc = inc + int(income.price)

    exin_value = inc - exp
    
    if str(exin_value)[0] == "-":
        return [exin_value*-1 , "-"]
    else:
        return [exin_value , ""]

        


