# OVA/OVF fail to deploy with "illegal character" ? Since ESX 6.5, this is because of a SCSI ID of 15 for a vmdk.
# Point this script to an .ovf (OVA support coming soon) and it will clean it up for deployment. :)
# Nico Aguilera - January 2018

#Ensure Python 2/3 compatibility
from __future__ import (absolute_import, division,print_function, unicode_literals)


# sample file to use:   C:\github\Pythons\ACH-EBS.ovf           (has the issue on lines 164 and 182) and its corresponding .mf 
ovfpath = input('Name of  OVF to fix (no quotes) (also, Nico is a n00b at python, only supports file in same folder as this script for now: ')

# open the .ovf to read - it's a text file
ovffile = open(ovfpath,'r')

#put contents of .ovf file in a string
ovfstring = ovffile.read()

# close the .ovf file, don't need it anymore
ovffile.close()

# replace all occurrences of AddressOnParent 15, save it into a new string
newOvfstring = ovfstring.replace('<rasd:AddressOnParent>15</rasd:AddressOnParent>','<rasd:AddressOnParent>11</rasd:AddressOnParent>')

#now open the .ovf to write to it.  
ovffile = open(ovfpath,'w')

#write the new OVF string
ovffile.write(newOvfstring)

#close the file, this writes to it :)
ovffile.close()

# now that the OVF is updated, we need to update the manifest (.mf) which includes SHA1 checksums for all .vmdks and the .ova
# So, calculate sha1 for the new .ovf


# open the .mf that corresponds to the .ovf
# replace the sha1 for the .ovf with the new one :)
# save .mf writing changes, and output that .mf has been udpated
# output that script ran and .ovf is ready for deployment now. 

print ("All done now")
input()