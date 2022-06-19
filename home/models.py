from django.db import models

# Create your models here.
class Customer(models.Model):
    Occupant_name = models.CharField(max_length=100)
    Occupant_email = models.EmailField()
    Occupant_occupation = models.CharField(max_length=100)
    def __str__(self):
        return self.Occupant_name

class Record(models.Model):
    Room_number = models.IntegerField()
    Amount_paid = models.CharField(max_length=20)
    Num_of_nights = models.IntegerField()
    Start_date = models.DateField()   
    End_date = models.DateField() 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return f'Record for {self.customer}, {self.End_date}'
    