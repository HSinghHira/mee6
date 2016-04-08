import aioredis
import asyncio
import logging
from storage import Storage
from utils import parse_redis_url

log = logging.getLogger('discord')

class Db(object):
    def __init__(self, redis_url, loop):
        self.loop = loop
        self.redis_url = redis_url
        self.loop.create_task(self.create())
        self.redis_address = parse_redis_url(redis_url)

    async def create(self):
        self.redis = await aioredis.create_redis(
            self.redis_address,
            encoding='utf8'
        )

    async def get_storage(self, plugin, server):
        namespace = "{}.{}:".format(
            plugin.__class__.__name__,
            server.id
        )
        storage = Storage(namespace, self.redis_url)
        await storage.create()

        return storage
