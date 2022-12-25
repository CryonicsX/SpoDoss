# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >

import os, yaml, random, signal, traceback, requests, shutil
from string import ascii_lowercase
from subprocess import check_call, DEVNULL, STDOUT
from .misc import *
from .terminal import *

with open('./config/config.yml') as f: config = yaml.load(f, Loader=yaml.FullLoader)
username = os.environ.get("USERNAME")
current = os.path.expanduser('~')


class spotify_creator:
    def __init__(self, proxy: dict = None) -> None:
        self.proxy = proxy
        self.session = requests.Session()
        self.session.proxies.update(self.proxy) if proxy else ""

        self.headers = {
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US",
            "App-Platform": "Android",
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "spclient.wg.spotify.com",
            "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
            "Spotify-App-Version": "8.6.72",
            "X-Client-Id": random_string(32)
        }


    def create(self) -> list:
        try:
            
            password = random_string(12)
            username = get_name()
            email = f"{username}_{random_string(3)}{random.randint(1,12)}@{random.choice(['gmail', 'outlook', 'hotmail'])}.com"
            
            payload = {
                "creation_point": "client_mobile",
                "gender": "male" if random.randint(0, 1) else "female",
                "birth_year": random.randint(1970, 2005),
                "displayname": username,
                "iagree": "true",
                "birth_month": random.randint(1, 11),
                "password_repeat": password,
                "password": password,
                "key": "142b583129b2df829de3656f9eb484e6",
                "platform": "Android-ARM",
                "email": email,
                "birth_day": random.randint(1, 20)
            }
            
            
            res = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account/", headers=self.headers, data=payload)

            if res.json()["status"] == 1:
                username = res.json()["username"]

                if username != "":
                    print(f"[{get_time()}]-{color.GREEN}[{username}] Account created | {email} : {password} {color.RESET_ALL}")
                    write("./config/tokens.txt", f"{username}:{password}\n")
                    return [username, password]    
                
                else:
                    print(f"[{get_time()}]-{color.RED}[ERROR] While creating account | {res.json()} {color.RESET_ALL}")
                    return [None]
                    #self.create()
            else:
                print(f"[{get_time()}]-{color.RED}[ERROR] While creating account | {res.json()} {color.RESET_ALL}")
                return [None]
                #self.create()
                


        except Exception as e:
            print(e)


