import sys
import re

#accept subnetmask or cidr as input
if len(sys.argv) != 2:
   print('Please input one value as a command line argument. 0 or more than 1 inputs are invalid.')
   sys.exit(1)
input = sys.argv[1]


#convert subnetmask to cidr
if re.match("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",input):   #validate the format of subnetmask
  concatbin = ''   #prepare var for concatenated binary of subnetmask
  for octet in input.split("."):
    removed0b = str(bin(int(octet))[2:].zfill(8))   #remove the sign of binary and fill with max 8 zeroes
    concatbin += removed0b
  if re.match('(?=1*)1*0+$', concatbin) or re.match('1{32}', concatbin):   #the first pattern is to find 1 after 0
    print(sum([str(bin(int(octet))).count("1") for octet in input.split(".")]))   #the total num of 1 is cidr
#convert cidr to subnetmask
elif re.match('[0-9]$|1[0-9]$|2[0-9]$|3[0-2]$',input):
  cidr = int(input)
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  print(str( (0xff000000 & mask) >> 24)   + '.' +
        str( (0x00ff0000 & mask) >> 16)   + '.' +
        str( (0x0000ff00 & mask) >> 8)    + '.' +
        str( (0x000000ff & mask)))
#error handling
else:
  print('Your input is invalid. Input must follow the format of subnetmask (xxx.xxx.xxx.xxx) or cidr ([0-32]).')
