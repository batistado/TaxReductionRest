import redis
import json

from django.conf import settings


class AutoComplete:
    __instance = None

    def __init__(self) -> None:
        self.instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                          port=settings.REDIS_PORT, db=0)
        self.key = self.__class__.__name__
        AutoComplete.__instance = self

    @staticmethod
    def get_instance():
        if AutoComplete.__instance == None:
            AutoComplete()
        return AutoComplete.__instance

    def add(self, key, values):
        self.instance.hset(self.key, key, json.dumps(values))

    def get(self, key):
        if not self.instance.hexists(self.key, key):
            return None

        return json.loads(self.instance.hget(self.key, key))
