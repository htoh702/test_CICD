from __future__ import unicode_literals

import time
import redis
from flask import Flask
import os

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_SERVER'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('this')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hit():
    count = get_hit_count()
    return 'Welcome to you have %i visitors on this page. by hyun.oh' % int(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


