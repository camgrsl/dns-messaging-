from dnslib.server import DNSRecord
import os

def resolve(uri: str) -> DNSRecord:
  question = DNSRecord.question(uri)
  answer = question.send("server", int(os.getenv("DNS_SERVER_PORT")), tcp=True)
  return DNSRecord.parse(answer)