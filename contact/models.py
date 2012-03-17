from django.db import models
#from datetime import date




class ContactInfo(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=75)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zip_code = models.IntegerField(max_length=11)
	phone = models.IntegerField(max_length=11)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	
	question = models.TextField(max_length=400)


	def __unicode__(self):
		return self.name



