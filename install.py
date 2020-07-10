# Installer for the Hubitat device extension

from weecfg.extension import ExtensionInstaller

def loader():
    return HubitatInstaller()

class HubitatInstaller(ExtensionInstaller):
    def __init__(self):
        super(HubitatInstaller, self).__init__(
            version="1.0",
            name='hubitat',
            description='Post loop data to a Hubitat device',
            restful_services='user.hubitat.Hubitat',
            config={
                'StdRESTful': {
                    'Hubitat': {
                        'server_url': 'hubURL_from_hubitat_device',
                        'post_interval': '60',
                        'log_success': False}}},
            files=[('bin/user', ['bin/user/hubitat.py'])]
        )
