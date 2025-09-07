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

# 3. Ensure target directory exists
mkdir -p /control/ssh

while [ ! -f /root/.ssh/id_rsa.pub ]; do sleep 1; done
cp /root/.ssh/id_rsa.pub  /control/ssh/authorized_keys
chmod 600 /control/ssh/authorized_keys

# ✅ Validate
if [[ -f /control/ssh/authorized_keys ]] && diff /root/.ssh/id_rsa.pub /control/ssh/authorized_keys >/dev/null; then
    echo "✅ SSH key copied successfully."
else
    echo "❌ Failed to copy SSH public key to shared volume!" >&2
    exit 1
fi

echo "✅ SSH key generated and shared."

exec "$@"  # This is optional but lets CMD be used properly

