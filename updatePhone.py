# updatePhone.py

from lxml import etree as ET
from getpass import getpass
from axl_config import AXLConfig
from netaddr import EUI, mac_bare

# AXL credentials
username = 'svc.postmanaxl'
password = getpass("\nEnter AXL Password\n")

# Instantiate AXLConfig
axl_config = AXLConfig(username, password)

# Create a Zeep client and service
service = axl_config.create_service()


#Device Specific Info
mac = '00A5BFC4C678'

phone_name = EUI(mac, dialect=mac_bare)
phone = {
    'name': f'SEP{phone_name}'
}
    # 'description': f'{desc}',
    # 'product': f'{model}',
    # 'model': f'{model}',
    # 'class': 'Phone',
    # 'protocol': 'SIP',
    # 'protocolSide': 'User',
    # 'callingSearchSpaceName': f'{css}',
    # 'devicePoolName': f'{device_pool}',
    # 'commonDeviceConfigName': 'EUR UC Common Device Profile',
    # 'commonPhoneConfigName': f'{phone_config_name}',
    # 'networkLocation': 'Use System Default',
    # 'locationName': 'Hub_None',
    # 'mlppDomainId': '000000',
    # 'mlppIndicationStatus': 'Off',
    # 'preemption': 'Disabled',
    # 'useTrustedRelayPoint': 'Default',
    # 'retryVideoCallAsAudio': 'true',  
    # 'securityProfileName': f'{security_profile}',
    # 'sipProfileName': '- SIP Profile - for TelePresence Endpoint Devices',
    # 'phoneTemplateName': f'{phone_template}',
    # 'useDevicePoolCgpnTransformCss': 'true',
    # 'sendGeoLocation': 'false',
    # 'singleButtonBarge': 'Off',
    # 'joinAcrossLines': 'Off',
    # 'builtInBridgeStatus': 'Off',
    # 'callInfoPrivacyStatus': 'Default',
    # 'hlogStatus': 'Off',
    # 'ignorePresentationIndicators': 'false',
    # 'packetCaptureMode': 'None',
    # 'subscribeCallingSearchSpaceName': f'{css}',
    # 'allowCtiControlFlag': 'false',
    # 'presenceGroupName': 'Standard Presence group',
    # 'unattendedPort': 'false',
    # 'requireDtmfReception': 'false',
    # 'rfc2833Disabled': 'false',
    # 'certificateOperation': 'Install/Upgrade',
    # 'authenticationMode': 'By Null String',
    # 'keySize': '2048',
    # 'keyOrder': 'RSA Only',
    # 'upgradeFinishTime': '2023:09:06:12:00',
    # 'deviceMobilityMode': 'Default',
    # 'lines': {
    #     'line': [
    #         {
    #             'index': 1,
    #             'display': f'{line_desc}',
    #             'displayAscii': f'{line_desc}',
    #             'maxNumCalls': '2',
    #             'busyTrigger': '2',
    #             'dirn': {
    #                 'pattern': f'{dirn}',
    #                 'routePartitionName': 'PT_Routine'
    #             }
    #         }
    #     ]
    # },
    # 'remoteDevice': 'false',
    # 'dndOption': 'Ringer Off',
    # 'dndStatus': 'false',
    # 'isActive': 'true',
    # 'isDualMode': 'false',
    # 'phoneSuite': 'Default',
    # 'phoneServiceDisplay': 'Default',
    # 'isProtected': 'false',
    # 'mtpRequired': 'false',
    # 'mtpPreferedCodec': '711ulaw',
    # 'outboundCallRollover': 'No Rollover',
    # 'hotlineDevice': 'false',
    # 'alwaysUsePrimeLine': 'Default',
    # 'alwaysUsePrimeLineForVoiceMessage': 'Default',
    # 'deviceTrustMode': 'Not Trusted',
    # 'AllowPresentationSharingUsingBfcp': 'false',
    # 'allowiXApplicableMedia': 'false',
    # 'useDevicePoolCgpnIngressDN': 'true',
    # 'enableCallRoutingToRdWhenNoneIsActive': 'false',
    # 'enableExtensionMobility': 'false',
    # 'subscribeCallingSearchSpaceName': f'{css}'

