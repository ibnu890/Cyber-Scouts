#!/usr/bin/env python
import subprocess

import json
from optparse import OptionParser
import subprocess
import base64
import md5                      
from socket import * 
import commands                  
import getopt
import StringIO
import random
import cookielib
import sys
from sgmllib import SGMLParser
import re
import sets
import urllib2
import sets
import socket
import urllib
import time
import httplib

# Terminal Colors

class bc:
    U = '\033[95m' # ungu
    B = '\033[94m' # Biru
    H = '\033[92m' # Hijau
    K = '\033[93m' # Kuning
    M = '\033[91m' # Merah
    ENDC = '\033[0m' # Akhir colors

if sys.platform == 'win32':
  bc.U = ''
  bc.B = ''
  bc.H = ''
  bc.K = ''
  bc.M = ''
  bc.ENDC = ''

# End of terminal colors

subprocess.call('clear', shell=True)

def password():
    print""
    print""+ bc.K +"+++++++Fuck++++++++"+ bc.ENDC +""
    import getpass
    try :
        sandi = getpass.getpass()
    except KeyboardInterrupt:
        print("\n\n[*] User keluar.")
        print("[*] aplikasi di matikan !!")
        sys.exit(1)
    if sandi == 'ibnu':
        print '||SelamaT||'
    else:
        print 'Username atau Password Anda Salah',exit()
    subprocess.call('clear', shell=True)
def ibnu():
    print""+ bc.H +"  _____________   __ "
    print""+ bc.H +" |_   _|  _  \ \ / /                                "
    print""+ bc.H +"   | | | | | |\ V / ___  ___  _ __ ___  _ __   __ _ "
    print""+ bc.H +"   | | | | | |/   \/ __|/ _ \| '__/ _ \| '_ \ / _` |"
    print""+ bc.H +"  _| |_| |/ // /^\ \__ \ (_) | | | (_) | | | | (_| |"
    print""+ bc.H +"  \___/|___/ \/   \/___/\___/|_|  \___/|_| |_|\__, |"
    print""+ bc.H +"                                               __/ |"
    print""+ bc.H +"                                              |___/ "
    print""+ bc.H +"        author : ibnugunawan my_IG | @ibnu_gp     "+ bc.ENDC + ""
ibnu()
def folder():
	ibnu()
	print(""+ bc.M + "["+ bc.B +"01"+ bc.M +"]"+ bc.M +" hash MD5"+ bc.H + ""+ bc.ENDC + "")
	print(""+ bc.M + "["+ bc.B +"02"+ bc.M +"]"+ bc.M +" decode base64"+ bc.H + ""+ bc.ENDC + "")
	print(""+ bc.M + "["+ bc.B +"03"+ bc.M +"]"+ bc.M +" encode base64"+ bc.H + ""+ bc.ENDC + "")
	print(""+ bc.M + "["+ bc.B +"00"+ bc.M +"]"+ bc.M +" Kembali"+ bc.H + ""+ bc.ENDC + "")
def menu():
    ibnu()
    print(""+ bc.M + "["+ bc.B +"01"+ bc.M +"]"+ bc.M +" Portscan "+ bc.H + ""+ bc.ENDC +"")
    print(""+ bc.M + "["+ bc.B +"02"+ bc.M +"]"+ bc.M +" Decode / encode "+ bc.H +""+ bc.ENDC +"")
    print(""+ bc.M + "["+ bc.B +"03"+ bc.M +"]"+ bc.M +" Wp_tema "+ bc.H +""+ bc.ENDC +"")
    print(""+ bc.M + "["+ bc.B +"04"+ bc.M +"]"+ bc.M +" wp plugins"+ bc.H +""+ bc.ENDC +"")
    print(""+ bc.M + "["+ bc.B +"05"+ bc.M +"]"+ bc.M +" Admin_findler"+ bc.H +""+ bc.ENDC +"")
    print(""+ bc.M + "["+ bc.B +"07"+ bc.M +"]"+ bc.M +" IP scaner"+ bc.H +""+ bc.ENDC +"")
    print ""
def encode_base64():
	ibnu()
	subprocess.call('clear', shell=True)
	import sys
	print (ibnu)
	import base64
	try:
		name = raw_input("masukan nama atau kalimat yang akan di encode :")
		print base64.b64encode(name)
	except KeyboardInterrupt:
		print("\n\n[*] User keluar.")
		print("[*] aplikasi di matikan !!")
		sys.exit(1)
def decode_base64():
	ibnu()
	subprocess.call('clear', shell=True)
	import base64
	try:
		name = raw_input("masukan hasil encode : ")
		print ("hasil decode : "),base64.b64decode(name)
	except KeyboardInterrupt:
		print("\n\n[*] User keluar.")
		print("[*] aplikasi di matikan !!")
		sys.exit(1)
def md5():
	ibnu()
	subprocess.call('clear', shell=True)
	import hashlib
	name = raw_input("masukan nama atau kalimat yang akan di decode :")
	print hashlib.md5(name).hexdigest()
def portscan():
	subprocess.call('clear', shell=True)
	ibnu()
	#!/usr/bin/env python
	import sys, time
	from datetime import datetime
	host = ''
	max_port = 5000
	min_port = 1

	def scan_host(host, port, r_code = 1):
		try:
			s = socket(AF_INET, SOCK_STREAM)

			code = s.connect_ex((host, port))

			if code == 0:
				r_code = code
			s.close()
		except Exception, e:
			pass

		return r_code

	try:
		host = raw_input("[*] Masukan Host Address Target : ")
	except KeyboardInterrupt:
		print("\n\n[*] Permintaan loe An Interrupt.")
		print("[*] Aplikasi di matikan.")
		sys.exit(1)

	hostip = gethostbyname(host)
	print("\n[*] Host : %s IP: %s" % (host, hostip))
	print("[*] Pemindaian di mulai AT %s...\n" % (time.strftime("%H:%M:%S")))
	start_time = datetime.now()
	for port in range(min_port, max_port):
		try:
			response = scan_host(host, port)

			if response == 0:
				print("[*] Port %d: Terbuka" % (port))
		except Exception, e:
			pass

	stop_time = datetime.now()
	total_time_duration = stop_time - start_time
	print("\n[*] Scanning Selesai AT %s..." % (time.strftime("%H:%M:%S")))
	print("[*] Waktu Scanning : %s ..." % (total_time_duration))
	print("[*] semoga harimu menyenangkan !!! ... @ibnu_gp ( Sploit )")

def wptema():
    ibnu()
    subprocess.call('clear', shell=True)
    tema = raw_input("Link for scann theme:")
    print "\nTarget:",tema
    print "Theme Scanning..."
    if not tema.startswith("http://"):
        tema = "http://"+tema
    magazine = tema+"/wp-content/themes/magazine"
    bizco = tema+"/wp-content/themes/bizco"
    suco = tema+"/wp-content/themes/suco"
    agency = tema+"/wp-content/themes/agency"
    koi = tema+"/wp-content/themes/koi"
    grido = tema+"/wp-content/themes/grido"
    education = tema+"/wp-content/themes/education"
    appius = tema+"/wp-content/themes/appius/"
    archin = tema+"/wp-content/themes/archin/"
    simfo = tema+"/wp-content/themes/simfo"
    radial = tema+"/wp-content/themes/radial-theme"
    echea = tema+"/wp-content/themes/echea/"
    reganto = tema+"/wp-content/themes/reganto-theme"
    rockstar = tema+"/wp-content/themes/rockstar-theme"
    elemin = tema+"/wp-content/themes/elemin"
    rayoflight = tema+"/wp-content/themes/rayoflight-theme"
    oxygen = tema+"/wp-content/themes/oxygen-theme"
    basic = tema+"/wp-content/themes/basic"
    bordeaux = tema+"/wp-content/themes/bordeaux-theme"
    wigi = tema+"/wp-content/themes/wigi"
    bulteno = tema+"/wp-content/themes/bulteno-theme"
    agritourismo = tema+"/wp-content/themes/agritourismo-theme/"
    wumblr = tema+"/wp-content/themes/wumblr"
    blogfolio = tema+"/wp-content/themes/blogfolio"
    minblr = tema+"/wp-content/themes/minblr"
    funki = tema+"/wp-content/themes/funki"
    folo = tema+"/wp-content/themes/folo"
    newsy = tema+"/wp-content/themes/newsy"
    responz = tema+"/wp-content/themes/responz"
    slide = tema+"/wp-content/themes/slide"
    parallax = tema+"/wp-content/themes/parallax"
    tisa = tema+"/wp-content/themes/tisa"
    bold = tema+"/wp-content/themes/bold"
    postline = tema+"/wp-content/themes/postline"
    qualifire = tema+"/wp-content/themes/qualifire"
    thisway = tema+"/wp-content/themes/ThisWay"
    metro = tema+"/wp-content/themes/metro"
    rezo = tema+"/wp-content/themes/rezo"
    pinboard = tema+"/wp-content/themes/pinboard"
    kmp = tema+"/wp-content/themes/kmp/"
    strange = tema+"/wp-content/themes/ut-strange"
    ghost = tema+"/wp-content/themes/Ghost"
    minshop = tema+"/wp-content/themes/minshop"
    area = tema+"/wp-content/themes/area53"
    purevision = tema+"/wp-content/themes/purevision"
    liberal = tema+"/wp-content/themes/liberal/"
    udesign = tema+"/wp-content/themes/u-design"
    shopsum = tema+"/wp-content/themes/shopsum/"
    ninetofive = tema+"/wp-content/themes/ninetofive"
    shotzz = tema+"/wp-content/themes/shotzz/"
    majestics = tema+"/wp-content/themes/majestics/"
    village = tema+"/wp-content/themes/village"
    scanmaje = urllib.urlopen(majestics)
    scanshot = urllib.urlopen(shotzz)
    scanshop = urllib.urlopen(shopsum)
    scanlib = urllib.urlopen(liberal)
    scanqual = urllib.urlopen(qualifire)
    scankm = urllib.urlopen(kmp)
    scansim = urllib.urlopen(simfo)
    scanvill = urllib.urlopen(village)
    scangrid = urllib.urlopen(grido)
    scansuc = urllib.urlopen(suco)
    scanrez = urllib.urlopen(rezo)
    scanbiz = urllib.urlopen(bizco)
    scanmin = urllib.urlopen(minshop)
    scanec = urllib.urlopen(echea)
    scanslid = urllib.urlopen(slide)
    scanbol = urllib.urlopen(bold)
    scanpost = urllib.urlopen(postline)
    scanpin = urllib.urlopen(pinboard)
    scanmet = urllib.urlopen(metro)
    scanrez = urllib.urlopen(responz)
    scanpara = urllib.urlopen(parallax)
    scanrock = urllib.urlopen(rockstar)
    scantis = urllib.urlopen(tisa)
    scanblog = urllib.urlopen(blogfolio)
    scanel = urllib.urlopen(elemin)
    scannew = urllib.urlopen(newsy)
    scanbas = urllib.urlopen(basic)
    scanwum = urllib.urlopen(wumblr)
    scanfol = urllib.urlopen(folo)
    scanfunk = urllib.urlopen(funki)
    scanminb = urllib.urlopen(minblr)
    scanagri = urllib.urlopen(agritourismo)
    scanwig = urllib.urlopen(wigi)
    scanborde = urllib.urlopen(bordeaux)
    scanbul = urllib.urlopen(bulteno)
    scanrad = urllib.urlopen(radial)
    scanox = urllib.urlopen(oxygen)
    scanarc = urllib.urlopen(archin)
    scanapi = urllib.urlopen(appius)
    scanray = urllib.urlopen(rayoflight)
    scanmag = urllib.urlopen(magazine)
    scanreg = urllib.urlopen(reganto)
    scanudes = urllib.urlopen(udesign)
    scanare = urllib.urlopen(area)
    scanagn = urllib.urlopen(agency)
    scannine = urllib.urlopen(ninetofive)
    scanstrang = urllib.urlopen(strange)
    scanthis = urllib.urlopen(thisway)
    scanko = urllib.urlopen(koi)
    scanghos = urllib.urlopen(ghost)
    scanpure = urllib.urlopen(purevision)
    scanedu = urllib.urlopen(education)
    if scanvill.getcode() == 200:
        print "[+] Found:",village
    elif scanvill.getcode() == 403:
        print "[+] Forbidden:",village
    elif scanvill.getcode() == 500:
        print "[+] Server Error:",village
    else:
        print "[-] Not found!:",village
    if scanghos.getcode() == 200:
        print "[+] Found:",ghost
    elif scanghos.getcode() == 403:
        print "[+] Forbidden:",ghost
    elif scanghos.getcode() == 500:
        print "[+] Server Error:",ghost
    else:
        print "[-] Not found!:",ghost
    if scanstrang.getcode() == 200:
        print "[+] Found:",strange
    elif scanstrang.getcode() == 403:
        print "[+] Forbidden:",strange
    elif scanstrang.getcode() == 500:
        print "[+] Server Error:",strange
    else:
        print "[-] Not found!:",strange
    if scanpure.getcode() == 200:
        print "[+] Found:",purevision
    elif scanpure.getcode() == 403:
        print "[+] Forbidden:",purevision
    elif scanpure.getcode() == 500:
        print "[+] Server Error:",purevision
    else:
        print "[-] Not found!:",purevision
    if scanthis.getcode() == 200:
        print "[+] Found:",thisway
    elif scanthis.getcode() == 403:
        print "[+] Forbidden:",thisway
    elif scanthis.getcode() == 500:
        print "[+] Server Error:",thisway
    else:
        print "[-] Not found!:",thisway
    if scannine.getcode() == 200:
        print "[+] Found:",ninetofive
    elif scannine.getcode() == 403:
        print "[+] Forbidden:",ninetofive
    elif scannine.getcode() == 500:
        print "[+] Server Error:",ninetofive
    else:
        print "[-] Not found!:",ninetofive
    if scanare.getcode() == 200:
        print "[+] Found:",area
    elif scanare.getcode() == 403:
        print "[+] Forbidden:",area
    elif scanare.getcode() == 500:
        print "[+] Server Error:",area
    else:
        print "[-] Not found!:",area
    if scanudes.getcode() == 200:
        print "[+] Found:",udesign
    elif scanudes.getcode() == 403:
        print "[+] Forbidden:",udesign
    elif scanudes.getcode() == 500:
        print "[+] Server Error:",udesign
    else:
        print "[-] Not found!:",udesign
    if scanqual.getcode() == 200:
        print "[+] Found:",qualifire
    elif scanqual.getcode() == 403:
        print "[+] Forbidden:",qualifire
    elif scanqual.getcode() == 500:
        print "[+] Server Error:",village
    else:
        print "[-] Not found!:",village
    if scanrock.getcode() == 200:
        print "[+] Found:",rockstar
    elif scanrock.getcode() == 403:
        print "[+] Forbidden:",rockstar
    elif scanrock.getcode() == 500:
        print "[+] Server Error:",rockstar
    else:
        print "[-] Not found!:",rockstar
    if scanreg.getcode() == 200:
        print "[+] Found:",reganto
    elif scanreg.getcode() == 403:
        print "[+] Forbidden:",reganto
    elif scanreg.getcode() == 500:
        print "[+] Server Error:",reganto
    else:
        print "[-] Not found!:",reganto
    if scanray.getcode() == 200:
        print "[+] Found:",rayoflight
    elif scanray.getcode() == 403:
        print "[+] Forbidden:",rayoflight
    elif scanray.getcode() == 500:
        print "[+] Server Error:",rayoflight
    else:
        print "[-] Not found!:",rayoflight
    if scanrad.getcode() == 200:
        print "[+] Found:",radial
    elif scanrad.getcode() == 403:
        print "[+] Forbidden:",radial
    elif scanrad.getcode() == 500:
        print "[+] Server Error:",radial
    else:
        print "[-] Not found!:",radial
    if scanox.getcode() == 200:
        print "[+] Found:",oxygen
    elif scanox.getcode() == 403:
        print "[+] Forbidden:",oxygen
    elif scanox.getcode() == 500:
        print "[+] Server Error:",oxygen
    else:
        print "[-] Not found!:",oxygen
    if scanbul.getcode() == 200:
        print "[+] Found:",bulteno
    elif scanbul.getcode() == 403:
        print "[+] Forbidden:",bulteno
    elif scanbul.getcode() == 500:
        print "[+] Server Error:",bulteno
    else:
        print "[-] Not found!:",bulteno
    if scanborde.getcode() == 200:
        print "[+] Found:",bordeaux
    elif scanborde.getcode() == 403:
        print "[+] Forbidden:",bordeaux
    elif scanborde.getcode() == 500:
        print "[+] Server Error:",bordeaux
    else:
        print "[-] Not found!:",bordeaux
    if scanagri.getcode() == 200:
        print "[+] Found:",agritourismo
    elif scanagri.getcode() == 403:
        print "[+] Forbidden:",agritourismo
    elif scanagri.getcode() == 500:
        print "[+] Server Error:",agritourismo
    else:
        print "[-] Not found!:",agritourismo
    if scanblog.getcode() == 200:
        print "[+] Found:",blogfolio
    elif scanblog.getcode() == 403:
        print "[+] Forbidden:",blogfolio
    elif scanblog.getcode() == 500:
        print "[+] Server Error:",blogfolio
    else:
        print "[-] Not found!:",blogfolio
    if scanwig.getcode() == 200:
        print "[+] Found:",wigi
    elif scanwig.getcode() == 403:
        print "[+] Forbidden:",wigi
    elif scanwig.getcode() == 500:
        print "[+] Server Error:",wigi
    else:
        print "[-] Not found!:",wigi
    if scanwum.getcode() == 200:
        print "[+] Found:",wumblr
    elif scanwum.getcode() == 403:
        print "[+] Forbidden:",wumblr
    elif scanwum.getcode() == 500:
        print "[+] Server Error:",wumblr
    else:
        print "[-] Not found!:",wumblr
    if scannew.getcode() == 200:
        print "[+] Found:",newsy
    elif scannew.getcode() == 403:
        print "[+] Forbidden:",newsy
    elif scannew.getcode() == 500:
        print "[+] Server Error:",newsy
    else:
        print "[-] Not found!:",newsy
    if scanminb.getcode() == 200:
        print "[+] Found:",minblr
    elif scanminb.getcode() == 403:
        print "[+] Forbidden:",minblr
    elif scanminb.getcode() == 500:
        print "[+] Server Error:",minblr
    else:
        print "[-] Not found!:",minblr
    if scanfunk.getcode() == 200:
        print "[+] Found:",funki
    elif scanfunk.getcode() == 403:
        print "[+] Forbidden:",funki
    elif scanfunk.getcode() == 500:
        print "[+] Server Error:",funki
    else:
        print "[-] Not found!:",funki
    if scanfol.getcode() == 200:
        print "[+] Found:",folo
    elif scanfol.getcode() == 403:
        print "[+] Forbidden:",folo
    elif scanfol.getcode() == 500:
        print "[+] Server Error:",folo
    else:
        print "[-] Not found!:",folo
    if scanel.getcode() == 200:
        print "[+] Found:",elemin
    elif scanel.getcode() == 403:
        print "[+] Forbidden:",elemin
    elif scanel.getcode() == 500:
        print "[+] Server Error:",elemin
    else:
        print "[-] Not found!:",elemin
    if scantis.getcode() == 200:
        print "[+] Found:",tisa
    elif scantis.getcode() == 403:
        print "[+] Forbidden:",tisa
    elif scantis.getcode() == 500:
        print "[+] Server Error:",tisa
    else:
        print "[-] Not found!:",tisa
    if scanrez.getcode() == 200:
        print "[+] Found:",responz
    elif scanrez.getcode() == 403:
        print "[+] Forbidden:",responz
    elif scanrez.getcode() == 500:
        print "[+] Server Error:",responz
    else:
        print "[-] Not found!:",responz
    if scanbas.getcode() == 200:
        print "[+] Found:",basic
    elif scanbas.getcode() == 403:
        print "[+] Forbidden:",basic
    elif scanbas.getcode() == 500:
        print "[+] Server Error:",basic
    else:
        print "[-] Not found!:",basic
    if scanpara.getcode() == 200:
        print "[+] Found:",parallax
    elif scanpara.getcode() == 403:
        print "[+] Forbidden:",parallax
    elif scanpara.getcode() == 500:
        print "[+] Server Error:",parallax
    else:
        print "[-] Not found!:",parallax
    if scanbol.getcode() == 200:
        print "[+] Found:",bold
    elif scanbol.getcode() == 403:
        print "[+] Forbidden:",bold
    elif scanbol.getcode() == 500:
        print "[+] Server Error:",bold
    else:
        print "[-] Not found!:",bold
    if scanmet.getcode() == 200:
        print "[+] Found:",metro
    elif scanmet.getcode() == 403:
        print "[+] Forbidden:",metro
    elif scanmet.getcode() == 500:
        print "[+] Server Error:",metro
    else:
        print "[-] Not found!:",metro
    if scanslid.getcode() == 200:
        print "[+] Found:",slide
    elif scanslid.getcode() == 403:
        print "[+] Forbidden:",slide
    elif scanslid.getcode() == 500:
        print "[+] Server Error:",slide
    else:
        print "[-] Not found!:",slide
    if scanpost.getcode() == 200:
        print "[+] Found:",postline
    elif scanpost.getcode() == 403:
        print "[+] Forbidden:",postline
    elif scanpost.getcode() == 500:
        print "[+] Server Error:",postline
    else:
        print "[-] Not found!:",postline
    if scanpin.getcode() == 200:
        print "[+] Found:",pinboard
    elif scanpin.getcode() == 403:
        print "[+] Forbidden:",pinboard
    elif scanpin.getcode() == 500:
        print "[+] Server Error:",pinboard
    else:
        print "[-] Not found!:",pinboard
    if scanmin.getcode() == 200:
        print "[+] Found:",minshop
    elif scanmin.getcode() == 403:
        print "[+] Forbidden:",minshop
    elif scanmin.getcode() == 500:
        print "[+] Server Error:",minshop
    else:
        print "[-] Not found!:",minshop
    if scansim.getcode() == 200:
        print "[+] Found:",simfo
    elif scansim.getcode() == 403:
        print "[+] Forbidden:",simfo
    elif scansim.getcode() == 500:
        print "[+] Server Error:",simfo
    else:
        print "[-] Not found!:",simfo
    if scanrez.getcode() == 200:
        print "[+] Found:",rezo
    elif scanrez.getcode() == 403:
        print "[+] Forbidden:",rezo
    elif scanrez.getcode() == 500:
        print "[+] Server Error:",rezo
    else:
        print "[-] Not found!:",rezo
    if scangrid.getcode() == 200:
        print "[+] Found:",grido
    elif scangrid.getcode() == 403:
        print "[+] Forbidden:",grido
    elif scangrid.getcode() == 500:
        print "[+] Server Error:",grido
    else:
        print "[-] Not found!:",grido
    if scanbiz.getcode() == 200:
        print "[+] Found:",bizco
    elif scanbiz.getcode() == 403:
        print "[+] Forbidden:",bizco
    elif scanbiz.getcode() == 500:
        print "[+] Server Error:",bizco
    else:
        print "[-] Not found!:",bizco
    if scansuc.getcode() == 200:
        print "[+] Found:",suco
    elif scansuc.getcode() == 403:
        print "[+] Forbidden:",suco
    elif scansuc.getcode() == 500:
        print "[+] Server Error:",suco
    else:
        print "[-] Not found!:",suco
    if scanmaje.getcode() == 200:
        print "[+] Found:",majestics
    elif scanmaje.getcode() == 403:
        print "[+] Forbidden:",majestics
    elif scanmaje.getcode() == 500:
        print "[+] Server Error:",majestics
    else:
        print "[-] Not found!:",majestics
    if scanshot.getcode() == 200:
        print "[+] Found:",shotzz
    elif scanshot.getcode() == 403:
        print "[+] Forbidden:",shotzz
    elif scanshot.getcode() == 500:
        print "[+] Server Error:",shotzz
    else:
        print "[-] Not found!:",shotzz
    if scanshop.getcode() == 200:
        print "[+] Found:",shopsum
    elif scanshop.getcode() == 403:
        print "[+] Forbidden:",shopsum
    elif scanshop.getcode() == 500:
        print "[+] Server Error:",shopsum
    else:
        print "[-] Not found!:",shopsum
    if scanlib.getcode() == 200:
        print "[+] Found:",liberal
    elif scanlib.getcode() == 403:
        print "[+] Forbidden:",liberal
    elif scanlib.getcode() == 500:
        print "[+] Server Error:",liberal
    else:
        print "[-] Not found!:",liberal
    if scanapi.getcode() == 200:
        print "[+] Found:",appius
    elif scanapi.getcode() == 403:
        print "[+] Forbidden:",appius
    elif scanapi.getcode() == 500:
        print "[+] Server Error:",appius
    else:
        print "[-] Not found!:",appius
    if scanarc.getcode() == 200:
        print "[+] Found:",archin
    elif scanarc.getcode() == 403:
        print "[+] Forbidden:",archin
    elif scanarc.getcode() == 500:
        print "[+] Server Error:",archin
    else:
        print "[-] Not found!:",archin
    if scanec.getcode() == 200:
        print "[+] Found:",echea
    elif scanec.getcode() == 403:
        print "[+] Forbidden:",echea
    elif scanec.getcode() == 500:
        print "[+] Server Error:",echea
    else:
        print "[-] Not found!:",echea
    if scankm.getcode() == 200:
        print "[+] Found:",kmp
    elif scankm.getcode() == 403:
        print "[+] Forbidden:",kmp
    elif scankm.getcode() == 500:
        print "[+] Server Error:",kmp
    else:
        print "[-] Not found!:",kmp    
    if scanedu.getcode() == 200:
        print "[+] Found:",education
    elif scanedu.getcode() == 403:
        print "[+] Forbidden:",education
    elif scanedu.getcode() == 500:
        print "[+] Server Error:",education
    else:
        print "[-] Not found!:",education
    if scanko.getcode() == 200:
        print "[+] Found:",koi
    elif scanko.getcode() == 403:
        print "[+] Forbidden:",koi
    elif scanko.getcode() == 500:
        print "[+] Server Error:",koi
    else:
        print "[-] Not found!:",koi
    if scanagn.getcode() == 200:
        print "[+] Found:",agency
    elif scanagn.getcode() == 403:
        print "[+] Forbidden:",agency
    elif scanagn.getcode() == 500:
        print "[+] Server Error:",agency
    else:
        print "[-] Not found!:",agency
    if scanmag.getcode() == 200:
        print "[+] Found:",magazine
    elif scanmag.getcode() == 403:
        print "[+] Forbidden:",magazine
    elif scanmag.getcode() == 500:
        print "[+] Server Error:",magazine
    else:
        print "[-] Not found!:",magazine

def wpplugin():
    ibnu()
    subprocess.call('clear', shell=True)
    plug = raw_input("Link for scann plugin:")
    print "\nTarget:",plug
    print "Plugin Scanning..."
    if not plug.startswith("http://"):
        plug = "http://"+plug
    simple = plug+"/wp-content/plugins/simple-ads-manager"
    wp3d = plug+"/wp-content/plugins/wp-3dflick-slideshow"
    fluid = plug+"/wp-content/plugins/fluid_forms"
    wpshop = plug+"/wp-content/plugins/wpshop"
    jqueryh = plug+"/wp-content/plugins/jquery-html5-file-upload"
    slideshow = plug+"/wp-content/plugins/slide-show-pro"
    easycom = plug+"/wp-content/plugins/easy-comment-uploads"
    comgallery = plug+"/wp-content/plugins/complete-galerry-manager"
    formcraft = plug+"/wp-content/plugins/formcraft"
    pitchprint = plug+"/wp-content/plugins/pitchprint"
    tevolution = plug+"/wp-content/plugins/Tevolution"
    wpmobile = plug+"/wp-content/plugins/wp-mobile-locator"
    scanwpmobil = urllib.urlopen(wpmobile)
    scanslides = urllib.urlopen(slideshow)
    scanwps = urllib.urlopen(wpshop)
    scanjquery = urllib.urlopen(jqueryh)
    scaneasy = urllib.urlopen(easycom)
    scansim = urllib.urlopen(simple)
    scancom = urllib.urlopen(comgallery)
    scanpitch = urllib.urlopen(pitchprint)
    scanform = urllib.urlopen(formcraft)
    scanwp3 = urllib.urlopen(wp3d)
    scanflu = urllib.urlopen(fluid)
    scantevo = urllib.urlopen(tevolution)
    if scanwpmobil.getcode() == 200:
        print "[+] Found:",wpmobile
    elif scanwpmobil.getcode() == 403:
        print "[+] Forbidden:",wpmobile
    elif scanwpmobil.getcode() == 500:
        print "[+] Server Error:",wpmobile
    else:
       print "[-] Not found!:",wpmobile
 
    if scanwps.getcode() == 200:
        print "[+] Found:",wpshop
    elif scanwps.getcode() == 403:
        print "[+] Forbidden:",wpshop
    elif scanwps.getcode() == 500:
        print "[+] Server Error:",wpshop
    else:
       print "[-] Not found!:",wpshop
 
    if scanjquery.getcode() == 200:
        print "[+] Found:",jqueryh
    elif scanjquery.getcode() == 403:
        print "[+] Forbidden:",jqueryh
    elif scanjquery.getcode() == 500:
        print "[+] Server Error:",jqueryh
    else:
       print "[-] Not found!:",jqueryh
 
    if scanslides.getcode() == 200:
        print "[+] Found:",slideshow
    elif scanslides.getcode() == 403:
        print "[+] Forbidden:",slideshow
    elif scanslides.getcode() == 500:
        print "[+] Server Error:",slideshow
    else:
       print "[-] Not found!:",slideshow
 
    if scaneasy.getcode() == 200:
        print "[+] Found:",easycom
    elif scaneasy.getcode() == 403:
        print "[+] Forbidden:",easycom
    elif scaneasy.getcode() == 500:
        print "[+] Server Error:",easycom
    else:
       print "[-] Not found!:",easycom
 
    if scancom.getcode() == 200:
        print "[+] Found:",comgallery
    elif scancom.getcode() == 403:
        print "[+] Forbidden:",comgallery
    elif scancom.getcode() == 500:
        print "[+] Server Error:",comgallery
    else:
       print "[-] Not found!:",comgallery
 
    if scantevo.getcode() == 200:
        print "[+] Found:",tevolution
    elif scantevo.getcode() == 403:
        print "[+] Forbidden:",tevolution
    elif scantevo.getcode() == 500:
        print "[+] Server Error:",tevolution
    else:
       print "[-] Not found!:",tevolution
 
    if scanflu.getcode() == 200:
        print "[+] Found:",fluid
    elif scanflu.getcode() == 403:
        print "[+] Forbidden:",fluid
    elif scanflu.getcode() == 500:
        print "[+] Server Error:",fluid
    else:
       print "[-] Not found!:",fluid
 
    if scanwp3.getcode() == 200:
        print "[+] Found:",wp3d
    elif scanwp3.getcode() == 403:
        print "[+] Forbidden:",wp3d
    elif scanwp3.getcode() == 500:
        print "[+] Server Error:",wp3d
    else:
       print "[-] Not found!:",wp3d
 
    if scansim.getcode() == 200:
        print "[+] Found:",simple
    elif scansim.getcode() == 403:
        print "[+] Forbidden:",simple
    elif scansim.getcode() == 500:
        print "[+] Server Error:",simple
    else:
       print "[-] Not found!:",simple
 
    if scanform.getcode() == 200:
        print "[+] Found:",formcraft
    elif scanform.getcode() == 403:
        print "[+] Forbidden:",formcraft
    elif scanform.getcode() == 500:
        print "[+] Server Error:",formcraft
    else:
       print "[-] Not found!:",formcraft
 
    if scanpitch.getcode() == 200:
        print "[+] Found:",pitchprint
    elif scanpitch.getcode() == 403:
        print "[+] Forbidden:",pitchprint
    elif scanpitch.getcode() == 500:
        print "[+] Server Error:",pitchprint
    else:
       print "[-] Not found!:",pitchprint

def adminfindler():
    ibnu()
    subprocess.call('clear', shell=True)
    adm = raw_input("Admin Finder:")
    print "\nTarget:",adm
    print "Admin Scanning..."
    if not adm.startswith("http://"):
        adm = "http://"+adm
    admin1 = adm+"/admin"
    admin2 = adm+"/administrator"
    admin3 = adm+"/adminweb"
    admin4 = adm+"/4dm1n"
    admin5 = adm+"/4dm1n1str4t0r"
    admin6 = adm+"/panel_admin"
    admin7 = adm+"/admin_panel"
    admin8 = adm+"/login/admin"
    admin9 = adm+"/admin/login"
    admin10 = adm+"/_admin"
    admin11 = adm+"/user/admin"
    admin12 = adm+"/admin.php"
    admin13 = adm+"/admin.aspx"
    admin14 = adm+"/redaktur"
    admin15 = adm+"/cp-admin"
    admin16 = adm+"/po-admin"
    admin17 = adm+"/p0-4dm1n"
    admin18 = adm+"/admin123"
    admin19 = adm+"/dataweb"
    admin20 = adm+"/pengurus"
    admin21 = adm+"/webpanel"
    admin22 = adm+"/paneldata"
    admin23 = adm+"/panel"
    admin24 = adm+"/admin/account.php"
    admin25 = adm+"/admin/login.php"
    admin26 = adm+"/admin/login.html"
    admin27 = adm+"/moderator"
    admin28 = adm+"/moderator/login.php"
    admin29 = adm+"/controlpanel"
    admin30 = adm+"/yonetim.asp"
    admin31 = adm+"/fileadmin"
    admin32 = adm+"/sysadmin"
    admin33 = adm+"/myadmin"
    admin34 = adm+"/wp-admin"
    admin35 = adm+"/ur-admin"
    admin36 = adm+"/webadmin"
    admin37 = adm+"/useradmin"
    admin38 = adm+"/blogindex"
    admin39 = adm+"/formslogin"
    admin40 = adm+"/admin_area"
    admin41 = adm+"/adminpro"
    admin42 = adm+"/super-admin"
    admin43 = adm+"/adm"
    admin44 = adm+"/cms"
    admin45 = adm+"/ADMIN"
    scanadm1 = urllib.urlopen(admin1)
    scanadm2 = urllib.urlopen(admin2)
    scanadm3 = urllib.urlopen(admin3)
    scanadm4 = urllib.urlopen(admin4)
    scanadm5 = urllib.urlopen(admin5)
    scanadm6 = urllib.urlopen(admin6)
    scanadm7 = urllib.urlopen(admin7)
    scanadm8 = urllib.urlopen(admin8)
    scanadm9 = urllib.urlopen(admin9)
    scanadm10 = urllib.urlopen(admin10)
    scanadm11 = urllib.urlopen(admin11)
    scanadm12 = urllib.urlopen(admin12)
    scanadm13 = urllib.urlopen(admin13)
    scanadm14 = urllib.urlopen(admin14)
    scanadm15 = urllib.urlopen(admin15)
    scanadm16 = urllib.urlopen(admin16)
    scanadm17 = urllib.urlopen(admin17)
    scanadm18 = urllib.urlopen(admin18)
    scanadm19 = urllib.urlopen(admin19)
    scanadm20 = urllib.urlopen(admin20)
    scanadm21 = urllib.urlopen(admin21)
    scanadm22 = urllib.urlopen(admin22)
    scanadm23 = urllib.urlopen(admin23)
    scanadm24 = urllib.urlopen(admin24)
    scanadm25 = urllib.urlopen(admin25)
    scanadm26 = urllib.urlopen(admin26)
    scanadm27 = urllib.urlopen(admin27)
    scanadm28 = urllib.urlopen(admin28)
    scanadm29 = urllib.urlopen(admin29)
    scanadm30 = urllib.urlopen(admin30)
    scanadm31 = urllib.urlopen(admin31)
    scanadm32 = urllib.urlopen(admin32)
    scanadm33 = urllib.urlopen(admin33)
    scanadm34 = urllib.urlopen(admin34)
    scanadm35 = urllib.urlopen(admin35)
    scanadm36 = urllib.urlopen(admin36)
    scanadm37 = urllib.urlopen(admin37)
    scanadm38 = urllib.urlopen(admin38)
    scanadm39 = urllib.urlopen(admin39)
    scanadm40 = urllib.urlopen(admin40)
    scanadm41 = urllib.urlopen(admin41)
    scanadm42 = urllib.urlopen(admin42)
    scanadm43 = urllib.urlopen(admin43)
    scanadm44 = urllib.urlopen(admin44)
    scanadm45 = urllib.urlopen(admin45)
    if scanadm1.getcode() == 200:
        print "[+] Found:",admin1
    else:
        print "[-] Not Found:",admin1
 
    if scanadm2.getcode() == 200:
        print "[+] Found:",admin2
    else:
        print "[-] Not Found:",admin2
 
    if scanadm3.getcode() == 200:
        print "[+] Found:",admin3
    else:
        print "[-] Not Found:",admin3
 
    if scanadm4.getcode() == 200:
        print "[+] Found:",admin4
    else:
        print "[-] Not Found:",admin4
 
    if scanadm5.getcode() == 200:
        print "[+] Found:",admin5
    else:
        print "[-] Not Found:",admin5
 
    if scanadm6.getcode() == 200:
        print "[+] Found:",admin6
    else:
        print "[-] Not Found:",admin6
 
    if scanadm7.getcode() == 200:
        print "[+] Found:",admin7
    else:
        print "[-] Not Found:",admin7
 
    if scanadm8.getcode() == 200:
        print "[+] Found:",admin8
    else:
        print "[-] Not Found:",admin8
 
    if scanadm9.getcode() == 200:
        print "[+] Found:",admin9
    else:
        print "[-] Not Found:",admin9
 
    if scanadm10.getcode() == 200:
        print "[+] Found:",admin10
    else:
        print "[-] Not Found:",admin10
 
    if scanadm11.getcode() == 200:
        print "[+] Found:",admin11
    else:
        print "[-] Not Found:",admin11
 
    if scanadm12.getcode() == 200:
        print "[+] Found:",admin12
    else:
        print "[-] Not Found:",admin12
 
    if scanadm13.getcode() == 200:
        print "[+] Found:",admin13
    else:
        print "[-] Not Found:",admin13
 
    if scanadm14.getcode() == 200:
        print "[+] Found:",admin14
    else:
        print "[-] Not Found:",admin14
 
    if scanadm15.getcode() == 200:
        print "[+] Found:",admin15
    else:
        print "[-] Not Found:",admin15
 
    if scanadm16.getcode() == 200:
        print "[+] Found:",admin16
    else:
        print "[-] Not Found:",admin16
 
    if scanadm17.getcode() == 200:
        print "[+] Found:",admin17
    else:
        print "[-] Not Found:",admin17
 
    if scanadm18.getcode() == 200:
        print "[+] Found:",admin18
    else:
        print "[-] Not Found:",admin18
 
    if scanadm19.getcode() == 200:
        print "[+] Found:",admin19
    else:
        print "[-] Not Found:",admin29
 
    if scanadm20.getcode() == 200:
        print "[+] Found:",admin20
    else:
        print "[-] Not Found:",admin20
 
    if scanadm21.getcode() == 200:
        print "[+] Found:",admin21
    else:
        print "[-] Not Found:",admin21
 
    if scanadm22.getcode() == 200:
        print "[+] Found:",admin22
    else:
        print "[-] Not Found:",admin22
 
    if scanadm23.getcode() == 200:
        print "[+] Found:",admin23
    else:
        print "[-] Not Found:",admin23
 
    if scanadm24.getcode() == 200:
        print "[+] Found:",admin24
    else:
        print "[-] Not Found:",admin24
 
    if scanadm25.getcode() == 200:
        print "[+] Found:",admin25
    else:
        print "[-] Not Found:",admin25
 
    if scanadm26.getcode() == 200:
        print "[+] Found:",admin26
    else:
        print "[-] Not Found:",admin26
 
    if scanadm27.getcode() == 200:
        print "[+] Found:",admin27
    else:
        print "[-] Not Found:",admin27
 
    if scanadm28.getcode() == 200:
        print "[+] Found:",admin28
    else:
        print "[-] Not Found:",admin28
 
    if scanadm29.getcode() == 200:
        print "[+] Found:",admin29
    else:
        print "[-] Not Found:",admin29
 
    if scanadm30.getcode() == 200:
        print "[+] Found:",admin30
    else:
        print "[-] Not Found:",admin30
 
    if scanadm31.getcode() == 200:
        print "[+] Found:",admin31
    else:
        print "[-] Not Found:",admin31
 
    if scanadm32.getcode() == 200:
        print "[+] Found:",admin32
    else:
        print "[-] Not Found:",admin32
 
    if scanadm33.getcode() == 200:
        print "[+] Found:",admin33
    else:
        print "[-] Not Found:",admin33
 
    if scanadm34.getcode() == 200:
        print "[+] Found:",admin34
    else:
        print "[-] Not Found:",admin34
 
    if scanadm35.getcode() == 200:
        print "[+] Found:",admin35
    else:
        print "[-] Not Found:",admin35
 
    if scanadm36.getcode() == 200:
        print "[+] Found:",admin36
    else:
        print "[-] Not Found:",admin36
 
    if scanadm37.getcode() == 200:
        print "[+] Found:",admin37
    else:
        print "[-] Not Found:",admin37
 
    if scanadm38.getcode() == 200:
        print "[+] Found:",admin38
    else:
        print "[-] Not Found:",admin38
 
    if scanadm39.getcode() == 200:
        print "[+] Found:",admin39
    else:
        print "[-] Not Found:",admin39
 
    if scanadm40.getcode() == 200:
        print "[+] Found:",admin40
    else:
        print "[-] Not Found:",admin40
 
    if scanadm41.getcode() == 200:
        print "[+] Found:",admin41
    else:
        print "[-] Not Found:",admin41
 
    if scanadm42.getcode() == 200:
        print "[+] Found:",admin42
    else:
        print "[-] Not Found:",admin42
 
    if scanadm43.getcode() == 200:
        print "[+] Found:",admin43
    else:
        print "[-] Not Found:",admin43
 
    if scanadm44.getcode() == 200:
        print "[+] Found:",admin44
    else:
        print "[-] Not Found:",admin44
 
    if scanadm45.getcode() == 200:
        print "[+] Found:",admin45
    else:
        print "[-] Not Found:",admin45

def kunci():
    from Crypto.Hash import SHA256
    from Crypto.Cipher import AES
    import os, random, sys, pkg_resources

    def encrypt(key, filename):
        chunksize = 64 * 1024
        outFile = os.path.join(os.path.dirname(filename), "(encrypted)"+os.path.basename(filename))
        filesize = str(os.path.getsize(filename)).zfill(16)
        IV = ''

        for i in range(16):
            IV += chr(random.randint(0, 0xFF))
    
        encryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(filename, "rb") as infile:
            with open(outFile, "wb") as outfile:
                outfile.write(filesize)
                outfile.write(IV)
                while True:
                    chunk = infile.read(chunksize)
                
                    if len(chunk) == 0:
                        break

                    elif len(chunk) % 16 !=0:
                        chunk += ' ' *  (16 - (len(chunk) % 16))

                    outfile.write(encryptor.encrypt(chunk))

                outfile.truncate(int(filesize))

    def decrypt(key, filename):
        outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))
        chunksize = 64 * 1024
        with open(filename, "rb") as infile:
            filesize = infile.read(16)
            IV = infile.read(16)

            decryptor = AES.new(key, AES.MODE_CBC, IV)
        
            with open(outFile, "wb") as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break

                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(int(filesize))

    def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd()):
            for names in files:
                allFiles.append(os.path.join(root, names))

        return allFiles

    
    choice = raw_input("Apakah kamu mau (E)ncrypt or (D)ecrypt? ")
    password = raw_input("Masukan password: ")

    encFiles = allfiles()

    if choice == "E":
        for Tfiles in encFiles:
            if os.path.basename(Tfiles).startswith("(encrypted)"):
                print "%s siap di encrypted" %str(Tfiles)
                pass

            elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
                pass
            else:
                encrypt(SHA256.new(password).digest(), str(Tfiles))
                print "Selesai encrypting %s" %str(Tfiles)
                os.remove(Tfiles)


    elif choice == "D":
        filename = raw_input("Masukan nama file yang akan di decrypt: ")
        if not os.path.exists(filename):
            print "File tidak ada"
            sys.exit(0)
        elif not filename.startswith("(encrypted)"):
            print "%s tidak siap di encrypted" %filename
            sys.exit()
        else:
            decrypt(SHA256.new(password).digest(), filename)
            print "Selesai decrypting %s" %filename
            os.remove(filename)

    else:
        print "Silahkan pilih perintah yang valid."
        sys.exit()

def ip_scan():
    import subprocess

    net_addr = input("Masukkan alamat jaringan dalam format CIDR(ex.192.168.1.0/24): ")
    ip_net = ipaddress.ip_network(net_addr)
    all_hosts = list(ip_net.hosts())

    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    for i in range(len(all_hosts)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

        if "Host tujuan tidak terjangkau" in output.decode('utf-8'):
            print(str(all_hosts[i]), "Tidak ada sambungan")
        elif "Request timed out" in output.decode('utf-8'):
            print(str(all_hosts[i]), "Tidak ada sambungan")
        else:
            print(str(all_hosts[i]), "Ada sambungan")

#program
password()
menu()
try:
	pilih = input(""+ bc.K + "Ibnu"+ bc.H +"@"+ bc.M + "IDXsorong : "+ bc.ENDC +"")
except KeyboardInterrupt:
		print("\n\n[*] User keluar.")
		print("[*] aplikasi di matikan !!")
		sys.exit(1)
if pilih == 1:
	portscan()
elif pilih == 2:
	folder()
	pilih = input(""+ bc.K + "Ibnu"+ bc.H +"@"+ bc.U + "IDXsorong : "+ bc.ENDC +"")
	if pilih == 1:
		md5()
	elif pilih == 2:
		encode_base64()
	elif pilih == 3:
		decode_base64()
	elif pilih == 00:
		menu()
elif pilih == 3:
	wptema()
elif pilih == 4:
    wpplugin()
elif pilih == 5:
    adminfindler()
elif pilih == 6:
    ip_scan()
elif pilih == 00:
    e = raw_input("Keluar ? | (Y/T)")
    if e in ["y","Y"]:
        print(exit())
    elif e in ["t","T"]:
        print("Makasih")
else:
	print("monyet")
