# OVA/OVF fail to deploy with "illegal character" ? Since ESX 6.5, this is because of a SCSI ID of 15 for a vmdk.
# Point this script to an .ovf (OVA support coming soon) and it will clean it up for deployment. :)
# Nico Aguilera - January 2018

# TO DO:
# consolidate SHA1 calculations into a function or something more elegant



#Ensure Python 2/3 compatibility
from __future__ import (absolute_import, division,print_function, unicode_literals)

#for the SHA1 calculations
import hashlib

# sample file to use:   C:\github\Pythons\ACH-EBS.ovf           (has the issue on lines 164 and 182) and its corresponding .mf 
ovfpath = input('Name of  OVF to fix (no quotes) (also, Nico is a n00b at python, only supports file in same folder as this script for now: ')

# gonna need the SHA1 of this .ovf before we modify it, save it into oldmfSHA1. Using as reference: https://www.pythoncentral.io/hashing-files-with-python/ 
BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open(ovfpath, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
oldmfSHA1 = hasher.hexdigest()

print("Original OVF checksum: " + oldmfSHA1)

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

print ("OVF modified. All AddressOnParent values that were 15, are now 11.")

# now that the OVF is updated, we need to update the manifest (.mf) which includes SHA1 checksums for all .vmdks and the .ova
# So, calculate sha1 for the new .ovf and save it into newmfSHA1. 
BLOCKSIZE = 65536           
hasher = hashlib.sha1()
with open(ovfpath, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
newmfSHA1 = hasher.hexdigest()

print ("New OVF checksum: " + newmfSHA1)

# the .mf should have the exact same filename as the .ovf, so just get the path by replacing the extension
mfpath = ovfpath.replace('.ovf','.mf')

# open the .mf that corresponds to the .ovf
mffile = open(mfpath,'r')

# read contents of .mf 
mfstring = mffile.read()

# close the .mf, no longer needed opened
mffile.close()

# replace the sha1 for the .ovf with the new one
newMfString = mfstring.replace(oldmfSHA1,newmfSHA1)

# open the .mf to write to it now
mffile = open(mfpath,'w')

# write new string to the .mf and close/save
mffile.write(newMfString)
mffile.close()

print ("Manifest (.mf) has been updated with the OVF's new checksums. This OVF should deploy just fine now.")
input()