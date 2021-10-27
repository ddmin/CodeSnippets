#!/bin/bash

# Create an OpenBSD Virtual Machine using Virt-Manager

ISO="/var/lib/libvirt/boot/openbsd-6.9.iso"
DISK="/var/lib/libvirt/images/openbsd.qcow2"

VM_NAME="OpenBSD-6.9"

RAM="512"
SIZE="100"
CPU="1"

# shutdown existing VM
[ -f "$DISK" ] && virsh destroy "$VM_NAME"

# delete disk
[ -f "$DISK" ] && echo "Removing $DISK" && virsh undefine "$VM_NAME" && rm "$DISK"

# install vm
echo "Installing $VM_NAME"
virt-install --virt-type=kvm --name "$VM_NAME" --ram "$RAM" --vcpus="$CPU" --os-variant=openbsd6.3 --hvm --cdrom="$ISO" --network network=default --graphics vnc --disk "$DISK",size="$SIZE",bus=virtio,format=qcow2
