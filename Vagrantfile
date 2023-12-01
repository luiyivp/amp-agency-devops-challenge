Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.network "forwarded_port", guest: 5432, host: 5432

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y software-properties-common
    apt-add-repository --yes --update ppa:ansible/ansible
    apt-get install -y ansible
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    ansible-playbook /vagrant/ansible/playbook.yaml -v
  SHELL
end
