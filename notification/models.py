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

