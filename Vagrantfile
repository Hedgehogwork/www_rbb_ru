# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder ".", "/home/vagrant/www_rbb_ru"

  config.vm.provision "aptinstall",
    type: "shell",
    path: "provision/apt_reqs.sh",
    preserve_order: true,
    privileged: true

  config.vm.provision "djangoinstall",
    type: "shell",
    path: "provision/django_reqs.sh",
    preserve_order: true

end
