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
	sub = raw_input("Masukan Domain : ")
	if sub =="":
		print("Please Input the Domain....")
		time.sleep(3)
		main()
	else:
		try:
			url = ("https://api.indoxploit.or.id/domain/"+sub)
			subdo = requests.get(url).json()
			ambil_data = subdo['data']['subdomains']
			for i in ambil_data:
				print(i)
				sub = open("subdo.txt", "a")
				sub.write(i+"\n")
			sub.close()
			print("\nSaved : subdo.txt")
			raw_input("Press enter returns to menu..."),main()
		except:
			exit()
def check():
	os.system("clear")
	dom = raw_input("Input Domain : ")
	f = open(dom,"r")
	z = f.read().splitlines()
	for dom in z:
		try:
			web = requests.get("http://"+dom).status_code
			stts = str(web)
			print(dom+" > "+stts)
		except requests.exceptions.InvalidURL:
			print(dom+" > Invalid URL")
		except requests.exceptions.HTTPError:
			print(dom+" > Http Error")
		except requests.exceptions.ConnectionError:
			print(dom+" > Error Connecting")
		except requests.exceptions.Timeout:
			print(dom+" > Timeout Error")
		except requests.exceptions.RequestException:
			print(dom+" > OOps: Something Else")
	raw_input("\nDONE!!! Press enter returns to menu"),main()

main()
