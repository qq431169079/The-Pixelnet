import subprocess
from netaddr import IPNetwork
import platform
from . import *
from . import get_ip
def netmask():
    ip = str(get_ip.get_ip())
    #NOTE: Using different statements because some simple string manipulation is slightly faster than using a module. Also can serve as a contigent if the module isn't there.
    if platform.system() == "Windows":
        proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if ip.encode() in line:
                break
        mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()
        return mask
    """
    elif platform.system() == "Linux":
        subnet = IPNetwork(get_ip.get_ip())
        refined_subnet = subnet.netmask
        print(refined_subnet)
        return refined_subnet
    """
netmask()