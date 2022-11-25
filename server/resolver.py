from helper import debug, decode
from dnslib.server import DNSHandler, BaseResolver
from infrastructure.redis_repository import RedisRepository
from invalid_dns_question_exception import InvalidDnsQuestionException

class GouachDNSResolver(BaseResolver):
  def __init__(self):
    self.redis_repository = RedisRepository()

  def parse_battery_id(self, uri: str) -> str:
    return str(uri).split('.')[0]

  def parse_payload(self, uri: str) -> str:
    return str(uri)[1:].split('.')[1]

  def resolve(self, request, handler: DNSHandler):
    reply = request.reply()

    try:
      battery_id = self.parse_battery_id(reply.q.qname)
      payload = self.parse_payload(reply.q.qname)
      decoded_payload = decode(payload)
      debug("Battery %s authenticating with payload %s" % (battery_id, payload))
      debug("Decoded payload %s" % (decoded_payload))
    except Exception:
      debug("Invalid DNS Question")
      raise InvalidDnsQuestionException('Invalid DNS Question')
    
    if self.redis_repository.persist(battery_id, decoded_payload):
      debug("Succesfully persisted payload to redis")
    
    return reply