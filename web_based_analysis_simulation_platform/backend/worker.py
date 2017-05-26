#!/usr/bin/env python3
from celery import Celery
from algorithm import approx

# run with:
# redis-server
# celery -A worker worker --loglevel=debug

app = Celery(__name__, backend='rpc://', broker='redis://localhost:6379/')

@app.task
def integrate(*args, **kwargs):
    try:
        return approx(*args, **kwargs)
    except Exception:
        return

# integrate = app.task(approx)
