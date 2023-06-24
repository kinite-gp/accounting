from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.PasswordInput()
    
    
class ExpenseForm(forms.Form):
    TAGS = (
        ("Food","Food"),
        ("Car","Car"),
        ("House","House"),
        ("General","General"),
        ("Treatment","Treatment"),
        ("Recreation","Recreation"),
        ("Travel","Travel"),
        ("Other","Other"),
    )
    FAVORITE = (
        ("True","True"),
        ("False","False")
    )
    title = forms.CharField(required=True, max_length=250,label="موضوع")
    tag = forms.ChoiceField(choices=TAGS, label="دسته بندی")
    favorite = forms.ChoiceField(choices=FAVORITE, label="علاقه مندی")
    price = forms.DecimalField(max_digits=8, decimal_places=2,required=True, label="قیمت")
    description = forms.CharField(widget=forms.Textarea, label="توضیحات")