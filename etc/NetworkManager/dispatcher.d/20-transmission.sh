#!/bin/sh
interface=$1 status=$2
if [[ "$interface" == "tun0" ]]; then
  case $status in
     up|vpn-up)
        systemctl start transmission
        su zzz -c "export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus; notify-send \"Starting Torrent\""
        ;;
     *)
        systemctl stop transmission
        killall transmission-daemon

        su zzz -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus; notify-send "Stoping Torrent"'
        ;;
  esac
fi
