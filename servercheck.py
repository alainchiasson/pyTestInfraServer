from datetime import datetime
import time
import os

from prometheus_client import Counter, Enum, Gauge, generate_latest, start_http_server

from apscheduler.schedulers.background import BackgroundScheduler

c = Counter('view', 'path view', ['task'])


def train_model():
    c.labels(task='train_model').inc()
    print('dask train_model! The time is: %s' % datetime.now())


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    scheduler = BackgroundScheduler()
    scheduler.add_job(train_model, 'interval', minutes=1)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()