# addressInNetwork and calcDottedNetmask functions courtesy of: https://stackoverflow.com/a/3188535
import netmask_determine
import get_ip
from netaddr import IPNetwork
def ip_range():
    ip = get_ip.get_ip()
    netmask = netmask_determine.netmask()
    ip_prefix = "/" + str(sum([bin(int(x)).count('1') for x in netmask.split('.')]))
    suffixed_ip = ip + ip_prefix
    print(suffixed_ip)
    netaddr_ip = IPNetwork(suffixed_ip)
    max_range = netaddr_ip.size
    return int(max_range)
ip_range()