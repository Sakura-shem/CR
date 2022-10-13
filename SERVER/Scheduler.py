import datetime
from flask_apscheduler import APScheduler
from flask import Flask


scheduler = APScheduler()

class Config(object):
    SCHEDULER_API_ENABLED = True
