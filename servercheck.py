from datetime import datetime
import time
import os

from flask import Flask, request
from prometheus_client import Counter, Enum, Gauge, generate_latest, start_http_server
from apscheduler.schedulers.background import BackgroundScheduler

c = Counter('view', 'path view', ['task'])
my_state = 'odd'
e = Enum('my_task_state', 'Description of enum', states=['even', 'odd'])


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
    else:
        my_state = 'odd'
        e.state('even')
    return "<p>Hello, World!</p> from request.path: %s" % request.path

def train_model():
    c.labels(task='train_model').inc()
    print('dask train_model! The time is: %s' % datetime.now())


if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    scheduler.add_job(train_model, 'interval', minutes=1)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    app.run()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()