# blog/models.py
from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	category = models.ForeignKey(to="Category", on_delete=models.CASCADE,related_name='posts')
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-created',)