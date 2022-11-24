from .repository import RepositoryInterface
import redis, os

class RedisRepository(RepositoryInterface):
  def __init__(self):
  	self.redis_client = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=os.getenv('REDIS_DB'))
  
  def persist(self, battery_id: str, payload: str) -> bool:
    return self.redis_client.set(battery_id, payload)