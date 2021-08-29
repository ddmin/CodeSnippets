#!/bin/bash

# Set up an Ubuntu Virtual Machine using Virt-Manager

ISO="/var/lib/libvirt/boot/ubuntu-21.04.iso"
DISK="/var/lib/libvirt/images/ubuntu.qcow2"

VM_NAME="Ubuntu-21.04"

RAM="4096"
SIZE="100"
CPU="1"

# shutdown existing VM
[ -f "$DISK" ] && virsh destroy "$VM_NAME"

# delete disk
[ -f "$DISK" ] && echo "Removing $DISK" && virsh undefine "$VM_NAME" && rm "$DISK"

# install vm
echo "Installing $VM_NAME"
virt-install --virt-type=kvm --name "$VM_NAME" --ram "$RAM" --vcpus="$CPU" --os-variant=generic --hvm --cdrom="$ISO" --network network=default --graphics vnc --disk "$DISK",size="$SIZE",bus=virtio,format=qcow2
