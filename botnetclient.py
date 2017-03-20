import os
import sys
import time
import socket
import random

def main():
	os.system("clear")
	print("""
 __  __     ______     __  __     __   __     ______     ______
/\ \_\ \   /\  __ \   /\_\_\_\   /\ "-.\ \   /\  ___\   /\__  _\
\ \  __ \  \ \  __ \  \/_/\_\/_  \ \ \-.  \  \ \  __\   \/_/\ \/
 \ \_\ \_\  \ \_\ \_\   /\_\/\_\  \ \_\\"\_\  \ \_____\    \ \_\
  \/_/\/_/   \/_/\/_/   \/_/\/_/   \/_/ \/_/   \/_____/     \/_/

                Type '!* help' for commands

""")
	net = raw_input("-> ")
	if "!* help" in net:
		help()
	else:
		print ""
		print net + " is not a command."
		time.sleep(3)
		main()

main()
