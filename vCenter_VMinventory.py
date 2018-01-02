#vCenter inventory script
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

# Loop through all objects to return name and VMware tools version
children = containerView.view
for child in children:
    childOS = child.summary.config.guestFullName
    childIP = child.summary.guest.ipAddress
    print("VM: {}, OS: {}, IP address: {}".format(child.name,childOS,childIP))


#disconnect session to vCenter
connect.Disconnect(my_vcenter)