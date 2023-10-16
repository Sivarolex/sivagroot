"""L3 Routing Configuration Test"""
from pyats.topology import loader
from pyats.aetest import Testcase, test
from pyats.topology import loader
from pyats.aetest import Testcase, test

class RoutingConfigurationTest(Testcase):

    @test
    def test_routing_configuration(self):
        # Load the testbed file
        testbed = loader.load('testbed.yaml')

        # Retrieve the device
        router = testbed.devices['router']

        # Connect to the device
        router.connect()

        # Execute the command to show routing table
        routing_table_output = router.execute('show ip route')

        # Validate routing configuration using regular expressions
        if '192.168.10.0/24' in routing_table_output and '10.1.1.0/24' in routing_table_output:
            self.passed('Routing configuration is correct.')
        else:
            self.failed('Routing configuration is not as expected.')

if __name__ == '__main__':
    import argparse
    from pyats import topology

    parser = argparse.ArgumentParser(description="pyATS Routing Configuration Test")
    parser.add_argument("--testbed", dest="testbed", type=topology.loader.load)
    args, unknown = parser.parse_known_args()

    aetest.main(testbed=args.testbed)
