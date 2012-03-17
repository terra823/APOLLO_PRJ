from django.db import models

class CensusInfo(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=75)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zip_code = models.IntegerField(max_length=11)
	phone = models.IntegerField(max_length=11)
	email = models.EmailField()
	is_accepted = models.BooleanField(default=False)
	admin_comments = models.TextField(blank=True, null=True)


	def __unicode__(self):
		return self.name

		

