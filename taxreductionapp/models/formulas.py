from django.db import models
from mongoengine import *

# Create your models here.


class FormulaDetails(EmbeddedDocument):
    meta = {
        'strict': False,
    }
    name = StringField(max_length=200,)
    property = StringField(max_length=200, required=True)
    matchType = StringField(max_length=200, required=True)


class Formulas(Document):
    meta = {
        'collection': 'Formula',
        'strict': False,
    }

    eq = ListField(EmbeddedDocumentField(FormulaDetails))
    lte = ListField(EmbeddedDocumentField(FormulaDetails))
