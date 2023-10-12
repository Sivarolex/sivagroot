"""OSPF Neighbor Count Test Using pyATS"""
# from pyats.topology import loader
# from pyats.aetest import Testcase, test
import re

class OSPFNeighborCountTest():        #or Testcase

    # @test
    def test_ospf_neighbor_count(self):
        # Load the testbed file
        #testbed = loader.load('testbed.yaml')

        # Retrieve the device
        #router = testbed.devices['router']

        # Connect to the device
        #router.connect()

        # Execute the command to show OSPF neighbors
        #ospf_neighbor_output = router.execute('show ip ospf neighbor')

        # Regular expression pattern to extract OSPF neighbor information
        #neighbor_pattern = r'Neighbor ID\s+Pri\s+State\s+Dead Time\s+Address\s+Interface'
        my_pattern="192.168.1.1      1   FULL/DR         32    10.0.0.1        GigabitEthernet0/0"
        neighbor_data_pattern = r'(\d+\.\d+\.\d+\.\d+)\s+(\d+)\s+(\S+)\s+\d+\s+(\d+\.\d+\.\d+\.\d+)\s+(\S+)'

        # Extract neighbor data using regular expressions
        ospf_neighbors = re.findall(neighbor_data_pattern, my_pattern)  #ospf_neighbor_output

        # Count the number of OSPF neighbors
        neighbor_count = len(ospf_neighbors)

        # Verify the neighbor count is as expected (you can change this value)
        expected_neighbor_count = 1  # Change this to your expected neighbor count
        assert neighbor_count == expected_neighbor_count, f"Expected {expected_neighbor_count} OSPF neighbors but found {neighbor_count}"
        if True:
            print("neighbor count is "+str(neighbor_count)+" and  Expected neighbor count is "+str(expected_neighbor_count)+".")
if __name__ == '__main__':
    # import argparse
    # from pyats import topology

    # parser = argparse.ArgumentParser(description="pyATS OSPF Neighbor Count Test")
    # parser.add_argument("--testbed", dest="testbed", type=topology.loader.load)
    # args, unknown = parser.parse_known_args()

    # aetest.main(testbed=args.testbed)
    my_instance = OSPFNeighborCountTest()
    my_instance.test_ospf_neighbor_count()


    #pyats command : python ospf_neighbor_count_test.py --testbed your_testbed.yaml