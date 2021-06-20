from django.db import models
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField()
	image = models.ImageField(upload_to = 'images', default = "static/logo.png")

	def __str__(self):
		return self.title
