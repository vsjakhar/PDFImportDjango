from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

gender = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'),('All','All'))
source = (('Website', 'Website'),('Android', 'Android'),('iOS', 'iOS'),('AMP', 'AMP'),('PWA', 'PWA'),('Desktop', 'Desktop'))
status=[('Active','Active'),('Inactive','Inactive'),('Delete','Delete')]

class User(AbstractUser):
	mobile = models.CharField(max_length=12, unique=True)
	phone = models.CharField(verbose_name="Alternate mobile", max_length=10, blank=True)
	gender = models.CharField(max_length=6, choices=gender, default='Male')
	dob = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='user/', blank=True, null=True, default="default/logo.png")
	tagline = models.CharField(max_length=80, blank=True)
	about = models.TextField(blank=True)
	occupation = models.CharField(max_length=100, blank=True)
	married = models.BooleanField(default=False)
	# country=models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True)
	# state=models.ForeignKey(State, on_delete=models.PROTECT, blank=True, null=True)
	city=models.CharField(max_length=50, blank=True)
	pincode=models.CharField(max_length=6, blank=True)
	address=models.TextField(blank=True)
	rawdata = models.TextField(blank=True)
	notification = models.TextField(blank=True)
	latitude = models.FloatField(blank=True, null=True) 
	longitude = models.FloatField(blank=True, null=True) 
	website = models.URLField(max_length=100, blank=True)
	facebook = models.URLField(max_length=100, blank=True)
	twitter = models.URLField(max_length=100, blank=True)
	instagram = models.URLField(max_length=100, blank=True)
	linkedin = models.URLField(max_length=100, blank=True)
	verified = models.BooleanField(default=False)
	multilogin = models.BooleanField(default=False)
	source = models.CharField(max_length=10, choices=source, default='Website')

class Collection(models.Model):
	"""docstring for Collection"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	pdf = models.FileField(upload_to='pdf/')
	title = models.CharField(max_length=50)
	content = models.TextField(blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Acitve')

	def __str__(self):
		return self.title
		
