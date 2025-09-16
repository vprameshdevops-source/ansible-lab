FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server python3 python3-pip && \
    mkdir -p /root/.ssh && \
    mkdir /var/run/sshd && \
    echo 'root:docker' | chpasswd && \
    sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    rm -rf /var/lib/apt/lists/*

RUN service ssh start 

# Install Python dependencies for your Flask app
RUN pip3 install flask psutil requests yfinance plotly

WORKDIR /root

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
