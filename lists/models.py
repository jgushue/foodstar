from django.db import models

# Create your models here.
class Food_List(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField('date created')
	def __unicode__(self):
		return self.name

class Food_Item(models.Model):
	food_list = models.ForeignKey(Food_List)
	item = models.CharField(max_length=200)
	number = models.IntegerField(default=0)
	def __unicode__(self):
		return self.item