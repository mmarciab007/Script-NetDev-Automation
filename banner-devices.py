import json
from scrapli.driver.core import IOSXEDriver # type: ignore

devices_list = [
    {
        "host" : "192.168.0.23",
        "auth_username": "python",
        "auth_password": "python",
        "auth_strict_key": False,
        "ssh_config_file": True,
        "transport": "paramiko",
        "transport_options": {
        "paramiko": {
            "hostkey_verify": False,
            "disabled_algorithms": {
                "pubkeys": []  # Permite ssh-rsa
                }
            }
        }
    },
    {
        "host" : "192.168.0.25",
        "auth_username": "python",
        "auth_password": "python",
        "auth_strict_key": False,
        "ssh_config_file": True,
        "transport": "paramiko",
        "transport_options": {
        "paramiko": {
            "hostkey_verify": False,
            "disabled_algorithms": {
                "pubkeys": []  # Permite ssh-rsa
                }
            }
        }
    },
]

for devices in devices_list:
        with IOSXEDriver(**devices) as conn:
                banner = ["banner motd #Unauthorized access to this device is prohibited!#"]
                conn.send_configs(banner)
                res = conn.send_command("sh run | include banner")
                print(res.result)