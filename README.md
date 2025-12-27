# Bluetooth Sniffer for a Temu Bluetooth Scale by OKOK
<img width="1718" height="960" alt="image" src="https://github.com/user-attachments/assets/30659173-679b-4c7d-a2b0-c9c54d845def" />
[Temu Link](https://www.temu.com/--scale--to-app-bathroom-human-body-scale-electronic-weight-scale-festival-gift-spring-new-product-christmas-plastic-material-aaa-included-g-601105719238886.html?_oak_mp_inf=EObB%2BKa91ogBGiBjNTg0Y2ZkMzc5ZGQ0NmY0OTU5YzQ0NDc4ZTdlYTZmMyDLm%2F%2FotTM%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Fopen%2Fc547de9b5a334d3d87183d09139695e4-goods.jpeg)

# Prerequisites
needs python3 module bleak (`pip3 install bleak`)

# Example
```
$ python3 ble_sniffer.py
[+] No MAC provided; attempting scale discovery... xD (go step on it)
[+] Found scale with MAC Address: A8:0B:6B:F4:23:38
[+] Using target MAC: A8:0B:6B:F4:23:38
[+] Listening for scale updates... (ctrl+C to stop)
[+] Scale has been stepped on
[+] User weighed in at 85.25 kg (187.94 lb)
[+] User weighed in at 85.25 kg (187.94 lb)
[+] Scale has been stepped on
[+] User weighed in at 85.25 kg (187.94 lb)
[+] Scale has been stepped on
[+] User weighed in at 85.25 kg (187.94 lb)
[+] Scale has been stepped on
[+] User weighed in at 85.25 kg (187.94 lb)
[+] User weighed in at 53.95 kg (118.94 lb)
[+] User weighed in at 85.25 kg (187.94 lb)
[+] User weighed in at 53.95 kg (118.94 lb)
```
