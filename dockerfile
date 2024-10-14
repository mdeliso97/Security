# base image Crypto 8-bit
FROM ubuntu:22.04

RUN cd ~ &&\
    apt-get update -y &&\
    apt-get upgrade -y &&\
    apt-get install git -y &&\
    apt-get install -y nano &&\
    apt-get install -y sudo &&\
    apt-get install dbus libdbus-1-3 dbus-x11 -y &&\
    apt-get update -y &&\
    apt-get install python3.9 python3-setuptools python3.9-dev -y &&\
    apt-get install python3-pip -y &&\
    apt-get install wget -y &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common &&\
    git clone https://github.com/mdeliso97/Crypto_8-bit.git

# install dependencies
RUN pip3 install -r Crypto_8-bit/requirements.txt

# launch crypto 8-bit
CMD ["python3" ,"Crypto_8-bit/cryptology.py"]


