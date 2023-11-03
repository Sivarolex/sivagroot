# OSPF Area test

# from pyats.topology import loader
# from pyats.aetest import Testcase, test
import re

class OSPFAreaTest(): #Testcase

    # @test
    def test_ospf_areas(self):
        # Load the testbed file
        # testbed = loader.load('testbed.yaml')

        # Retrieve the device
        # router = testbed.devices['router']

        # Connect to the device
        # router.connect()

        # Execute the command to show OSPF areas
        # ospf_area_output = router.execute('show ip ospf')

        # Regular expression pattern to extract OSPF area information
        area_pattern = r'Area (\d+)'
        sample_area = input("Enter area: ")
        example_area_ip = input("Enter Area IP: ")

        # Extract OSPF area data using regular expressions
        # ospf_areas = re.findall(area_pattern, ospf_area_output)

        # Verify the OSPF areas
        expected_areas = ['0.0.0.0', '1.1.1.1']  # Modify this with your expected areas
        if re.match(area_pattern,sample_area):
            for area in expected_areas:
                # assert area in ospf_areas, f"OSPF area {area} is not configured."
                assert area in example_area_ip, f"OSPF area {area} is not configured."
                print("Areas configured Successfully.")
        else:
            print("No Active Areas Found:")


if __name__ == '__main__':
    # import argparse
    # from pyats import topology

    # parser = argparse.ArgumentParser(description="pyATS OSPF Area Test")
    # parser.add_argument("--testbed", dest="testbed", type=topology.loader.load)
    # args, unknown = parser.parse_known_args()

    # aetest.main(testbed=args.testbed)
    my_test = OSPFAreaTest()
    my_test.test_ospf_areas()