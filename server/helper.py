import base64

LOG_PREFIX = "[Gouach DNS Server]"

def debug(msg: str) -> str:
  print("%s %s" % (LOG_PREFIX, msg))

def decode(msg: str) -> str:
  msg_bytes = base64.b64decode(msg.encode("ascii"))
  return msg_bytes.decode("ascii")