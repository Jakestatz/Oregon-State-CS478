# TCP SYN Flooding Attack

### 1. Create NetOne Network
    docker network create --subnet 10.2.5.0/24 NetOne --driver bridge
### 1. Launch Server Container in Privileged Mode
    docker run -it --privileged --network NetOne --name Server --ip 10.2.5.3 ubuntu:latest 
### 2. Disable SYN Cookies in The Server Container
    sysctl -a | grep syncookies (Display the SYN cookie flag)
    sysctl -w net.ipv4.tcp_syncookies=0 (turn off SYN cookie)
    sysctl -p (restart sysctl)
    sysctl -a | grep syncookies (sanity check, make sure =0) 
### 3. Launch Client Container
    docker run -it --network NetOne --name Client --ip 10.2.5.2 ubuntu:latest 
### 4. Launch Attacker Container
    docker run -it --network host --name Attacker ubuntu:latest 
### 5. Sniff From Client Container
    nc -l 80 -v (Run from server) 
    telnet 10.2.5.3 80 (Run from client)  
### 6. Launch Attack From Attacker Container
    Python3 SYN_Flood.py