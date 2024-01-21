import subprocess
import optparse
import re

def get_args():
    try:
        # Create an instance of OptionParser
        parser = optparse.OptionParser()

        # Add options for interface and new MAC address
        parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
        parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

        # Parse the command-line arguments
        (options, arguments) = parser.parse_args()

        # Check if both interface and new MAC address are provided
        if not options.interface:
            parser.error("[-] Please specify an interface, use --help for more info.")
        elif not options.new_mac:
            parser.error("[-] Please specify a MAC address, use --help for more info.")

        return options
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def mac_change(interface, new_mac):
    try:
        # Disable the interface
        subprocess.call(["ifconfig", interface, "down"])

        # Change the MAC address
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

        # Enable the interface
        subprocess.call(["ifconfig", interface, "up"])

        def is_valid_mac(mac):
            # Define the pattern for a valid MAC address
            pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

            # Check if the provided MAC address matches the pattern
            return re.match(pattern, mac) is not None

        if not is_valid_mac(new_mac):
            # Print an error message if the MAC address is invalid
            print("[-] Invalid MAC address format")
            # Handle the error or ask the user to provide a valid MAC address
        else:
            # Disable the interface
            subprocess.call(["ifconfig", interface, "down"])

            # Change the MAC address
            subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

            # Enable the interface
            subprocess.call(["ifconfig", interface, "up"])
            # Print a success message if the MAC address was successfully changed
            print("[+] MAC address was successfully changed to", new_mac)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

options = get_args()

mac_change(options.interface, options.new_mac)
