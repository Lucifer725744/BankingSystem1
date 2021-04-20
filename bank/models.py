from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_id=models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=50)
    cust_email=models.EmailField()
    cust_bal=models.FloatField()
    def __str__(self):
        return self.cust_name,self.cust_email,self.cust_bal

class Transfer(models.Model):
    trans_id=models.AutoField(primary_key=True)
    trans_amt=models.FloatField()
    trans_from_id=models.IntegerField()
    trans_to_id=models.IntegerField()