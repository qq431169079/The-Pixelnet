import subprocess
import platform
try:
    import netifaces
except:
    pass
from . import *
from . import get_ip
ip_faces_dict = {}
def list_to_dict(a):
    for k, v in [(k, v) for x in a for (k, v) in x.items()]:
        ip_faces_dict[k] = v
def netmask():
    ip = str(get_ip.get_ip())
    if platform.system() == "Windows":
        proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if ip.encode() in line:
                break
        mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()
        for iface in netifaces.interfaces():
            if iface == 'lo' or iface.startswith('vbox'):
                continue
            iface_details = netifaces.ifaddresses(iface)
        return mask
    elif platform.system() == "Linux":
        for iface in netifaces.interfaces():
            if iface == 'lo' or iface.startswith('vbox'):
                continue
            iface_details = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in iface_details.keys():
                print (iface_details[netifaces.AF_INET])
                netmask_list = iface_details[netifaces.AF_INET]
                list_to_dict(netmask_list)
                netmask = ip_faces_dict.get("netmask")
                print(netmask)
                return netmask