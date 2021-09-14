from ydk.models.cisco_ios_xr import Cisco_IOS_XR_snmp_agent_cfg
from ydk.providers import NetconfServiceProvider
from ydk.models.ietf import ietf_interfaces
from ydk.services import CRUDService
from ydk.services import NetconfService, Datastore


if __name__ == '__main__':
    sp_instance = NetconfServiceProvider(address='sbx-iosxr-mgmt.cisco.com',
                                        port=10000,
                                        username='admin',
                                        password='C1sco12345',
                                        protocol='ssh')
    
    crud = CRUDService()

    # Create the top-level container
    snmp = Cisco_IOS_XR_snmp_agent_cfg.Snmp()

    # Create the list instance
    rule = Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule()
    rule.name = 'abc'

    # Instantiate and assign the presence class
    rule.non_stateful = Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful()

    rule.non_stateful.timeout = 3

    # Append the list instance to its parent
    snmp.correlator.rules.rule.append(rule)

    # Call the CRUD create on the top-level snmp object
    # (assuming you have already instantiated the service and provider)
    result = crud.create(sp_instance, snmp)