class spotify_streamer:
    def __init__(self, stream_url: str, username: str, password: str, mu: str, proxy: str = None):
        self.stream_url = stream_url
        self.username = username
        self.password = password
        self.proxy = proxy
        self.wait = config["program_sleep_delay"]
        self.song_wait = random.randint(config["min_wait_max_wait"][0], config["min_wait_max_wait"][1])
        self.mu = random.randint(0, 500)



    
    def send_stream(self) -> None:

        try:
            mu = self.mu
            print(f"[{get_time()}]-{color.BLUE}[{self.username}] Session started | Proxy: {self.proxy if self.proxy else 'Proxyless'}  {color.RESET_ALL}")
            st = subprocess.Popen([".\Spotify\Spotify.exe", f"--uri=spotify:track:{self.stream_url}", f" --username={self.username}",f" --password={self.password}", f"--mu={mu}", rf"--log-file={os.getcwd()}\logs\{self.username}-{mu}.log"])
            print(f"[{get_time()}]-{color.GREEN}[{self.username}] Client Started | PID: {st.pid} | M: {mu} {color.RESET_ALL}")
            client_succes()

            time.sleep(config["program_sleep_delay"])

            file_exists_(f'{os.getcwd()}\logs\{self.username}-{mu}.log')
            with open(rf'{os.getcwd()}\logs\{self.username}-{mu}.log', 'r') as file: data = file.read().replace('\n', '')
            wait_in_content(rf'{os.getcwd()}\logs\{self.username}-{mu}.log', "Login5")

            if "Successful authentication" in data:
                print(f"[{get_time()}]-{color.GREEN}[{self.username}] Successful client authentication{color.RESET_ALL}")
                total_auth()

                path = rf"{current}\AppData\Roaming\Spotify-{self.mu}\prefs"
                path_2 = rf"{current}\\Local\\Spotify-{mu}\\Storage"
                file_exists_(path)

                if config["use_proxy"]:
                        
                    proxy_auth = [
                        'network.proxy.pass="{}"\n'.format(self.proxy.split(":")[1].split("@")[0]),
                        'network.proxy.addr="{}@{}"\n'.format(self.proxy.split('@')[1], config["proxy_protocol"]),
                        "network.proxy.mode=2\n",
                        'network.proxy.user="{}"\n'.format(self.proxy.split(':')[0]),
                        "core.clock_delta=-1\n",
                        #'app.last-launched-version="Spotify/1.1.63.568.gda8cb5ac Windows/10.0 (Aqueduct/v1.2.137-e129b513)"\n',
                        "app.autostart-configured=true\n",
                        'campaign-id="organic"\n',
                        f'storage.last-location="{path_2}"' + "\n",
                        f'autologin.username="{self.username}"\n',
                        f'autologin.canonical_username="{self.username}"\n',
                        "autologin.enabled=false\n"
                    ]

                    with open(path, "w") as e: e.writelines(proxy_auth)
                    print(f"[{get_time()}]-{color.BLUE}[{self.username}] Client re-starting for proxy authentication...  {color.RESET_ALL}")
                    #os.kill(st.pid, signal.SIGTERM)
                    subprocess.check_output("Taskkill /PID %d /F" % st.pid)
                    st = subprocess.Popen([".\Spotify\Spotify.exe", f"--uri=spotify:track:{self.stream_url}", f" --username={self.username}",f" --password={self.password}", f"--mu={mu}", rf"--log-file={os.getcwd()}\logs\{self.username}-{mu}.log"])
                    time.sleep(config["program_sleep_delay"])
                    with open(rf'{os.getcwd()}\logs\{self.username}-{mu}.log', 'r') as file: data = file.read().replace('\n', '')

                    wait_in_content(rf'{os.getcwd()}\logs\{self.username}-{mu}.log', "Login5")


                    if "login5_http_transport_error" in data:
                        print(f"[{get_time()}]-{color.RED}[{self.username}] HTTP transport error while client proxy authenticating | {self.proxy} {color.RESET_ALL}")
                        bad_procces()

                        if config["retry_bad_procces"]:
                            print(f"[{get_time()}]{color.BLUE}-[{self.username}] Retrying the procces...{color.RESET_ALL}")
                            os.kill(st.pid, signal.SIGTERM)
                            path = rf"{current}\AppData\Roaming\Spotify-{self.mu}"
                            path_2 = rf"{current}\AppData\Local\Spotify-{mu}"
                            os.kill(st.pid, signal.SIGTERM)
                            time.sleep(config["program_sleep_delay"])
                            shutil.rmtree(path)
                            shutil.rmtree(path_2)

                    print(f"[{get_time()}]-{color.GREEN}[{self.username}] Proxy connected to client!  {color.RESET_ALL}")

                wait_in_content(rf'{os.getcwd()}\logs\{self.username}-{mu}.log', "Playing music set to 'true")
                print(f"[{get_time()}]-{color.GREEN}[{self.username}] Now Playing: https://open.spotify.com/track/{self.stream_url} | Playtime: {self.song_wait} second(s) {color.RESET_ALL}")
                    
                stream_succes()
                time.sleep(self.song_wait)
                earning_succes()

                print(f"[{get_time()}]-{color.GREEN}[{self.username}] Stream has been sent successfully! {color.RESET_ALL}")

                path = rf"{current}\AppData\Roaming\Spotify-{self.mu}"
                path_2 = rf"{current}\AppData\Local\Spotify-{mu}"
                os.kill(st.pid, signal.SIGTERM)
                time.sleep(config["program_sleep_delay"])
                shutil.rmtree(path)
                shutil.rmtree(path_2)
            
            else:
                print(f"[{get_time()}]-{color.RED}[{self.username}] Error while logining the client | Failed authenticating: login5_invalid_credentials {color.RESET_ALL}")
                bad_procces()

                if config["retry_bad_procces"]:
                    print(f"[{get_time()}]{color.BLUE}-[{self.username}] Retrying the procces...{color.RESET_ALL}")
                    path = rf"{current}\AppData\Roaming\Spotify-{self.mu}"
                    path_2 = rf"{current}\AppData\Local\Spotify-{mu}"
                    os.kill(st.pid, signal.SIGTERM)
                    time.sleep(config["program_sleep_delay"])
                    shutil.rmtree(path)
                    shutil.rmtree(path_2)
        
        except Exception as e:
            print(f"[{get_time()}]-{color.RED}[ERROR] While starting function: {e} {color.RESET_ALL}")
            traceback.print_exc()


# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >