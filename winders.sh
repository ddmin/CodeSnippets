#!/bin/bash

# Set up a Windows 10 Virtual Machine using Virt-Manager

ISO="/var/lib/libvirt/boot/windows10LTSC.iso"
VIRT="/var/lib/libvirt/boot/virtio-win.iso"
DISK="/var/lib/libvirt/images/windows.qcow2"

VM_NAME="Windows-10"

RAM="10240"
SIZE="400"
CPU="2"

# shutdown existing VM
[ -f "$DISK" ] && virsh destroy "$VM_NAME"

# delete disk
[ -f "$DISK" ] && echo "Removing $DISK" && virsh undefine "$VM_NAME" && rm "$DISK"

# install vm
echo "Installing $VM_NAME"
virt-install --name "$VM_NAME" --description "Windows 10" --graphics vnc,listen=0.0.0.0 --noautoconsole --os-type=windows --memory "$RAM" --vcpus "$CPU" --disk path="$DISK",bus=virtio,size="$SIZE" --cdrom="$ISO" --disk "$VIRT",device=cdrom,bus=ide --network network=default
