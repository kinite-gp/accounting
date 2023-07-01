from django.db import models



class Expense(models.Model):
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
    favorite = models.CharField(choices=FAVORITE,default="False",max_length=6)
    tag = models.CharField(choices=TAGS,blank=True,null=True,max_length=15)
    title = models.CharField(max_length=100)

    price = models.CharField(max_length=255)
    
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


class Income(models.Model):
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
    favorite = models.CharField(choices=FAVORITE,default="False",max_length=6)
    tag = models.CharField(choices=TAGS,blank=True,null=True,max_length=15)
    title = models.CharField(max_length=100)

    price = models.CharField(max_length=255)

    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def price_display(self):
        return f"R {self.price}"

    
class Note(models.Model):
    TAGS = (
        ("reminder","یادآور"),
        ("tip","نکته"),
    )
    FAVORITE = (
        ("True","فعال"),
        ("False","غیرفعال")
    )
    favorite = models.CharField(choices=FAVORITE,default="False",max_length=6)
    tag = models.CharField(choices=TAGS,blank=True,null=True,max_length=15)
    title = models.CharField(max_length=100)

    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)