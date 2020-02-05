sudo echo 'net.ipv6.conf.all.disable_ipv6 = 1' >> /etc/sysctl.d/40-ipv6.conf
sudo echo 'net.ipv6.conf.wlp5s0.disable_ipv6 = 1' >> /etc/sysctl.d/40-ipv6.conf

yay -S curl networkmanager-openvpn networkmanager-applet networkmanager

# sudo apt-get install curl network-manager-openvpn-gnome
cd /tmp
wget https://www.privateinternetaccess.com/installer/pia-nm.sh
sudo bash pia-nm.sh

sudo mkdir -p /etc/NetworkManager/dispatcher.d
sudo cp etc/NetworkManager/dispatcher.d/* /etc/NetworkManager/dispatcher.d/
sudo mkdir -p /etc/netctl
sudo cp etc/netctl/* /etc/netctl/
