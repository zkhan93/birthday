from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from time import strftime


def get_friend_image_path(instance,filename):
	base='images/friends/'
	filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f_')+filename
	return base+filename
	

def get_post_image_path(instance,filename):
	base='images/posts/'
	filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f_')+filename
	return base+filename
	

def get_enroll_image_path(instance,filename):
	base='images/enrolls/'
	filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f_')+filename
	return base+filename
	
class Friend(models.Model):
	user = models.OneToOneField(User)
	image=models.ImageField(upload_to=get_friend_image_path)
	date_of_birth=models.DateField("Date of Birth")
	def __str__(self):
		return self.user.first_name+" "+self.user.last_name+"("+self.user.username+")"
	def image_tag(self):
		return u'<img src="/%s" width=200/>' % self.image.url
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True
	
	
class Post(models.Model):
	image=models.ImageField(upload_to=get_post_image_path)
	caption=models.CharField(max_length=500)
	friend=models.ForeignKey(Friend)
	author=models.ForeignKey(Friend, related_name="author")
	def __str__(self):
		return "("+str(self.image)+")"+self.caption
		
class Comment(models.Model):
	comment=models.CharField(max_length=200)
	post=models.ForeignKey(Post)
	author=models.ForeignKey(Friend)
	def __str__(self):
		return self.comment
		

class UserEnroll(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(unique=True)
	username=models.CharField(max_length=50,unique=True)
	password=models.CharField(max_length=50)
	date_of_birth=models.DateField("Date of Birth")
	image=models.ImageField(upload_to=get_enroll_image_path)
	def __str__(self):
		return self.first_name+" "+self.last_name+"("+self.username+")"
	def image_tag(self):
		return u'<img src="/%s" width=200/>' % self.image.url
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True