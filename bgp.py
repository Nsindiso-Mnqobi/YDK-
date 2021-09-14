from ydk.providers import NetconfServiceProviderfrom 
ydk.models.openconfig import openconfig_bgp
from ydk.models.openconfig import openconfig_bgp_types


sp_instance = NetconfServiceProvider(address='10.0.0.1',
                                     port=830,
                                     username='test',
                                     password='test',
                                     protocol='ssh')