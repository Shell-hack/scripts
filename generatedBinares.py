import base64
import urllib.request
import socket

# Script by: BASH -shell script

try:
	userAgent = urllib.request.build_opener()
	userAgent.addheaders = [('User-agent', 'Mozilla/5.0')]
	userAgent.open('https://www.google.com')
	print("")
	print ("User-agent open !")
	print("")
except:
	print ("error user-agent")


def licenseKey():
	print("")
	print("License key:")
	print(str(base64.b64encode(b"License: Bash Shell")))
	print("")

licenseKey()

def socketDos():
	try:
		while True:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			lineCmd = input ("ip-host: ")
			sock.connect((lineCmd, 80))
			for packs in range(1, 65535):
				print("Atacando", lineCmd, "port", "80")
	except:
		print("")
		print("Erro no hostname <-")
		print("")

socketDos()