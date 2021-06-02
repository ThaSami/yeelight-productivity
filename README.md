### Requirements

First get the lamp token https://python-miio.readthedocs.io/en/latest/discovery.html#logged-tokens

Then enable developer mode on the lamp 

``miiocli yeelight --ip <IP> --token <token> set_developer_mode 1``

make sure to update the IP inside the api.py

---
### Extension

head to 
``chrome://extensions``
click on (Load unpacked)
then choose the extension dir. 


### TODO
- Dockerize and parametrize the API