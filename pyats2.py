"""L2 VLAN Configuration Test"""
from pyats.topology import loader
from pyats.aetest import Testcase, test
class vlan_config_test():  #(Testcase)
    @test
    def test_vlan_config(self):
        testbed = loader.load('testbed.yaml')
        switch = testbed.devices['switch']
        switch.connect()
        vlan_config_output = switch.execute('show vlan')
        if 'VLAN123' in vlan_config_output and 'VLAN456' in vlan_config_output:
            self.passed('VLANs 123 and 456 are configured correctly.')
        else:
            self.failed('VLANs 123 and 456 are not configured as expected.')
if "__name__" == "__main__":
    import argparse
    from pyats import topology
    parser = argparse.ArgumentParser(description="pyATS vlan config test.")
    parser.add_argument("--testbed",dest='testbed',type=topology.loader.load)
    args, unknown = parser.parse_known_args()
    aetest.main(testbed=args.testbed)
