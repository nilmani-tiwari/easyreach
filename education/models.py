from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class QuestionBank(models.Model):
    vendor_id = models.CharField(max_length=250, help_text="Identification for the campaign")
    subject = models.CharField(max_length=200, help_text="Max 200 characters", null=True, blank=True)
    question_html = models.TextField(help_text="Put full HTML", null=True, blank=True)
    label = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    answer = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    answer = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    answer = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    answer = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    answer = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")

    emails = models.TextField(null=True, blank=True, max_length=25000)
    from_email = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    subject = models.CharField(max_length=200, help_text="Max 200 characters", null=True, blank=True)
    body_html = models.TextField(help_text="Put full HTML", null=True, blank=True)
    attachment = models.FileField(upload_to="one_off_emails/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    password=models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth=models.DateField(blank=True,null=True)
    # owner_date_of_birth=models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField( max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=12,  blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=20,blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)



class School(models.Model):
    # school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    school_code = models.CharField(unique=True, max_length=200, blank=True, null=True)
    registration_number=models.CharField( max_length=200, blank=True, null=True)
    affiliated_by=models.CharField( max_length=200, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200, blank=True, null=True)
    mobile = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=20,blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    principal_sign_image = models.ImageField(upload_to='images/', blank=True, null=True)
    logo_of_school = models.ImageField(upload_to='images/', blank=True, null=True)
    password=models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    # user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    owner_gender = models.CharField(max_length=10, blank=True, null=True)
    #owner_date_of_birth=models.DateField(blank=True,null=True)
    owner_date_of_birth=models.CharField(max_length=10, blank=True, null=True)
    owner_email = models.CharField( max_length=200, blank=True, null=True)
    owner_mobile = models.CharField(max_length=10,  blank=True, null=True)
    owner_image = models.ImageField(upload_to='images/', blank=True, null=True)
    owner_qualification = models.CharField(max_length=200, blank=True, null=True)
    owner_address = models.CharField(max_length=200, blank=True, null=True)
    owner_city = models.CharField(max_length=200, blank=True, null=True)
    owner_pincode = models.CharField(max_length=20,blank=True, null=True)
    owner_school_code=models.CharField(max_length=200, null=True,blank=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.school_name+" "+str(self.school_code)
