#vCenter 6.5 throws an error "Value Illegal" when there are disks with SCSI ID of 15
# this script scans all VMs in the inventory, and gives a list of all affected VMs
# perhaps it'll even fix them


#by Nico Aguilera

#Ensure Python 2/3 compatibility
from __future__ import (absolute_import, division,print_function, unicode_literals)

# requires "pip install pyvmomi"

import pyVim

from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim

vCenterIP="10.4.51.175"
vCenterPort=443
vCenterUsername="administrator@vsphere.local"
vCenterPassword=input('Enter password for vCenter:')

#connect to vCenter
my_vcenter = connect.ConnectNoSSL(vCenterIP, vCenterPort, vCenterUsername, vCenterPassword)  #connect.Connect requires a functional SSL on vCenter

#for retrieving information
content = my_vcenter.RetrieveContent()

container = content.rootFolder  # starting point - root folder
viewType = [vim.VirtualMachine]  #  look for object types "virtualMachine"
recursive = True  # so it goes into folders

# Create a view
containerView = content.viewManager.CreateContainerView(
    container, viewType, recursive)

# Loop through all objects to return name and disks
children = containerView.view
print("There are a total of %d Total VMs " %(len(children)))
for child in children:
    #if there's a SCSI = 15, add the VM to a new collection

#print the list of affected VMs


#ask if want to try fixing them
consentToFix = input('Should the script attempt to replace all ocurrences of SCSI ID 15?(y/n):')

if (consentToFix == 'y') or (consentToFix == 'Y')
    #do stuff
    #exit with message and results
    else:
    #exit with message
    
