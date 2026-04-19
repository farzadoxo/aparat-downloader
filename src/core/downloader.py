import requests
import os
from colorama import Fore




class AparatDownloader:
    def __init__(self,url:str,path:str,name:str):
        self.url = url 
        self.name = name
        self.path = path

    # def buffer(path,bin):
    #     os.chdir(path)
    #     with open(f'file.{bin}')


    def download(self):
        req = requests.get(self.url)
        print(Fore.YELLOW+"Requesting URL ...")
        print(Fore.BLUE+"Downloading Video...")
        if req.headers['Content-Type'] == 'video/mp4':
            os.chdir(self.path)
            with open(f"{self.name}.{req.headers['Content-Type'].split('/')[1]}",'ba') as buffer:
                print(Fore.MAGENTA+"Buffering ...")
                buffer.write(req.content)
                print(Fore.GREEN+f"Video successfully downloaded and saved in:",Fore.YELLOW+f"{self.path}")
        else:
            print(Fore.RED+"Download Failed!")



