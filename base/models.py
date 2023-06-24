from django.db import models



class Expense(models.Model):
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
    favorite = models.CharField(choices=FAVORITE,default="False",max_length=6)
    tag = models.CharField(choices=TAGS,blank=True,null=True,max_length=15)
    title = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def price_display(self):
        return f"R {self.price}"


class Income(models.Model):
    TAGS = (
        ("Salary","Salary"),
        ("interest","interest"),
        ("monthly","monthly"),
        ("other","other"),
    )
    FAVORITE = (
        ("True","True"),
        ("False","False")
    )
    favorite = models.CharField(choices=FAVORITE,default="False",max_length=6)
    tag = models.CharField(choices=TAGS,blank=True,null=True,max_length=15)
    title = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def price_display(self):
        return f"R {self.price}"

    
class Note(models.Model):
    TAGS = (
        ("reminder","reminder"),
        ("tip","tip"),
    )
    FAVORITE = (
        ("True","True"),
        ("False","False")
    )
    favorite = models.CharField(choices=FAVORITE,default="False",max_length=6)
    tag = models.CharField(choices=TAGS,blank=True,null=True,max_length=15)
    title = models.CharField(max_length=100)

    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)