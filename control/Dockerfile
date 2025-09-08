FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip openssh-client sshpass vim && \
    pip3 install ansible && \
    mkdir -p /ansible /root/.ssh && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /ansible

# Copy bootstrap script into image
COPY bootstrap.sh /usr/local/bin/bootstrap.sh
RUN chmod +x /usr/local/bin/bootstrap.sh

# Run bootstrap each time container starts
ENTRYPOINT ["/usr/local/bin/bootstrap.sh"]
CMD ["/bin/bash"]