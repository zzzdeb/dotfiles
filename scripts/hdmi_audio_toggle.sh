#!/bin/bash

#Adicionar regra no /etc/udev/rules.d/hdmi_sound.rules com o conteudo:
# SUBSYSTEM=="drm", ACTION=="change", RUN+="/usr/local/bin/hdmi_sound_toggle"

#Colocar em /usr/local/bin

USER_NAME=`who | grep "(:0)" | cut -f 1 -d ' '`
USER_ID=`id -u $USER_NAME`
HDMI_STATUS=`cat /sys/class/drm/card0/*HDMI*/status`

export PULSE_SERVER="unix:/run/user/"$USER_ID"/pulse/native"

if [[ $HDMI_STATUS = "connected" ]]
then
    sudo -u $USER_NAME pactl --server $PULSE_SERVER set-card-profile 0 output:hdmi-stereo+input:analog-stereo
else
    sudo -u $USER_NAME pactl --server $PULSE_SERVER set-card-profile 0 output:analog-stereo+input:analog-stereo
fi
