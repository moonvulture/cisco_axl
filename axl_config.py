# axl_config.py

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client, Settings, Plugin, xsd
from zeep.transports import Transport
import urllib3

# AXL settings and configurations
class AXLConfig:
    binding_name = "{http://www.cisco.com/AXLAPIService/}AXLAPIBinding"
    axl_address = "https://136.215.78.10:8443/axl/"
    wsdl_file = "/home/michael.s.sullivan50.civ/uc-scripts/scripts/schema/AXLAPI.wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Set up session and transport configurations
        session = Session()
        session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        session.auth = HTTPBasicAuth(username, password)
        transport = Transport(session=session, timeout=5)
        settings = Settings(strict=False, xml_huge_tree=True)
        self.client = Client(wsdl=self.wsdl_file, transport=transport, settings=settings)

    def create_service(self):
        return self.client.create_service(self.binding_name, self.axl_address)

