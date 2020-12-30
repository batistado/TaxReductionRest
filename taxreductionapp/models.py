from django.db import models
from mongoengine import *

# Create your models here.


class Properties(Document):
    meta = {
        'collection': 'Properties',
        'strict': False,
        'indexes': [
            ('Address1', 'Address2', 'Address3', 'City', 'State', 'Zip'),
        ]}

    PropertyID = StringField(max_length=200, required=True)
    Address1 = StringField(max_length=2000)
    Address2 = StringField(max_length=2000)
    Address3 = StringField(max_length=2000)
    City = StringField(max_length=200)
    State = StringField(max_length=200)
    Zip = StringField(max_length=20)
