# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-docker-compose")
  system("vagrant plugin install vagrant-docker-compose")
  puts "Dependencies installed, please try the command again."
  exit
end

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.synced_folder ".", "/vagrant"
  config.vm.box = "phusion/ubuntu-14.04-amd64"


# Only run the provisioning on the first 'vagrant up'
  if Dir.glob("#{File.dirname(__FILE__)}/.vagrant/machines/default/*/id").empty?
    # Install Docker
    pkg_cmd = "wget -q -O - https://get.docker.io/gpg | apt-key add -;" \
      "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list;" \
      "apt-get update -qq; apt-get install -q -y --force-yes lxc-docker; "
    # Add vagrant user to the docker group
    pkg_cmd << "usermod -a -G docker vagrant; "
    config.vm.provision :shell, :inline => pkg_cmd
  end



  config.vm.network :private_network, ip: "192.168.58.31"
  config.vm.define "dockerhost"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "dockerhost"
    vb.memory = 2048
    vb.cpus = 2
  end

  portDjango = 8887
  portPSQL = 5432
  portRedis = 6379
  portNginx = 8080

  portSSHDjango = 8022
  portSSHPSQL = 8023
  portSSHRedis = 8024
#  portSSHNginx = 8025

  config.vm.network(:forwarded_port, guest: portDjango, host: portDjango)
  config.vm.network(:forwarded_port, guest: portPSQL, host: portPSQL)
  config.vm.network(:forwarded_port, guest: portRedis, host: portRedis)
  config.vm.network(:forwarded_port, guest: portNginx, host: portNginx)

  config.vm.network(:forwarded_port, guest: 22, host: portSSHDjango)
  config.vm.network(:forwarded_port, guest: 22, host: portSSHPSQL)
  config.vm.network(:forwarded_port, guest: 22, host: portSSHRedis)
#  config.vm.network(:forwarded_port, guest: 22, host: portSSHNginx)

  


  config.vm.provision :shell, inline: "apt-get update"
  config.vm.provision :shell, inline: "apt-get install -y git"
  config.vm.provision :shell, inline: "apt-get install -y expect"
  config.vm.provision :docker
  config.vm.provision "shell", inline: "ps aux|grep 'sshd:'|awk '{print $2}'|xargs kill"
  config.vm.provision "shell", inline: "echo 'now running su2root.expect'"
  config.vm.provision "shell", inline: "/vagrant/su2root.expect"
  config.vm.provision "shell", inline: "chmod 777 /var/lib/docker"
  config.vm.provision "shell", inline: "cd /vagrant"

  
#  config.ssh.username = "root"
#  config.ssh.private_key_path = "insecure_key"

  config.vm.provision :docker_compose, env: { "PORTSSHRedis" => "#{portSSHRedis}","PORTSSHDjango" => "#{portSSHDjango}","PORTSSHPSQL" => "#{portSSHPSQL}","PORTDjango" => "#{portDjango}", "PORTPSQL" => "#{portPSQL}", "PORTRedis" => "#{portRedis}", "PORTNginx" => "#{portNginx}"}, yml: "/vagrant/docker-compose.yml", rebuild: true, run: "always"

end

