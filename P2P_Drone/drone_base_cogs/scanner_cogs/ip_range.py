# addressInNetwork and calcDottedNetmask functions courtesy of: https://stackoverflow.com/a/3188535
import netmask_determine
import get_ip
import ipaddress
def ip_range():
    ip = get_ip.get_ip()
    netmask = netmask_determine.netmask()
    ip_prefix = sum([bin(int(x)).count('1') for x in netmask.split('.')])
    