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
    LegalDesc = StringField(max_length=2000)
    LegalAcres = StringField(max_length=2000)
    AbstractBlock = StringField(max_length=2000)
    SubBlock = StringField(max_length=2000)
    SubLot = StringField(max_length=2000)
    SubLotRange = StringField(max_length=2000)
    SubSection = StringField(max_length=2000)
    SubUnit = StringField(max_length=2000)
    TaxingUnitList = StringField(max_length=2000)
    MarketValue = StringField(max_length=2000)
    AssessedValue = StringField(max_length=2000)
    LandValue = StringField(max_length=2000)
    ImprovmentValue = StringField(max_length=2000)
    AgValue = StringField(max_length=2000)
    SquareFootage = StringField(max_length=2000)
    NbhdCode = StringField(max_length=2000)
    NbhdDesc = StringField(max_length=2000)
    SaleDate = StringField(max_length=2000)
    DeedDate = StringField(max_length=2000)
    PrevOwnerName = StringField(max_length=2000)
    DeedType = StringField(max_length=2000)
    OwnerName = StringField(max_length=2000)
    Address1 = StringField(max_length=2000)
    Address2 = StringField(max_length=2000)
    Address3 = StringField(max_length=2000)
    City = StringField(max_length=2000)
    State = StringField(max_length=2000)
    Zip = StringField(max_length=2000)
    OwnershipPercent = StringField(max_length=2000)
    LandType = StringField(max_length=2000)
    Description = StringField(max_length=2000)
    SquareFeet = StringField(max_length=2000)
    EffDepth = StringField(max_length=2000)
    Type = StringField(max_length=2000)
    Description = StringField(max_length=2000)
    Sequence = StringField(max_length=2000)
    ImpValue = StringField(max_length=2000)
    Class = StringField(max_length=2000)
    ActYrBuilt = StringField(max_length=2000)
    EffYrBuilt = StringField(max_length=2000)
    Area = StringField(max_length=2000)
    AreaFactor = StringField(max_length=2000)
    Vectors = StringField(max_length=2000)
    Sequence = StringField(max_length=2000)
    Bedrooms = StringField(max_length=2000)
    Fireplace = StringField(max_length=2000)
    HeatAC = StringField(max_length=2000)
    Roof = StringField(max_length=2000)
    Foundation = StringField(max_length=2000)
    ExtFinish = StringField(max_length=2000)
    Plumbing = StringField(max_length=2000)
