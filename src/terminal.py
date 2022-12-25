# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >

import os, time, yaml, requests
from .misc import *

tokens = open("./config/tokens.txt", "+r", encoding="utf-8").read().splitlines()
proxies = open("./config/proxies.txt", "+r", encoding="utf-8").read().splitlines()
with open('./config/config.yml') as f: config = yaml.load(f, Loader=yaml.FullLoader)

__streaming = 0
__earning = 0
__current_client = 0
__bad_procces = 0
__total_auth = 0


class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET_ALL = "\033[0m"


def stream_succes():
    global __streaming
    __streaming = __streaming + 1


def earning_succes():
    global __earning
    __earning = __earning + 0.004


def client_succes():
    global __current_client
    __current_client = __current_client + 1


def bad_procces():
    global __bad_procces
    __bad_procces = __bad_procces + 1


def total_auth():
    global __total_auth
    __total_auth = __total_auth + 1


def send_webhook() -> None:
    try:
        if config["use_discord_webhook"]:

            embed = {
                "description": f"→ Accounts: **{len(tokens)}**\n→ Proxies: **{len(proxies) if config['use_proxy'] else 'Proxyless'}**\n→ Total Client: **{__current_client}**\n→ Successful Auth: **{__total_auth}**\n→ Total Streaming: **{__streaming}**\n→ Remaining Stream: **{config['view_count'] - __streaming}**\n→ Total Earning: **{__earning}**$\n→ Bad Procces: **{__bad_procces}**",
                "title": "SpoDoss 2022 - By CryonicX"
            }

            data = {
                "username": "SpoDoss - WEBHOOK",
                "avatar_url": "https://media.discordapp.net/attachments/917863500720767066/986221202429313064/download-icon-socialspotifysquareicon-1320185493878020594_512.png",
                "embeds": [embed],
            }

            headers = {
                "Content-Type": "application/json"
            }

            r = requests.post(config["discord_webhook_url"], json=data, headers=headers)
            '''
            if 200 <= r.status_code < 300:
                print(f"[{get_time()}]{color.GREEN}-[WEBHOOK] Webhook Sent. {color.RESET_ALL}")
            else:
                print(f"[{get_time()}]{color.RED}-[WEBHOOK] Webhook not sent. {color.RESET_ALL}")
            '''
    except Exception as e:
        print(f"[{get_time()}]-{color.RED}[WEBHOOK_ERROR] {e} {color.RESET_ALL}")

def title_thread():
    while True:
        time.sleep(1)
        os.system(
            f"title SpoDoss 2022 - By CryonicX - Accounts: {len(tokens)} - Proxies: {len(proxies) if config['use_proxy'] else 'Proxyless'} - Total Client: {__current_client} - Successful Auth: {__total_auth} - Total Streaming: {__streaming} - Remaining Stream: {config['view_count'] - __streaming} - Total Earning: {__earning}$ - Bad Procces: {__bad_procces}")
        send_webhook()


# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >