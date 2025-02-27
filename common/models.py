from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.PROTECT)

class BlogModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

class CategoriesModel(models.Model):
    title = models.CharField(max_length=255)

class ProductModel(models.Model):
    categories = models.ManyToManyField(CategoriesModel)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True