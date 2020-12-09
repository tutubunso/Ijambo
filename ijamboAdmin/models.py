from django.db import models


class events(models.Model):
	cover=models.ImageField(upload_to="picture/img")
	organisateur=models.CharField(max_length=30)
	place=models.CharField(max_length=20)
	prix=models.IntegerField()
	paid =models.BooleanField(default=False)


	def __str__(self):
		return f"{self.cover} --{self.organisateur} -- {self.place} -- {self.prix}"


class contact(models.Model):
	email=models.CharField(max_length=20)
	message= models.CharField(max_length=1000)

	def __str__(self):
		return f"{self.email} -- {self.message}"

class paiement(models.Model):
	code=models.IntegerField()
	code=models.IntegerField()

	def __str__(self):
		return f"{self.code} -- {self.code}"
