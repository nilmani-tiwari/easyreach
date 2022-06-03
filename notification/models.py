from django.db import models
import json
import pdb
import time
from collections import Counter
from copy import deepcopy
from datetime import datetime, timedelta
import logging

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.db.models import CASCADE, SET_NULL
from django.contrib.auth.models import User
from easyreach.utils.ses_email import send_email

# from fcm_django.fcm import response_dict
# from fcm_django.models import FCMDevice, FCMDeviceQuerySet

# from analytics.models import PageViewLog
# from blog.models import BlogPost, BlogCategoryMap
# from expert.models import Expert, ExpertCategory
# from podcasts.models import Podcast, PodcastEpisode
# from shop.models import ShopCategoryMapping, ItemMeta, Item, Product
# from tlc.utils.utils import get_utm_link, datetime_str, append_tlcode, get_tlcode, chunks
# from rq import Queue
# from worker import conn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create your models here.


class EmailOutreach(models.Model):
    name = models.CharField(max_length=250, help_text="Identification for the campaign")
    emails = models.TextField(null=True, blank=True, max_length=25000)
    from_email = models.CharField(max_length=100, default="EasyReach.Today <sambadnilmani085@gmail.com>", help_text="Ensure that it's approved on SES. Format is what's put above as default")
    subject = models.CharField(max_length=200, help_text="Max 200 characters", null=True, blank=True)
    body_html = models.TextField(help_text="Put full HTML", null=True, blank=True)
    attachment = models.FileField(upload_to="one_off_emails/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "One Off Email Outreach"
        verbose_name_plural = "One Off Email Outreaches"

    def send(self):
        _TG = f'[ONE OFF EMAIL] [{self.name} / ID: {self.id}] '
        emails = self.emails.split(',')
        logger.info(f"{_TG} Starting to send {len(emails)} emails")
        c = 1
        t = int(len(emails))
        for email in emails:
            try:
                logger.info(f"{_TG} Sending (Email: {c}/{t} | {email})")
                # time.sleep(0.2)
                email = EmailMessage(
                    self.subject,
                    self.body_html,
                    self.from_email,
                    [email],
                    reply_to=['nilmani085@gmail.com']
                )
                email.content_subtype = 'html'

                if self.attachment:
                    email.attach(self.attachment.name.replace('one_off_emails/', ''), self.attachment.file.read())

                email.send(fail_silently=False)
            except:
                logger.info(f"{_TG} Failed for {email}")
            c += 1

        return




class UserVerificationCodes(models.Model):
    usr = models.ForeignKey(User, related_name="user_verification", on_delete=CASCADE)
    otp=models.IntegerField()
    verified = models.BooleanField(default=False,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[{}] - {}".format(self.otp, self.usr)

    class Meta:
        verbose_name = "User Verification Code"
        verbose_name_plural = "User Verification Codes"

    def send_email(self, recepient_email):
        send_email(
            subject="[{}] Your Verification Code for EasyReach.Today".format(self.otp),
            message="[{}] Your Verification Code for EasyReach.Today".format(self.otp),
            # template='notification/email/podcast_otp.html',
            template='notification/email/user_otp.html',
            data={
                "otp": self.otp,
                "podcast": self.usr.email
            },
            recipient_list=["alokraj.ad@gmail.com", recepient_email],
            from_email="User Verification <alokraj.ad@gmail.com>"
        )
        return


#E:\c drive data\My Home\easyest_deployment\backup\easyreach\templates\notification\email\podcast_otp.html

#    use    UserVerificationCodes    need template='emails/podcast_otp.html', 

# codes = PodcastVerificationCodes.objects.filter(podcast=podcast, created_at__gte=datetime.utcnow()-timedelta(days=1))
# if not codes.exists():
#     code = PodcastVerificationCodes.objects.create(podcast=podcast, otp=random.randint(1000, 9999))
#     code.send_email(recepient_email=request_verification_email)

# import random
# usr=User.objects.filter(username="nilamani@tickle.life")
# if usr.exists():
#     usr=usr.first()
# codes = UserVerificationCodes.objects.filter(usr=usr, created_at__gte=datetime.utcnow()-timedelta(days=1))
# if not codes.exists():
#     code = UserVerificationCodes.objects.create(usr=usr, otp=random.randint(1000, 9999))
#     code.send_email(recepient_email=request_verification_email)
#     print("code sent")
# else:
#    print("exist")


# from django.contrib.auth.models import User
# from notification.models import *
# import random
# request_verification_email="sambadnilmani085@gmail.com"
# usr=User.objects.filter(username="sambadnilmani085@gmail.com")
# if usr.exists():
#     usr=usr.first()
# codes = UserVerificationCodes.objects.filter(usr=usr, created_at__gte=datetime.utcnow()-timedelta(days=1))
# if not codes.exists():
#     code = UserVerificationCodes.objects.create(usr=usr, otp=random.randint(1000, 9999))
#     code.send_email(recepient_email=request_verification_email)
#     print("code sent")
# else:
#    print("exist")