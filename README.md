********************************************************************************************************* 
How to download ubuntu os:
********************************************************************************************************* 
docker pull ubuntu:22.04

********************************************************************************************************* 
How to run the docker compose 
*********************************************************************************************************
docker-compose down
docker-compose up -d

********************************************************************************************************* 
To connect with nodes from ansible controller first login to the docker.
*********************************************************************************************************

docker exec -it ansible-control bash

*********************************************************************************************************
Add the nodes to known_host files:
*********************************************************************************************************

ssh-keyscan node1 node2 node3 >> ~/.ssh/known_hosts

*********************************************************************************************************
Copy the public key from ansible node to other nodes for agentless and passwordless connection.
*********************************************************************************************************

ssh-copy-id -i /root/.ssh/id_rsa.pub root@node1
ssh-copy-id -i /root/.ssh/id_rsa.pub root@node2
ssh-copy-id -i /root/.ssh/id_rsa.pub root@node3

ssh root@node1
ssh root@node2
ssh root@node3

*********************************************************************************************************

docker compose -f 'docker-compose.yml' up -d --build 'control'

docker compose  --env-file .env -f 'docker-compose.yml' up -d --build

docker exec -it ansible-control bash

ansible -i inventory.ini all -m ping

ansible-playbook -i inventory.ini playbook/playbook.yml