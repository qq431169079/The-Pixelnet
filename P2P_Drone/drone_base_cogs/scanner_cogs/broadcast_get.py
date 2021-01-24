#Only good on Linux for now.
import netifaces
ip_faces_dict = {}
def list_to_dict(a):
    for k, v in [(k, v) for x in a for (k, v) in x.items()]:
        ip_faces_dict[k] = v

def get():
    for iface in netifaces.interfaces():
            if iface == 'lo' or iface.startswith('vbox'):
                continue
            iface_details = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in iface_details.keys():
                netmask_list = iface_details[netifaces.AF_INET]
                list_to_dict(netmask_list)
                broadcast = ip_faces_dict.get("broadcast")
                print(broadcast)
                return broadcast