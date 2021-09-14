from ydk.providers import NetconfServiceProvider
from ydk.services import NetconfService, Datastore
from ydk.models.ietf import ietf_interfaces
from ydk.services import CRUDService
from ydk.models.ietf.iana_if_type import SoftwareLoopback

if __name__ == '__main__':
    sp_instance = NetconfServiceProvider(address='192.168.42.69',
                                        port=830,
                                        username='Nsindiso',
                                        password='bulawayo',
                                        protocol='ssh')
    
    crud_service = CRUDService() 

    # Create Top level Container
    intf = ietf_interfaces.Interfaces()

    # Create the list Instance
    intf_config = intf.Interface()
    intf_config.name = "Loopback2"
    # Populate the values of the Global config Object

    intf_config.description = "Interface has been configure by ydk"
    intf_config.type = SoftwareLoopback()
    intf_config.Ipv4.Address.ip = "192.168.1.2"
    intf_config.Ipv4.Address.netmask = "255.255.255.0"

    send_config = crud_service.create(sp_instance, intf)
    print(send_config)