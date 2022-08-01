import hashlib

s = "Python Bootcamp"

# getting hash with internal function
print("Hash: %s" % hash(s))

# getting MD5 hash
hash_MD5 = hashlib.md5(s.encode())
print("Hash MD5: %s" % hash_MD5.hexdigest())

# getting SHA256 hash
hash_SHA256 = hashlib.sha256(s.encode())
print("Hash SHA256: %s" % hash_SHA256.hexdigest())
