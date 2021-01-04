from django.db import models
from mongoengine import *

# Create your models here.


class Properties(Document):
    meta = {
        'collection': 'Properties',
        'strict': False,
        'indexes': [
            ('Situs'),
        ]}

    PropertyID = StringField(max_length=200, required=True)
    Situs = StringField(max_length=2000)
