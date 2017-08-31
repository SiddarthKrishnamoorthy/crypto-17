import Crypto.Util.number as xgd
import hashlib as zfs

flag = "Some string"

if len(flag) != 17:
    print "You're wrong!!!"
    exit(1)

padding = xgd.bytes_to_long(zfs.md5(flag).digest())

secret = 0

for x in flag:
    secret = secret + padding
    secret = secret*ord(x)

print secret
#The value of secret is 88875271648816426359572741955640071243782001492239352683113083966490250
#Good luck!
