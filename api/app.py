from flask import Flask, jsonify
from flask_cors import CORS
import redis, os, json

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_batteries():
    buffer = {}
    redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"))

    for key in redis_client.keys(pattern='*'):
      buffer[key.decode('ascii')] = json.loads(redis_client.get(key).decode("ascii"))

    return jsonify(buffer)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug=True)