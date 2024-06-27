
import os

print("""

╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
| ████████▄  ████████▄   ▄██████▄     ▄████████ | CREATE : ALFAZ    |
| ███   ▀███ ███   ▀███ ███    ███   ███    ███ |                   |
| ███    ███ ███    ███ ███    ███   ███    █▀  |                   |
| ███    ███ ███    ███ ███    ███   ███        |                   |
| ███    ███ ███    ███ ███    ███ ▀███████████ |                   |
| ███    ███ ███    ███ ███    ███          ███ |                   |
| ███   ▄███ ███   ▄███ ███    ███    ▄█    ███ |                   |
| ████████▀  ████████▀   ▀██████▀   ▄████████▀  | BY: ALFAZINFOSEC  | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
                                             
""") 

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt update && apt upgrade")
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install python")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")
    os.system("install mechanize")
    os.system("pip install wget")
    os.system("pip install requests")
    os.system("pip install times")
    os.system("pip install ipaddress")
    os.system("pip install bs4")
    os.system("apt update && apt upgrade")

elif c == "1":
    os.system("apt update && apt upgrade")
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip install python")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
    os.system("pip3 install mechanize")
    os.system("pip3 install wget")
    os.system("pip3 install requests")
    os.system("pip3 install times")
    os.system("pip3 install ipaddress")
    os.system("pip3 install bs4")
    
  
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")
