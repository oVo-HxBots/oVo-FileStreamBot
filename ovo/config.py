#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    API_ID = "924859"
    API_HASH = "a4c9a18cf4d8cb24062ff6916597f832"
    BOT_TOKEN = "1670920423:AAGNpQwyLUFDRPdqQZQtWomuI_uGC6nfyso"
    SESSION_NAME = str(getenv('SESSION_NAME', 'oVo_FileStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    LOG_CHANNEL = "-1001364200595"
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = "filestream.rehost.tech"
    OWNER_ID = "754495556"
    NO_PORT = "False"
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU else APP_NAME+'.herokuapp.com'
    DATABASE_URL = "mongodb+srv://user:user@cluster0.x7biw.mongodb.net/filestreambot"
    JOIN_CHANNEL = "hxbots"
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS",)).split()))
