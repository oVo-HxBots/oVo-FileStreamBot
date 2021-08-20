#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

from pyrogram import Client
from .config import Config

StreamBot = Client(
    session_name='oVo_FileStreamBot',
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    sleep_threshold=Config.SLEEP_THRESHOLD,
    workers=Config.WORKERS
)