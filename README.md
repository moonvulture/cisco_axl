# AXL Phone Adder

This script (`addPhone.py`) is a utility tool for adding phone devices to a Cisco Unified Communications Manager (CUCM) using the AXL (Administrative XML) API. It provides a convenient way to automate the creation of phone devices in a CUCM environment.

## Prerequisites

- Python 3.x
- Required Python packages: `lxml`, `getpass`, `netaddr`

## Setup

1. Clone or download the repository.

2. Install the required Python packages:
   ```bash
   pip install lxml netaddr

3. Update the following variables in addPhone.py to match your specific environment:
   - AXL credentials (username and password)
   - Device-specific information (MAC address, description, model, etc.)
   - Vendor-specific configurations (if applicable)

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing addPhone.py.

3. Run the script:
    ```bash
    python addPhone.py

4. Enter your AXL username and password when prompted.

5. The script will connect to the CUCM using the AXL API and add the phone device using the provided information.

## Important Notes

The axl_config.py module is required for the script to function. Do not modify or remove it.

Ensure that your environment meets the prerequisites before running the script.

Make sure to review and update the device-specific information in addPhone.py before running the script.