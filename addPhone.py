# addphone.py

# Import necessary libraries 
import yaml
import sys
from lxml import etree as ET
from getpass import getpass
from axl_config import AXLConfig
from zeep.exceptions import Fault
from netaddr import EUI, mac_bare


# Load the configuration from YAML
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Function to add a line using AXL service
def add_line(service, line):
    try:
        resp = service.addLine(line)
    except Fault as err:
        print( f'Zeep error: addLine:', err)
        sys.exit(1)

    print( '\naddLine response:\n' )
    print( resp,'\n' )

# Function to add a device using AXL service    
def add_phone(service, phone):
    try:
        resp = service.addPhone(phone)
    except Fault as err:
        print(f'Zeep error: addPhone:', err)
        sys.exit(1)

    print( '\naddPhone response:\n' )
    print( resp,'\n' )

if __name__ == '__main__':
    # Get AXL credentials from the user
    username = input("Enter your username: ")
    password = getpass("\nEnter AXL Password\n")

    # Instantiate AXLConfig
    axl_config = AXLConfig(username, password)

    # Create a Zeep client and service using the AXL configuration
    service = axl_config.create_service()

    phone_config = config.get("phone", {})
    mac = phone_config.get("mac")
    desc = phone_config.get("desc")
    model = phone_config.get("model")
    css = phone_config.get("css")
    device_pool = phone_config.get("device_pool")
    phone_config_name = phone_config.get("phone_config_name")
    security_profile = phone_config.get("security_profile")
    sip_profile = phone_config.get("sip_profile")
    common_device_profile = phone_config.get("common_device_profile")
    phone_template = phone_config.get("phone_template")
    line_desc = phone_config.get("line_desc")
    dirn = phone_config.get("dirn")
    admin_pass = phone_config.get("admin_pass")
    admin_user = phone_config.get("admin_user")
    ldap_server = phone_config.get("ldap_server")
    ldap_baseDN = phone_config.get("ldap_baseDN")
    ldap_adminGroup = phone_config.get("ldap_adminGroup")

    # Define line information
    line = {
        'pattern': f'{dirn}',
        'description': f'{line_desc}',
        'usage': 'Device',
        'alertingName': f'{line_desc}',
        'asciiAlertingNam': f'{line_desc}',
        'callingSearchSpaceName': f'{css}',
        'routePartitionName': 'PT_Routine'
    }

    # Define phone information
    phone_name = EUI(mac, dialect=mac_bare)
    phone = {
        'name': f'SEP{phone_name}',
        'description': desc,
        'product': model,
        'model': model,
        'class': 'Phone',
        'protocol': 'SIP',
        'protocolSide': 'User',
        'callingSearchSpaceName': css,
        'devicePoolName': device_pool,
        'commonDeviceConfigName': common_device_profile,
        'commonPhoneConfigName': phone_config_name,
        'networkLocation': 'Use System Default',
        'locationName': 'Hub_None',
        'mlppDomainId': '000000',
        'mlppIndicationStatus': 'Off',
        'preemption': 'Disabled',
        'useTrustedRelayPoint': 'Default',
        'retryVideoCallAsAudio': 'true',  
        'securityProfileName': security_profile,
        'sipProfileName': sip_profile,
        'phoneTemplateName': phone_template,
        'useDevicePoolCgpnTransformCss': 'true',
        'sendGeoLocation': 'false',
        'singleButtonBarge': 'Off',
        'joinAcrossLines': 'Off',
        'builtInBridgeStatus': 'Off',
        'callInfoPrivacyStatus': 'Default',
        'hlogStatus': 'Off',
        'ignorePresentationIndicators': 'false',
        'packetCaptureMode': 'None',
        'subscribeCallingSearchSpaceName': css,
        'allowCtiControlFlag': 'false',
        'presenceGroupName': 'Standard Presence group',
        'unattendedPort': 'false',
        'requireDtmfReception': 'false',
        'rfc2833Disabled': 'false',
        'certificateOperation': 'Install/Upgrade',
        'authenticationMode': 'By Null String',
        'keySize': '2048',
        'keyOrder': 'RSA Only',
        'upgradeFinishTime': '2023:09:06:12:00',
        'deviceMobilityMode': 'Default',
        'lines': {
            'line': [
                {
                    'index': 1,
                    'display': line_desc,
                    'displayAscii': line_desc,
                    'maxNumCalls': '2',
                    'busyTrigger': '2',
                    'dirn': {
                        'pattern': dirn,
                        'routePartitionName': 'PT_Routine'
                    }
                }
            ]
        },
        'remoteDevice': 'false',
        'dndOption': 'Ringer Off',
        'dndStatus': 'false',
        'isActive': 'true',
        'isDualMode': 'false',
        'phoneSuite': 'Default',
        'phoneServiceDisplay': 'Default',
        'isProtected': 'false',
        'mtpRequired': 'false',
        'mtpPreferedCodec': '711ulaw',
        'outboundCallRollover': 'No Rollover',
        'hotlineDevice': 'false',
        'alwaysUsePrimeLine': 'Default',
        'alwaysUsePrimeLineForVoiceMessage': 'Default',
        'deviceTrustMode': 'Not Trusted',
        'AllowPresentationSharingUsingBfcp': 'false',
        'allowiXApplicableMedia': 'false',
        'useDevicePoolCgpnIngressDN': 'true',
        'enableCallRoutingToRdWhenNoneIsActive': 'false',
        'enableExtensionMobility': 'false',
        'subscribeCallingSearchSpaceName': css
    }

    # Define Vendor Config
    webAccess = ET.Element('webAccess')  
    webAccess.text = '2'

    sshAccess = ET.Element('sshAccess')
    sshAccess.text = '1'

    SystemName = ET.Element('SystemName')
    SystemName.text = line_desc

    SettingsMenuMode = ET.Element('SettingsMenuMode')
    SettingsMenuMode.text = 'Locked'

    configurationControl = ET.Element('configurationControl')
    configurationControl.text = 'CUCM'

    UIFeaturesCallJoinWebex = ET.Element('UIFeaturesCallJoinWebex')
    UIFeaturesCallJoinWebex.text = 'Hidden'

    AdminLoginDetails = ET.Element('AdminLoginDetails')

    adminUserId = ET.SubElement(AdminLoginDetails, 'adminUserId')
    adminUserId.text = admin_user

    adminPassword = ET.SubElement(AdminLoginDetails, 'adminPassword')
    adminPassword.text = admin_pass

    LDAPUserManagement = ET.Element('LDAPUserManagement')

    LDAPMode = ET.SubElement(LDAPUserManagement, 'LDAPMode')
    LDAPMode.text = 'On'

    LDAPServerAddress = ET.SubElement(LDAPUserManagement, 'LDAPServerAddress')
    LDAPServerAddress.text = ldap_server

    LDAPServerPort = ET.SubElement(LDAPUserManagement, 'LDAPServerPort')
    LDAPServerPort.text = '636'

    LDAPBaseDN = ET.SubElement(LDAPUserManagement, 'LDAPBaseDN')
    LDAPBaseDN.text = ldap_baseDN

    LDAPEncryption = ET.SubElement(LDAPUserManagement, 'LDAPEncryption')
    LDAPEncryption.text = 'LDAPS'

    LDAPMinimumTLSVersion = ET.SubElement(LDAPUserManagement, 'LDAPMinimumTLSVersion')
    LDAPMinimumTLSVersion.text = 'TLSv1.0'

    LDAPVerifyServerCertificate = ET.SubElement(LDAPUserManagement, 'LDAPVerifyServerCertificate')
    LDAPVerifyServerCertificate.text = 'Off'

    LDAPAdminGroup = ET.SubElement(LDAPUserManagement, 'LDAPAdminGroup')
    LDAPAdminGroup.text = ldap_adminGroup

    vendorConfig = []
    vendorConfig.append(webAccess)
    vendorConfig.append(sshAccess)
    vendorConfig.append(SystemName)
    vendorConfig.append(SettingsMenuMode)
    vendorConfig.append(configurationControl)
    vendorConfig.append(LDAPUserManagement)
    vendorConfig.append(AdminLoginDetails)
    xvcType = axl_config.client.get_type('ns0:XVendorConfig')

    phone['vendorConfig'] = xvcType(vendorConfig)

    # Call the functions to add line and phone
    # add_line(service, line)
    add_phone(service, phone)

