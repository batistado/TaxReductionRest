import argparse
import csv
import json

from pymongo import MongoClient
from pymongo import UpdateOne
from pymongo import ASCENDING

from utils.dbConfig import MONGODB_HOST, MONGODB_PORT, DB_NAME
from utils.path import get_parent_dir, get_parent_dir_from_dir, join_paths

PROJECT_DIR = get_parent_dir_from_dir(get_parent_dir(__file__))
CUSTOM_FIELDS_PATH = "taxreductionapp/data/customFields.json"
COLLECTION_NAME = 'Properties'
BATCH_SIZE = 5000


class PropertyDataImporter:
    def __init__(self) -> None:
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)[DB_NAME]
        self.db[COLLECTION_NAME].create_index(
            [('PropertyID', ASCENDING)], unique=True)
        self.custom_fields = self._get_custom_fields()

    def _get_custom_fields(self):
        with open(join_paths(PROJECT_DIR, CUSTOM_FIELDS_PATH)) as f:
            return json.load(f)

    def _create_custom_fields(self, data: dict, record, key):
        for prop in self.custom_fields[key].keys():
            field_details = self.custom_fields[key][prop]

            data[field_details["name"]] = record[prop].split(field_details["separator"])[
                field_details["index"]]

    def ingest_data(self, file, headers, collection, keys, custom_fields_key=None):
        if file == "":
            raise ValueError("file path can not be empty.")

        batch = list()
        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            # Skip the headers line.
            next(reader, None)

            for record in reader:
                record_key = dict()

                for k in keys:
                    record_key[k] = record[k]

                data = dict()
                for header in headers:
                    data[header] = record[header]

                if custom_fields_key:
                    self._create_custom_fields(data, record, custom_fields_key)

                batch.append(
                    UpdateOne(record_key, {'$set': data}, upsert=True))

                if len(batch) >= BATCH_SIZE:
                    res = self.db[collection].bulk_write(batch)
                    batch.clear()

    def ingest_property_data(self, property_file) -> None:
        headers = ['PropertyID',
                   'QuickRefID',
                   'PropertyNumber',
                   'LegalDesc',
                   'LegalAcres',
                   'AbstractBlock',
                   'SubBlock',
                   'SubLot',
                   'SubLotRange',
                   'SubSection',
                   'SubUnit',
                   'TaxingUnitList',
                   'MarketValue',
                   'AssessedValue',
                   'LandValue',
                   'ImprovmentValue',
                   'AgValue',
                   'SquareFootage',
                   'NbhdCode',
                   'NbhdDesc',
                   'Situs']

        self.ingest_data(property_file, headers,
                         COLLECTION_NAME, ['PropertyID'], custom_fields_key="Property")

    def ingest_sales_data(self, sales_file) -> None:
        headers = ['PropertyID',
                   'QuickRefID',
                   'PropertyNumber',
                   'SaleDate',
                   'DeedDate',
                   'PrevOwnerName',
                   'DeedType']

        self.ingest_data(sales_file, headers,
                         COLLECTION_NAME, ['PropertyID'])

    def ingest_owner_data(self, owner_file) -> None:
        headers = ['PropertyID',
                   'QuickRefID',
                   'PropertyNumber',
                   'OwnerName', 'Address1', 'Address2', 'Address3', 'City', 'State', 'Zip', 'OwnershipPercent']

        self.ingest_data(owner_file, headers,
                         COLLECTION_NAME, ['PropertyID'])

    def ingest_land_data(self, land_file) -> None:
        headers = ['PropertyID',
                   'QuickRefID',
                   'PropertyNumber',
                   'LandType', 'Description', 'SquareFeet', 'EffDepth']

        self.ingest_data(land_file, headers,
                         COLLECTION_NAME, ['PropertyID'])

    def ingest_improvement_data(self, impr_file) -> None:
        headers = ['PropertyID',
                   'QuickRefID',
                   'PropertyNumber',
                   'Type', 'Description', 'Sequence', 'ImpValue']

        self.ingest_data(impr_file, headers,
                         COLLECTION_NAME, ['PropertyID'])

    def ingest_segment_data(self, seg_file) -> None:
        headers = ['PropertyID',
                   'QuickRefID',
                   'PropertyNumber',
                   'InstanceID', 'Type', 'Description', 'Class', 'ActYrBuilt', 'EffYrBuilt', 'Area', 'AreaFactor', 'Vectors', 'Sequence', 'Bedrooms', 'Fireplace', 'HeatAC', 'Roof', 'Foundation', 'ExtFinish', 'Plumbing']

        self.ingest_data(seg_file, headers,
                         COLLECTION_NAME, ['PropertyID'])


# dummy
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--property', required=False,
                        help="absolute path to properties data file")
    parser.add_argument('-l', '--land', required=False,
                        help="absolute path to land data file")
    parser.add_argument('-o', '--owner', required=False,
                        help="absolute path to owners data file")
    parser.add_argument('-sa', '--sales', required=False,
                        help="absolute path to sales data file")
    parser.add_argument('-se', '--segment', required=False,
                        help="absolute path to segments data file")
    parser.add_argument('-i', '--improvement', required=False,
                        help="absolute path to improvement data file")

    args = parser.parse_args()

    importer = PropertyDataImporter()
    try:
        if args.property:
            importer.ingest_property_data(args.property)

        if args.land:
            importer.ingest_land_data(args.land)

        if args.owner:
            importer.ingest_owner_data(args.owner)

        if args.sales:
            importer.ingest_sales_data(args.sales)

        if args.improvement:
            importer.ingest_improvement_data(args.improvement)

        if args.segment:
            importer.ingest_segment_data(args.segment)

    except Exception as e:
        print(e)
