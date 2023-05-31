FROM ubuntu
RUN apt-get -y update 
RUN apt-get -y install iputils-ping 
RUN apt-get -y install net-tools 
RUN apt-get -y install telnet 
RUN apt-get -y install iproute2
RUN apt-get -y install python3
RUN apt-get -y install python3-scapy 
RUN apt-get -y install netcat
RUN apt-get -y install vim
