#!/bin/bash

# Create an freeBSD Virtual Machine using Virt-Manager

ISO="/var/lib/libvirt/boot/freebsd-13.0.iso"
DISK="/var/lib/libvirt/images/freebsd.qcow2"

VM_NAME="FreeBSD-13.0"

RAM="512"
SIZE="100"
CPU="1"

# shutdown existing VM
[ -f "$DISK" ] && virsh destroy "$VM_NAME"

# delete disk
[ -f "$DISK" ] && echo "Removing $DISK" && virsh undefine "$VM_NAME" && rm "$DISK"

# install vm
echo "Installing $VM_NAME"
virt-install --virt-type=kvm --name "$VM_NAME" --ram "$RAM" --vcpus="$CPU" --os-variant=freebsd9.3 --hvm --cdrom="$ISO" --network network=default --graphics vnc --disk "$DISK",size="$SIZE",bus=virtio,format=qcow2
