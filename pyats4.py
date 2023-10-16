"""OSPF Route Validation Test"""

import re
# from pyats.topology import loader
# from pyats.aetest import Testcase, test

class OSPFRouteValidationTest():  #Testcase

    #@test
    def test_ospf_route_validation(self):
        # # Load the testbed file
        # testbed = loader.load('testbed.yaml')

        # # Retrieve the device
        # router = testbed.devices['router']

        # # Connect to the device
        # router.connect()

        # Execute the command to show OSPF routes
        ospf_route_output = """10.1.0.0/24 [110/2] via 10.0.0.2 00:03:13 FastEthernet0/0"""    #router.execute('show ip ospf route')

        # Regular expression pattern to extract OSPF routes
        route_pattern = r'(\d+\.\d+\.\d+\.\d+)\s+/\d+\s+\S+\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\:\d+\:\d+)\s+\S'

        # Extract OSPF route information using regular expressions
        ospf_routes = re.findall(route_pattern, ospf_route_output)

        # Validate OSPF routes
        for route in ospf_routes:
            if route[0] == '192.168.10.0' and route[3] == '10.1.1.1' and route[5] == 'FastEthernet0/0':
                print("OSPF route to {route[0]} is correct.")
                #self.passed(f'OSPF route to {route[0]} is correct.')
            else:
                print("OSPF route to {route[0]} is not as expected.")
                #self.failed(f'OSPF route to {route[0]} is not as expected.')

if __name__ == '__main__':
    # import argparse
    # from pyats import topology

    # parser = argparse.ArgumentParser(description="pyATS OSPF Route Validation Test")
    # parser.add_argument("--testbed", dest="testbed", type=topology.loader.load)
    # args, unknown = parser.parse_known_args()

    # aetest.main(testbed=args.testbed)
    my_instance = OSPFRouteValidationTest()
    my_instance.test_ospf_route_validation()