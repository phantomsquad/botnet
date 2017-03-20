import os
import sys
import time
import socket

print "Are you sure you want to start the server?"
print ""
a = raw_input("[y/N] ")
if "y" in a:
	print ""
	print "Server started."
	time.sleep(3)
	os.system("python botnetclient.py")
	os.system("exit")
elif "n" in a:
	os.system("clear")
	sys.exit()