#vendor config must be completed or will be overwritten by defaults
webAccess = ET.Element('webAccess')  
webAccess.text = '2'

sshAccess = ET.Element('sshAccess')
sshAccess.text = '1'

DefaultCallProtocol = ET.Element('DefaultCallProtocol')
DefaultCallProtocol.text = '0'

multipointMode = ET.Element('multipointMode')
multipointMode.text = '1'

TelnetMode = ET.Element('TelnetMode')
TelnetMode.text = 'Off'

MicUnmuteOnDisconnectMode = ET.Element('MicUnmuteOnDisconnectMode')
MicUnmuteOnDisconnectMode.text = 'On'

CallLoggingMode = ET.Element('CallLoggingMode')
CallLoggingMode.text = 'On'

DefaultVolume = ET.Element('DefaultVolume')
DefaultVolume.text = '50'

MaxTotalDownstreamRate = ET.Element('MaxTotalDownstreamRate')
MaxTotalDownstreamRate.text = '3072'

MaxTotalUpstreamRate = ET.Element('MaxTotalUpstreamRate')
MaxTotalUpstreamRate.text = '3072'

WifiAllowed = ET.Element('WifiAllowed')
WifiAllowed.text = 'Off'

WakeupOnMotionDetection = ET.Element('WakeupOnMotionDetection')
WakeupOnMotionDetection.text = 'Off'

AccessibilityCallNotification = ET.Element('AccessibilityCallNotification')
AccessibilityCallNotification.text = 'Default'

SystemName = ET.Element('SystemName')
SystemName.text = f'{line_desc}'

SettingsMenuMode = ET.Element('SettingsMenuMode')
SettingsMenuMode.text = 'Locked'

configurationControl = ET.Element('configurationControl')
configurationControl.text = 'CUCM'

UIFeaturesCallJoinWebex = ET.Element('UIFeaturesCallJoinWebex')
UIFeaturesCallJoinWebex.text = 'Hidden'

FarEndCameraControlGroup = ET.Element('FarEndCameraControlGroup')

FarEndCameraControlMode = ET.SubElement(FarEndCameraControlGroup, 'FarEndCameraControlMode')
FarEndCameraControlMode.text = 'Off'

FarEndCameraControlSignalCapability = ET.SubElement(FarEndCameraControlGroup, 'FarEndCameraControlSignalCapability')
FarEndCameraControlSignalCapability.text = 'Off'

FacilityServiceGroup = ET.Element('FacilityServiceGroup')

FacilityServiceType = ET.SubElement(FacilityServiceGroup, 'FacilityServiceType')
FacilityServiceType.text = 'Helpdesk'

FacilityServiceCallType = ET.SubElement(FacilityServiceGroup, 'FacilityServiceCallType')
FacilityServiceCallType.text = 'Video'

StandbyGroup = ET.Element('StandbyGroup')

StandbyMode = ET.SubElement(StandbyGroup, 'StandbyMode')
StandbyMode.text = 'On'

StandbyDelay = ET.SubElement(StandbyGroup, 'StandbyDelay')
StandbyDelay.text = '10'

StandbyAction = ET.SubElement(StandbyGroup, 'StandbyAction')
StandbyAction.text = 'PrivacyPosition'

SerialPortGroup = ET.Element('SerialPortGroup')

SerialPortMode = ET.SubElement(SerialPortGroup, 'SerialPortMode')
SerialPortMode.text = 'On'

SerialPortLoginRequired = ET.SubElement(SerialPortGroup, 'SerialPortLoginRequired')
SerialPortLoginRequired.text = 'Off'

AdminLoginDetails = ET.Element('AdminLoginDetails')

adminUserId = ET.SubElement(AdminLoginDetails, 'adminUserId')
adminUserId.text = 'svc_rcce_euccmadmin'

adminPassword = ET.SubElement(AdminLoginDetails, 'adminPassword')
adminPassword.text = f'{password}'

Osd = ET.Element('Osd')

TodaysBookings = ET.SubElement(Osd, 'TodaysBookings')
TodaysBookings.text = 'Off'

Proximity = ET.Element('Proximity')

ProximityMode = ET.SubElement(Proximity, 'ProximityMode')
ProximityMode.text = 'Off'

ProximityCallControl = ET.SubElement(Proximity, 'ProximityCallControl')
ProximityCallControl.text = 'Disabled'

ProximityContentShareFromClients = ET.SubElement(Proximity, 'ProximityContentShareFromClients')
ProximityContentShareFromClients.text = 'Disabled'

ProximityContentShareToClients = ET.SubElement(Proximity, 'ProximityContentShareToClients')
ProximityContentShareToClients.text = 'Disabled'

LDAPUserManagement = ET.Element('LDAPUserManagement')

LDAPMode = ET.SubElement(LDAPUserManagement, 'LDAPMode')
LDAPMode.text = 'On'

LDAPServerAddress = ET.SubElement(LDAPUserManagement, 'LDAPServerAddress')
LDAPServerAddress.text = 'CLAYW059AAA1EU1.eur.ds.army.mil'

LDAPServerPort = ET.SubElement(LDAPUserManagement, 'LDAPServerPort')
LDAPServerPort.text = '636'

LDAPBaseDN = ET.SubElement(LDAPUserManagement, 'LDAPBaseDN')
LDAPBaseDN.text = 'OU=Service-Accounts,OU=Administration,OU=CiscoUC,OU=Enterprise Services,DC=EUR,DC=DS,DC=ARMY,DC=MIL'

LDAPEncryption = ET.SubElement(LDAPUserManagement, 'LDAPEncryption')
LDAPEncryption.text = 'LDAPS'

LDAPMinimumTLSVersion = ET.SubElement(LDAPUserManagement, 'LDAPMinimumTLSVersion')
LDAPMinimumTLSVersion.text = 'TLSv1.0'

LDAPVerifyServerCertificate = ET.SubElement(LDAPUserManagement, 'LDAPVerifyServerCertificate')
LDAPVerifyServerCertificate.text = 'Off'

LDAPAdminGroup = ET.SubElement(LDAPUserManagement, 'LDAPAdminGroup')
LDAPAdminGroup.text = 'CN=RCC-EUR UC Admin,OU=Groups,OU=CiscoUC,OU=Enterprise Services,DC=EUR,DC=DS,DC=ARMY,DC=MIL'

vendorConfig = []
vendorConfig.append(webAccess)
vendorConfig.append(sshAccess)
vendorConfig.append(DefaultCallProtocol)
vendorConfig.append(multipointMode)
vendorConfig.append(TelnetMode)
vendorConfig.append(MicUnmuteOnDisconnectMode)
vendorConfig.append(CallLoggingMode)
vendorConfig.append(DefaultVolume)
vendorConfig.append(MaxTotalDownstreamRate)
vendorConfig.append(MaxTotalUpstreamRate)
vendorConfig.append(WifiAllowed)
vendorConfig.append(WakeupOnMotionDetection)
vendorConfig.append(AccessibilityCallNotification)
vendorConfig.append(SystemName)
vendorConfig.append(SettingsMenuMode)
vendorConfig.append(configurationControl)
vendorConfig.append(UIFeaturesCallJoinWebex)
vendorConfig.append(FarEndCameraControlGroup)
vendorConfig.append(FacilityServiceGroup)
vendorConfig.append(StandbyGroup)
vendorConfig.append(SerialPortGroup)
vendorConfig.append(AdminLoginDetails)
vendorConfig.append(Osd)
vendorConfig.append(Proximity)
vendorConfig.append(LDAPUserManagement)
xvcType = axl_config.client.get_type('ns0:XVendorConfig')

phone['vendorConfig'] = xvcType(vendorConfig)

def update_phone():
    try:
        resp = service.updatePhone(**phone)
    except Fault as err:
        print(f'Zeep error: updatePhone: {err}')
        sys.exit(1)

    print( '\nupdatePhone response:\n' )
    print( resp,'\n' )

if __name__ == '__main__':
    update_phone()

