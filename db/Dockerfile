FROM phusion/baseimage:0.9.19

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

#Creating working directory and installing Postgres
RUN mkdir /code
WORKDIR /code
RUN echo `ls /code`
RUN apt-get update
RUN apt-get install -y inetutils-ping net-tools sudo git
RUN apt-get install -y postgresql
RUN echo "Hello world! Here is Postgres!!!"

#Creating projcet folder for Postgres
RUN mkdir /etc/service/postgres
ADD postgresini.sh /etc/service/postgres/
RUN echo `ls /etc/service/postgres`
RUN chmod -R 755 /etc/service/postgres/
RUN sed -i "s/\r//" /etc/service/postgres/postgresini.sh

#Copying the rest of files into container
ADD . /code/
RUN echo `ls /code`

#Enabling SSH
RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
RUN /usr/sbin/enable_insecure_key

##Enabling SSH 127.0.0.1
RUN ssh-keygen -t ecdsa -P '' -f ~/.ssh/id_ecdsa
RUN cat ~/.ssh/id_ecdsa.pub >> ~/.ssh/authorized_keys

##Disable checking
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN echo "IgnoreUserKnownHosts yes" >> /etc/ssh/sshd_config

##Providing the previlidge
RUN chmod 700 /root/.ssh
RUN chmod 644 /root/.ssh/authorized_keys
RUN echo "SSH Successful!"


##Ansible
#RUN echo "[testhost]\n127.0.0.1" >> /etc/ansible/hosts
#RUN ansible-playbook /code/playbook.yml




# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*