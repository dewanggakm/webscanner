# Sora Cyber Team & Rezad Odinson

#module
import os,sys,time
import requests
author = "dewanggakm"

def main():
	os.system("clear")
	print("Simple Tools!")
	print("1.Reverse IP")
	print("2.Subdomain Scanner")
	print("3.Status Code Checker")
	print("0.Exit")
	choose = raw_input("Choose : ")
	if choose =="":
		main()
	elif choose =="1":
		revip()
	elif choose =="2":
		subdo()
	elif choose =="3":
		check()
	else:
		exit("Exit")
	
def revip():
	os.system("clear")
	jumlah = []
	print("Simple Reverse IP tools")
	print("without http/https!!!")
	ini = raw_input("Input Domain : ")
	if ini =="":
		print("Harus Diisi !")
		time.sleep(1)
		revip()
	else:
		print("Wait..")
		time.sleep(2)
		ip = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+ini).text
		print("list : ")
		print(ip)
		rev = open("rev.txt", "w")
		rev.write(ip)
		rev.close()
		print("File Saved : rev.txt")
		raw_input("Press enter returns to menu ...");main()

def subdo():
	os.system("clear")
	jumlah = []
	print("Subdomain Scanner")
	print("without http/https!!!")
	sub = raw_input("Input Domain : ")
	if sub =="":
		print("Harus Diisi !")
		time.sleep(1)
		main()
	else:
		print("Wait...")
		time.sleep(2)
		subdo = requests.get("https://api.hackertarget.com/hostsearch/?q="+sub).text
		print("list : ")
		print(subdo)
		sub = open("subdo.txt", "w")
		sub.write(subdo)
		sub.close()
		print("File Saved : subdo.txt")
		raw_input("Press enter returns to menu ...");main()
def check():
	os.system("clear")
	dom = raw_input("Input Domain : ")
	f = open(dom,"r")
	z = f.read().split("\n")
	try:
		for dom in z :
			web = requests.get("http://"+dom)
			web.raise_for_status()
			print(dom+" ==> ", web.status_code)
	except requests.exceptions.InvalidURL as erri:
			print("Invalid URL:", erri)
	except requests.exceptions.HTTPError as errh:
	   		print("Http Error:",errh)
	except requests.exceptions.ConnectionError as errc:
		   	print("Error Connecting:",errc)
	except requests.exceptions.Timeout as errt:
		   	print("Timeout Error:",errt)
	except requests.exceptions.RequestException as err:
	    	print("OOps: Something Else",err)

main()
