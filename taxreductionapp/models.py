from django.db import models
from mongoengine import *

# Create your models here.


class Properties(Document):
    meta = {'collection': 'Properties', 'strict': False}
    PropertyID = StringField(max_length=200, required=True)
