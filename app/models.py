from django.db import models

# Create your models here.
class artist(models.Model):
	name=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	
class customer(models.Model):
	name=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	
class product(models.Model):
	image=models.ImageField(upload_to="images")
	name=models.CharField(max_length=20)
	price=models.IntegerField()
	
class comment(models.Model):
	urname=models.CharField(max_length=20)
	arname=models.CharField(max_length=20)
	comments=models.TextField()
	
class purchased(models.Model):
	uname=models.CharField(max_length=20)
	iname=models.CharField(max_length=20)
	image=models.ImageField()
	price=models.IntegerField()