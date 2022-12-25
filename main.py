# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- > 

from src import spotify_streamer, color, get_uuid, spotify, title_thread
import threading, os, yaml, random, traceback, time, os, shutil, sys, requests

from src.misc import get_time


with open('./config/config.yml') as f: config = yaml.load(f, Loader=yaml.FullLoader)
tokens = open("./config/tokens.txt", "+r", encoding="utf-8").read().splitlines()
proxies = open("./config/proxies.txt", "+r", encoding="utf-8").read().splitlines()

view_count = config["view_count"]
client_count = config["client_thread"]
temp_token_count = tokens.copy()

os.system("cls") if os.name == "nt" else os.system("clear")


def worker(process_count) -> None:

    global view_count
    global tokens
    global temp_token_count
    global client_count

    while view_count > 0:
        tokens = open("./config/tokens.txt", "+r", encoding="utf-8").read().splitlines()

        try:


            if len(temp_token_count) <= client_count:
                temp_token_count = tokens.copy()


            random_token = random.choice(temp_token_count)
            temp_token_count.remove(random_token)
            

            view_count -= 1
            song_id = random.choice(config["song_link"]).split("/")[4].split("?")[0]
            

            username = random_token.split(":")[0]
            password = random_token.split(":")[1]
            
            
            q = spotify_streamer(song_id, username, password, process_count, random.choice(proxies) if config["use_proxy"] else None).send_stream()
        
        except KeyboardInterrupt:
            os.system(f"taskkill /f /im ./Spotify/spotify.exe")


def starter() -> None:
    threading.Thread(target=title_thread).start()
    print(rf"""{color.GREEN}
                                                                    v2
  _________            ________                       by CryonicX :)
 /   _____/_____   ____\______ \   ____  ______ ______
 \_____  \\____ \ /  _ \|    |  \ /  _ \/  ___//  ___/
 /        \  |_> >  <_> )    `   (  <_> )___ \ \___ \ 
/_______  /   __/ \____/_______  /\____/____  >____  >
        \/|__|                 \/           \/     \/ 


[INFO] = Running on {color.RESET_ALL}{config['client_thread']}{color.GREEN} threads.
[INFO] = Loaded on {color.RESET_ALL}{len(proxies)}{color.GREEN} proxies.
[INFO] = Loaded on {color.RESET_ALL}{len(tokens)}{color.GREEN} accounts.
[INFO] = Track playtime Between {color.RESET_ALL}{config['min_wait_max_wait'][0]}{color.GREEN}-{color.RESET_ALL}{config['min_wait_max_wait'][1]}{color.GREEN} second(s).
[INFO] = Track scraped {color.RESET_ALL}{config['song_link']}{color.GREEN}
[INFO] = Proxy {color.RESET_ALL}{'True' if config['use_proxy'] else 'False'}{color.GREEN}
[INFO] = View count {color.RESET_ALL}{config['view_count']}{color.GREEN}

presss any key to start software....
{color.RESET_ALL}
""")
    input("")
    os.system("mode 150, 30")
    os.system("cls") if os.name == "nt" else os.system("clear")


    threads = []
    for process_count in range(1, client_count + 1):
        time.sleep(config["program_sleep_delay"])
        t = threading.Thread(target=worker, args=(process_count,))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()



if __name__ == "__main__":
    if os.name != "nt":
        print(f"{color.RED}[OS] YOUR OPARATING SYSTEM MUST BE WINDOWS {color.RESET_ALL}")
        time.sleep(99)
        sys.exit()
    
    folder = f"{os.getcwd()}\logs"
    username = os.environ.get("USERNAME")
    folder_2 = rf"C:\Users\{username}\AppData\Roaming"

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for filename in os.listdir(folder_2):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                if filename.startswith("Spotify-"): 
                    print(file_path)
                    os.unlink(file_path)
            elif os.path.isdir(file_path):
                if filename.startswith("Spotify-"):
                    print(file_path)
                    shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    if config["use_proxy"]:
        if len(proxies) < 1:
            print(f"{color.RED} ./config/proxies.txt is empty. {color.RESET_ALL}")
            input("...")
            quit()

    if config["use_proxy"]:
        if "@" not in random.choice(proxies):
            print(f"{color.RED}[PROXY_CONNECTION_ERROR] YOUR PROXY TYPE MUST BE user:pass@ip:port {color.RESET_ALL}")
            time.sleep(999)
            sys.exit()

    '''
    check = check_license(config["program_license"], get_uuid())
    if check[0]:
        print(f"{color.GREEN}[+] License correct program starting... {color.RESET_ALL}")
        try:
            os.system("cls") if os.name == "nt" else os.system("clear")
            starter()
        except:
            print(f"{color.RED}[-] Error while starting program. {color.RESET_ALL}")
            traceback.print_exc()
            input("...")
    else:
        print(f"{color.RED}[-] {check[1]} {color.RESET_ALL}")
        input("...")

    '''

    starter()

# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >