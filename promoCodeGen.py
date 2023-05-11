import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

os.system("title [Admiralz] Made by </0xZeDeen'211#0211")

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.BLUE +'Starting ZWeeksGen Promotion gen...'+i)
		sys.stdout.flush()
		time.sleep(0.1)

Spinner()

banner = (Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n"+ 
Fore.WHITE +Fore.RED +'''
  ________          __       _         _____            
 |___  /\ \        / /      | |       / ____|           
    / /  \ \  /\  / /__  ___| | _____| |  __  ___ _ __  
   / /    \ \/  \/ / _ \/ _ \ |/ / __| | |_ |/ _ \ '_ \ 
  / /__    \  /\  /  __/  __/   <\__ \ |__| |  __/ | | |
 /_____|    \/  \/ \___|\___|_|\_\___/\_____|\___|_| |_|
                                                        
                                                        
                                                            ' \n\n'''+ Fore.RESET + Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n")

os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.WHITE +Fore.RED +"                                         Welcome to "+Fore.RED+" ZWeeksGEN Promotion gen "+Fore.BLUE+"- 2023 -")
print(Fore.WHITE +Fore.BLUE +"                                         [1] "+Fore.RED+"Promotions Generator")
print(Fore.WHITE +Fore.BLUE +"                                         [2] "+Fore.RED+"Codes Checker")
print(Fore.WHITE +Fore.BLUE +"                                         [3] "+Fore.RED+"Credits")
print(Fore.WHITE +Fore.BLUE +"                                         [4] "+Fore.RED+"Exit")
print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
opcion = input("\nChoice: ")
if opcion=='1':
	os.system("cls")
	print(banner)
	cantidad = input("\nAmount to generate: ")
	while int(count)<int(cantidad):
		Codes = "https://discord.com/billing/promotions/3A"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(24))
		f= open(current_path +"/"+str("Codes")+str("")+".txt","a")
		f.write(Codes+"\n")
		print(Fore.GREEN +"Codes: "+ Fore.RESET + Codes)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.CYAN +Fore.RED +"Codes have been generated successfully!")
			print(Fore.WHITE +Fore.RED +"The codes are in the promocodes .txt !")
			input(Fore.BLUE +Fore.RED +"\nPress enter to exit")
			os.system("cls")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			print(Fore.BLUE +Fore.RED +"                                                   Closing!")
			print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			time.sleep(2)
			sys.exit()
			pass
	pass
if opcion=='2':
	os.system("cls")
	print("\n" + banner + "\n")
	with open('promocodes.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{codes}'  
	        }
	        src = requests.get('discord.com/api/v8/promotions/picsart', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.RED}InValid Codes >{Fore.RESET} ' + token)
	            else:
	                print(f'{Fore.LIGHTGREEN_EX}Valid Code >{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.CYAN}Error, please contact </0xZeDeen'211#0211 {Fore.RESET}")
pass
if opcion=='3':
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.WHITE +Fore.RED +"                                         Promotion Gen"+Fore.RED+" Made by "+Fore.RED+"ZeDeen")
	print(Fore.WHITE +Fore.RED +"                                         [Discord] "+Fore.BLUE+"ZWeeksGen Promo Gen")
	print(Fore.WHITE +Fore.RED +"                                         [Server] "+Fore.RED+"https://discord.gg/zRRTpXrDv4")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	input(Fore.RED +Fore.RED +"\nEnter to exit")
	os.system("cls")
	print(Fore.WHITE +Fore.BLUE +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.BLUE +Fore.RED +"                                                   Closing!")
	print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass
if opcion=='4':
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   Closing!")
	print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass


