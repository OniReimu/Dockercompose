FROM phusion/baseimage:0.9.19

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

#Creating working directory and installing Apache
RUN mkdir /code
WORKDIR /code
RUN echo `ls /code`
RUN apt-get update
RUN apt-get install -y inetutils-ping net-tools sudo git
RUN apt-get install -y apache2 apache2-doc apache2-utils
RUN sed -i "s#^.*KeepAlive.*#KeepAlive Off#" /etc/apache2/apache2.conf
RUN sed -i "s#Listen 80#Listen 8888#" /etc/apache2/ports.conf


###Enable MPM, Disable Prefork
ADD mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork

###Virtual Host
RUN sudo a2dissite 000-default.conf
ADD example.conf /etc/apache2/sites-available/example.conf
RUN sudo mkdir -p /var/www/example/public_html
RUN sudo mkdir /var/www/example/logs

RUN sudo a2ensite example.conf
ADD index.php /var/www/example/public_html

###Enable scripting of PHP
RUN apt-get install -y aptitude
RUN sudo aptitude purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`
RUN sudo add-apt-repository ppa:ondrej/php
RUN sudo apt-get update
RUN apt-get install -y libapache2-mod-php5.6 php5.6 php-xdebug php5.6-xcache php-gettext php5.6-mbstring
RUN sed -i "s#;extension=php_pgsql.dll#extension=php_pgsql.dll#" /etc/php/5.6/apache2/php.ini
RUN sudo a2enmod php5.6


RUN echo "Hello world! Here is Apache!!!"

#Creating projcet folder for Apache
RUN mkdir /etc/service/apache
ADD apacheini.sh /etc/service/apache/
RUN echo `ls /etc/service/apache`
RUN chmod -R 755 /etc/service/apache/
RUN sed -i "s/\r//" /etc/service/apache/apacheini.sh

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