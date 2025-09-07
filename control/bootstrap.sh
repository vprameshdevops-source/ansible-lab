#!/bin/bash
echo "Bootstrap script is running..."
# Add any setup logic here
# 1. Generate new SSH keypair (overwrite each time)
echo " Generating fresh SSH keypair..."
rm -f /root/.ssh/id_rsa /root/.ssh/id_rsa.pub
ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa -N ""

# 2. Add nodes to known_hosts
echo "Adding nodes to known_hosts..."
ssh-keyscan node1 node2 node3 >> /root/.ssh/known_hosts 2>/dev/null

echo "You need to login to the host with the passwords each time."

exec "$@"  # This is optional but lets CMD be used properly

