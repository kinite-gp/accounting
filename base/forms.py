from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.PasswordInput()
    
    
class ExpenseForm(forms.Form):
    TAGS = (
        ("Food","غذا"),
        ("Car","ماشین"),
        ("House","خانه"),
        ("General","عمومی"),
        ("Treatment","درمان"),
        ("Recreation","تفریح"),
        ("Travel","سفر"),
        ("Other","متفرقه"),
    )
    FAVORITE = (
        ("True","فعال"),
        ("False","غیرفعال")
    )
    title = forms.CharField(required=True, max_length=250,label="موضوع")
    tag = forms.ChoiceField(choices=TAGS, label="دسته بندی")
    favorite = forms.ChoiceField(choices=FAVORITE, label="علاقه مندی",initial="False")
    price = forms.CharField(required=True , max_length=255 ,label="قیمت")
    description = forms.CharField(widget=forms.Textarea, label="توضیحات")
    
class IncomeForm(forms.Form):
    TAGS = (
        ("Salary","حقوق"),
        ("interest","سود"),
        ("monthly","ماهیانه"),
        ("other","متفرقه"),
    )
    FAVORITE = (
        ("True","فعال"),
        ("False","غیرفعال")
    )
    title = forms.CharField(required=True, max_length=250,label="موضوع")
    tag = forms.ChoiceField(choices=TAGS, label="دسته بندی")
    favorite = forms.ChoiceField(choices=FAVORITE, label="علاقه مندی",initial="False")
    price = forms.CharField(required=True , max_length=255 ,label="قیمت")
    description = forms.CharField(widget=forms.Textarea, label="توضیحات")
    
    
class NoteForm(forms.Form):
    TAGS = (
        ("reminder","یادآور"),
        ("tip","نکته"),
    )
    FAVORITE = (
        ("True","فعال"),
        ("False","غیرفعال")
    )
    title = forms.CharField(required=True, max_length=250,label="موضوع")
    tag = forms.ChoiceField(choices=TAGS, label="دسته بندی")
    favorite = forms.ChoiceField(choices=FAVORITE, label="علاقه مندی",initial="False")
    description = forms.CharField(widget=forms.Textarea, label="توضیحات")