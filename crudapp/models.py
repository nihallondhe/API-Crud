from django.db import models
 
class Employee(models.Model):
 	Empid = models.IntegerField(primary_key = True)
 	Empname = models.CharField(max_length = 10)
 	Email = models.EmailField()
 	Salary = models.IntegerField(max_length=6)

 	class Meta:
 		db_table = 'EmployeeTable'