# -*- mode: ruby -*-
# vi: set ft=ruby :
nodes_config = (JSON.parse(File.read("nodes.json")))['nodes']

VAGRANTFILE_API_VERSION = "2"

ENV["LC_ALL"] = "en_US.UTF-8"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 
  if ARGV[1] and \
     (ARGV[1].split('=')[0] == "--provider" or ARGV[2])
    provider = (ARGV[1].split('=')[1] || ARGV[2])
  else
    provider = (ENV['VAGRANT_DEFAULT_PROVIDER'] || :virtualbox).to_sym
  end
  puts "Detected #{provider}"  


  nodes_config.each do |node|

    node_name = node["node"] # name of node
    config.ssh.insert_key = false
    config.ssh.private_key_path = '~/.vagrant.d/insecure_private_key'


    # For each node
    config.vm.define node_name do |config|
      ports = node['ports']
      ports.each do |port|
        config.vm.network :forwarded_port,
        host: port['host'],
        guest: port['guest'],
        auto_correct: port['auto_correct']
      end

      config.vm.hostname = node['hostname']
      config.vm.network :private_network, ip: node['ip']


      # config.vm.box = 'bento/ubuntu-16.04'

      if provider==:virtualbox
        puts "provider= #{provider}"
        config.vm.box = 'bento/ubuntu-16.04'
        config.vm.synced_folder "provision", "/provision"
        config.vm.provider :virtualbox do |vb, override|
          vb.customize ["modifyvm", :id, "--memory", node['memory']]
          vb.customize ["modifyvm", :id, "--name", node['node']]
          vb.customize ["modifyvm", :id, "--cpus", node['cpus']]
          vb.customize ["modifyvm", :id, "--audio", "none"]
          vb.customize ["modifyvm", :id, "--usb", "off"]
        end
      end


      if Vagrant.has_plugin?("vagrant-hostsupdater")
        config.hostsupdater.aliases = node['aliases']
      end

      if Vagrant.has_plugin?("vagrant-cachier") && node['apt_cache']
        config.cache.scope = :machine
        config.cache.enable :apt
        config.cache.enable :gem
        config.cache.enable :bower
        config.cache.enable :npm
      end


      config.vm.provision "fix-no-tty", type: "shell" do |s|
        s.privileged = false
        s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
      end

      config.vm.provision "ansible" do |ansible|
        ansible.playbook = node['playbook'] 
        ansible.sudo = true
      end
    
    end
 end
end
