#!/bin/sh

mount /dev/nvme0n1p6 /mnt
mount /dev/nvme0n1p2 /mnt/boot
mount /dev/sdc2 /mnt/home

mount -t proc /proc /mnt/proc 
mount --rbind /sys /mnt/sys
mount --rbind /dev /mnt/dev
