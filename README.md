*********************************************************************************************************
How to store data in git:
*********************************************************************************************************
goto location /mnt/d/study/source/ansible-lab$
rm -rf .git
git init

git config --global user.email "vpramesh.devops@gmail.com"
git config --global user.name "vprameshdevops-source"

********************************************************************************************************* 
in case of first time you have to add the public key into git settings -> SSH Key -> Add Key.
*********************************************************************************************************
cat ~/.ssh/id_rsa.pub

ssh-keygen -t ed25519 -C "vpramesh.devops@gmail.com"

ls -al ~/.ssh

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_ed25519  --> Starts and adds the SSH key to SSH agent..

ssh-add -l  

cat ~/.ssh/id_ed25519.pub

--> Copy this into settings --> SSH key and add it pls

Remote-WSL: New Window

/mnt/d/study/source/ansible-lab

********************************************************************************************************* 
git remote add origin git@github.com:vprameshdevops-source/ansible-lab.git
*********************************************************************************************************

This ensure you have right remote, run the below command

ramesh@Ramesh-PC:/mnt/d/study/source/ansible-lab$ git remote -v

origin  git@github.com:vprameshdevops-source/ansible-lab.git (fetch)
origin  git@github.com:vprameshdevops-source/ansible-lab.git (push)

********************************************************************************************************* 
This step would required to ensure vscode identifies right git repo and branch.
********************************************************************************************************* 
git push --set-upstream origin master

git add .

git commit -m 'commiting the code'

git push -u origin master

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

ansible -i inventory.ini all -m ping

ansible-playbook -i inventory.ini playbook/playbook.yml