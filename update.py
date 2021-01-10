import shutil
import hashlib
import os

print("zipping contents...")
shutil.make_archive("memePack", "zip", "contents")
print("calculating SHA1...")
sha1 = hashlib.sha1()
with open("memePack.zip", "rb") as f:
	while True:
		data = f.read(65536) #64kb chunks of data, arbitrary amount
		if not data: #if EOF
			break
		sha1.update(data)
		
print("writing readme.md...")
with open("README.md", "w") as readme, open("base readme.md", "r") as template:
	readme.write(template.read())
	readme.write(sha1.hexdigest())
	
print("done!")