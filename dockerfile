# base image Crypto 8-bit
FROM ubuntu:22.04


# Set environment to noninteractive to avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
    software-properties-common \
    git \
    nano \
    sudo \
    dbus libdbus-1-3 dbus-x11 \
    python3.9 \
    python3-pip \
    python3-tk \
    pulseaudio \
    alsa-utils \
    wget && \
    apt-get clean

# Clone the repository
RUN git clone https://github.com/mdeliso97/Crypto_8-bit.git

# Set working directory to the cloned repository
WORKDIR /Crypto_8-bit


# Install Python dependencies
RUN pip3 install -r requirements.txt

# Launch Crypto 8-bit
CMD ["python3", "cryptology.py"]


