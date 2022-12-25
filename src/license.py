# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
"""
import pymongo, time, requests
from urllib.request import Request, urlopen

__VERSION__ = "2.1"


class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"


Pass = True
while Pass:
    try:
        mongo = pymongo.MongoClient("")
        cluster = mongo["cryonicx"]
        database = cluster["spotify"]
        Pass = False
        print(f'{color.GREEN}[+] Connected to DB.{color.RESET_ALL}')
    except Exception as err:
        print(f"{color.RED}Trying to connect DB:{color.RESET_ALL} {err}.")
        time.sleep(5)


def get_current_date() -> str:
    try:
        r = requests.get("http://worldtimeapi.org/api/timezone/Europe/Istanbul").json()
        return r["datetime"].split("T")[0]
    except Exception as e:
        print(e)


def get_version() -> str:
    x = urlopen("https://raw.githubusercontent.com/CryonicsX/SpotifyStreamBot/main/version.txt")
    a = x.read().splitlines()
    return a[0].decode()


def check_license(license_key: str, device_id: str):
    data = database.find_one({"license_key": license_key})
    if data:
        bitis = data["license_expiry_date"].replace("-", "")
        bugun = get_current_date().replace("-", "")
        device_list = data["device_id"]

        if device_id in device_list:

            if data["license_expiry_date"] == "license_expired":
                return [False, f"Your license has expired!"]

            elif data["license_expiry_date"] != get_current_date() and bitis > bugun:
                if get_version() == __VERSION__:
                    return [True]
                else:
                    return [False, f"Please use the current version of the program."]
            else:
                database.update_one({"license_expiry_date": data["license_expiry_date"]},
                                    {"$set": {"license_expiry_date": "license_expired"}})
                return [False, f"Your license has expired!"]
        else:
            if "UNDEFINED" in device_list:
                leng = device_list.index("UNDEFINED")
                database.update_one({"_id": data["_id"]}, {"$set": {'device_id.' + str(leng): device_id}})
                return [True]
            else:
                return [False, "INVALID LICANSE"]
    else:
        return [False, "INVALID LICANSE"]



"""


# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >