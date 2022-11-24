from dnslib.server import DNSServer, DNSLogger, DNSRecord
from resolver import GouachDNSResolver
from helper import debug, LOG_PREFIX
import os

def run_server() -> DNSServer:
  resolver = GouachDNSResolver()
  logger = DNSLogger(prefix=LOG_PREFIX)
  server = DNSServer(resolver, port=int(os.getenv('DNS_SERVER_PORT')), address="0.0.0.0", logger=logger, tcp=True)
  debug('Starting')
  server.start_thread()
  debug('Succesfully started')
  return server