import json

from pymongo import MongoClient
from pymongo import UpdateOne

from utils.path import get_parent_dir, get_parent_dir_from_dir, join_paths
from utils.dbConfig import MONGODB_HOST, MONGODB_PORT, DB_NAME

PROJECT_DIR = get_parent_dir_from_dir(get_parent_dir(__file__))
FORMULA_PATH = "taxreductionapp/data/formula.json"
COLLECTION_NAME = 'Formula'


class FormulaImporter:
    def __init__(self) -> None:
        self.db = MongoClient(MONGODB_HOST, MONGODB_PORT)[DB_NAME]

    def _get_formula(self):
        with open(join_paths(PROJECT_DIR, FORMULA_PATH)) as f:
            return json.load(f)[COLLECTION_NAME.lower()]

    def import_formula(self):
        formula = self._get_formula()
        self.db[COLLECTION_NAME].update_one(
            {COLLECTION_NAME.lower(): COLLECTION_NAME.lower()}, {'$set': formula}, upsert=True)


if __name__ == '__main__':
    f = FormulaImporter()
    f.import_formula()
