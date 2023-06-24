from django.contrib import admin
from .models import Expense,Note,Income

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Note)
