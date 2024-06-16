from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=32, null=False)
    productLocation = models.CharField(max_length=64, null=False)
    productActivity = models.TextField()
    productDining = models.TextField()
    productPrice = models.IntegerField(null=False)
    productImageName = models.CharField(max_length=128, null=False)
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"hotelName: {self.productName}\nhotelLocation: {self.productLocation}"

    class Meta:
        db_table = "product"