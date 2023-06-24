from .models import Expense,Income


def exin():
    exp_model = Expense.objects.all()
    inc_model = Income.objects.all()
    
    exp = 0
    inc = 0
    
    for expense in exp_model:
        exp = exp + expense.price
        
    for income in inc_model:
        inc = inc + income.price

    return inc - exp
        


