from ydk.providers import NetconfServiceProvider
from ydk.models.ietf import ietf_interfaces
from ydk.services import CRUDService
from ydk.services import NetconfService, Datastore


if __name__ == '__main__':
    sp_instance = NetconfServiceProvider(address='192.168.42.69',
                                        port=830,
                                        username='Nsindiso',
                                        password='bulawayo',
                                        protocol='ssh')
    
    netconf_service = NetconfService() 

    config = ietf_interfaces.Interfaces()

    config.interface.name = "Loopback1"
    config.interface.description = "YDK Config Interface"
    config.interface.type =  "iana-if-type:softwareLoopback"
    config.interface.enabled = True
    config.Interface.Ipv4.Address.ip = "10.10.1.1"
    config.Interface.Ipv4.Address.subnet = "255.255.255.0"
    
    netconf_service.get_config(sp_instance, Datastore.running ,config)
   

