import subprocess
import platform
import netifaces
from . import *
from . import get_ip
def netmask():
    ip = str(get_ip.get_ip())
    if platform.system() == "Windows":
        proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if ip.encode() in line:
                break
        mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()
        return mask
    elif platform.system() == "Linux":
        print(netifaces.interfaces())
        for iface in netifaces.interfaces():
            if iface == 'lo' or iface.startswith('vbox'):
                continue
            iface_details = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in iface_details:
                print (iface_details[netifaces.AF_INET])
netmask()