# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 5235547))
    API_HASH = os.environ.get("API_HASH", "69ff912f0d3150af610c1542031617ef")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5436661916:AAHIrm0oZ2oH3-jp4Mde-AQr-haugdBTSjY")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5137809317 1956698956").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["False", "false"]
    LOGS_CHANNEL = int(os.environ.get("-100704206291")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("chan_viruz@yahoo.com")
    MEGA_PASSWORD = os.environ.get("adivita2604")
