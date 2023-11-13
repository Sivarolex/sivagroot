# ARP Table test
# from pyats.topology import loader
# from pyats.aetest import Testcase, test
import re

class ARPTableTest(): #Testcase

    # @test
    def test_arp_table(self):
        # Load the testbed file
        # testbed = loader.load('testbed.yaml')

        # Retrieve the device
        # router = testbed.devices['router']

        # Connect to the device
        # router.connect()

        # Execute the command to show ARP table
        # arp_table_output = router.execute('show arp')

        # Regular expression pattern to extract ARP table entries
        arp_entry_pattern = r'(\d+\.\d+\.\d+\.\d+)\s+([\w:]+)\s+(\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+([\w\-]+)'

        # Extract ARP table data using regular expressions
        # arp_entries = re.findall(arp_entry_pattern, arp_table_output)

        # Verify ARP entries (you can customize the expected entries)
        expected_entries = [
            ('192.168.1.1', '00:11:22:33:44:55', 'ARPA', 'Vlan1'),
            ('192.168.1.2', 'AA:BB:CC:DD:EE:FF', 'ARPA', 'Vlan1')
        ]

        # for entry in expected_entries:
        #     assert entry in arp_entries, f"Expected ARP entry {entry} not found in the ARP table."

if __name__ == '__main__':
    # import argparse
    # from pyats import topology

    # parser = argparse.ArgumentParser(description="pyATS ARP Table Test")
    # parser.add_argument("--testbed", dest="testbed", type=topology.loader.load)
    # args, unknown = parser.parse_known_args()

    # aetest.main(testbed=args.testbed)
    my_test = ARPTableTest()
    my_test.test_arp_table()

