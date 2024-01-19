from flask import Flask, request
import random
from datetime import datetime
from prometheus_client import Counter, Enum, Gauge, generate_latest

c = Counter('view', 'path view', ['path'])
my_state = 'odd'
e = Enum('my_task_state', 'Description of enum', states=['even', 'odd'])
a = Gauge('alert_state', 'Description of enum')

# Create my app
app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
@app.route("/metrics")
def metrics():
    return generate_latest()


@app.route("/")
def hello_world():
    global my_state

    if my_state == 'odd':
        my_state = 'even'
        e.state('odd')
        a.set('1')
    else:
        my_state = 'odd'
        e.state('even')
        a.set('0')
    return "<p>Hello, World!</p> from request.path: %s" % request.path
