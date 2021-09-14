from ydk.providers import NetconfServiceProvider
from ydk.services import NetconfService, Datastore
from ydk.models.ietf import ietf_interfaces
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_interfaces_oper
from ydk.models.openconfig import openconfig_bgp
from ydk.models.openconfig import openconfig_bgp_types
from ydk.services import CRUDService


if __name__ == '__main__':
    sp_instance = NetconfServiceProvider(address='192.168.42.69',
                                        port=830,
                                        username='Nsindiso',
                                        password='bulawayo',
                                        protocol='ssh')
    
    crud_service = CRUDService() 

    intf = ietf_interfaces.Interfaces()

    interface_state = crud_service.read(sp_instance,intf)
    
    for int1 in interface_state.interface:
        print(int1.name,"\n", int1.enabled, "\n",int1.type,"\n",int1.description,"\n" )
        print("******************************************************")