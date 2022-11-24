import sys, base64
from random import randint
from dns_resolve import resolve

def encode(payload: str) -> str:
  base64_bytes = base64.b64encode(payload.encode("ascii"))
  base64_string = base64_bytes.decode("ascii")
  return base64_string

payload = encode('{"level": %s}' % randint(1, 100))
uri = "23udju.=%s" % payload

try:
  answer = resolve(uri)
  print("Sucessfully sent question to the DNS Server")
except Exception:
  print("Invalid request uri")
  sys.exit(1)
