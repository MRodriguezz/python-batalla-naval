#-*- coding: utf-8 -*-
import random
import os 
import time
import sys
#*****************************************************************************************************************************
#************************************************** BLOQUE INSTRUCCIONES *****************************************************
#*****************************************************************************************************************************
def instrucciones():
	print "              _____ _   _  _____ _______ _____  _    _  _____ _____ _____ ____   _   _ ______  _____  "
	print "             |_   _| \ | |/ ____|__   __|  __ \| |  | |/ ____/ ____|_   _/ __ \ | \ | |  ____|/ ____|  "
	print "               | | |  \| | (___    | |  | |__) | |  | | |   | |      | || |  | ||  \| | |__   | (__    "
	print "               | | | . ` |\___ \   | |  |  _  /| |  | | |   | |      | || |  | || . ` |  __|  \___ \   "
	print "              _| |_| |\  |____) |  | |  | | \ \| |__| | |___| |____ _| || |__| || |\  | |____ ____) |  "
	print "             |_____|_| \_|______/  |_|  |_|  \_\\\_____/\_____\_____|_____\_____/|_| \_|______|______/   " 
	print "                                                                                                      "

	print """              Este juego se compone solamente de un tablero, solamente para un jugador, ya que este llega 
	      a poner en practica sus destrezas contra la maquina, y así al mismo tiempo llegando a adivinar 
	      los barcos que se encuentran escondidos aleatoriamente en el tablero, el tablero se compone de 15*15 
	      casillas y cada posición se identifica con números permitidos del 1 al 16 en cada FILA y COLUMNA."""
	print "                                                                                                    "        
	print  """             Una vez todas las naves posicionas por la maquina, se inicia una serie de rondas las cuales constan 
	       de 5 turnos. En cada ronda, el jugador va ingresando números aleatorios hasta adivinar 
	       y poder hundir los barcos. Cuando las posición de un barco ha sido dañada, debe indicar ¡Genial! ¡Pudiste 
	       hundir mi barco!, de tal circunstancia que indicará al atacante la importancia de la nave destruida. Ahora bien, 
	       si la posición estuviera fuera de las coordenadas que posee el tablero mostrara un mensaje diciendo 
	       ¡Vaya, esta coordenada no se encuentra en el Océano.!"""
	print ""

#*****************************************************************************************************************************
#************************************************* MENSAJE BIENVENIDA ********************************************************
#*****************************************************************************************************************************
print ""
def mensaje():
	print """ 
		d8888b. d888888b d88888b d8b   db db    db d88888b d8b   db d888888b d8888b.  .d88b.  .d8888.      
		88  `8D   `88'   88'     888o  88 88    88 88'     888o  88   `88'   88  `8D .8P  Y8. 88'  YP      
		88oooY'    88    88ooooo 88V8o 88 Y8    8P 88ooooo 88V8o 88    88    88   88 88    88 `8bo.        
		88~~~b.    88    88~~~~~ 88 V8o88 `8b  d8' 88~~~~~ 88 V8o88    88    88   88 88    88   `Y8b.      
		88   8D   .88.   88.     88  V888  `8bd8'  88.     88  V888   .88.   88  .8D `8b  d8' db   8D      
		Y8888P' Y888888P Y88888P VP   V8P    YP    Y88888P VP   V8P Y888888P Y8888D'  `Y88P'  `8888Y'

							  d8b.  
							d8' `8b 
							88ooo88 
							88~~~88 
							88   88 
							YP   YP 

		d8888b.  .d8b.  d888888b  .d8b.  db      db       .d8b.       d8b   db  .d8b.  db    db  .d8b.  db      
		88  `8D d8' `8b `~~88~~' d8' `8b 88      88      d8' `8b      888o  88 d8' `8b 88    88 d8' `8b 88      
		88oooY' 88ooo88    88    88ooo88 88      88      88ooo88      88V8o 88 88ooo88 Y8    8P 88ooo88 88      
		88~~~b. 88~~~88    88    88~~~88 88      88      88~~~88      88 V8o88 88~~~88 `8b  d8' 88~~~88 88      
		88   8D 88   88    88    88   88 88booo. 88booo. 88   88      88  V888 88   88  `8bd8'  88   88 88booo. 
		Y8888P' YP   YP    YP    YP   YP Y88888P Y88888P YP   YP      VP   V8P YP   YP    YP    YP   YP Y88888P """
	print " "
mensaje()
#*********************************************************** GANADOR *********************************************************
#*****************************************************************************************************************************
def ganaste():
	print "FELICIDADES, HAZ GANADO"

#*********************************************************** PERDEDOR ********************************************************
#*****************************************************************************************************************************
def perdiste():
	print """               
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###############@@@@@#@@@@@@
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####################@#@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MMMBBBMMMMMMMMMMMMMMMM####@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@H@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG9G&AAAAAAAAAAAAAAHBB##@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@ss#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#h@@@@@H5i5X3XX222255223h&HM##@@@@@
		 @@@@@@@@@A@@@@@@@@@@@@@@@#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#G&rS@@@@@@HX2X3irrrrs52S29&AB#@@@@@@
		 @@@@@2hH: &BXssA@@@@@@@@@@: ;@@@@@@@@M @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@hii,;X#@@@@Ahirh##@@@@@#@@@@##@@@@@@@
		 @@@@@;:         s@@@@@@@@@,  @@@@@@@@r :B@@@@@@@;,@@92r:55ir;;::A@@@@@#i5;...,:;,.:r,.:5SA@@@@@@@@@#@@@@@@@@
		 @@@@@@S     ;@r  :@@@@@@@h ,,.@@@@@@@    S@@@@@.  @@:          .2@@@@@@S25..:.   .:. .,.  :M@@@@@Hh9AM#@@@@@
		 @@@@@@  s@@@@@@@  ,@@@@@@. H3, ,@@@@H 2;  @@@#    @@@ .#@@@@@@@@@@@@@@@H2Br.:r;;:;:  ,,,.  .,;;rrr5A##@@@@@@
		 @@@@@:  G@@@@@@@@,;@@@@@M  @@  s.@@@X 2h  h@@  @; B@@  @@@@@@@@@@@@@@@@@@@G32G@@2r, ,:,,:.::,.,;s2GM###@@@@@
		 @@@@s  :@@@@@@@@@@M@@@@@:;r@@2,, 9@@r @@  :@r G@i 5@@  .r55SiSA#@@@@@@@@@@@@@@sS2s..:;;ss:;;;;riGGAHM#@@@@@@
		 @@@@   h@@@@@@@@@@#@@@@M rX@@@. @@@@: @@  r@ i@@B 5@X         r3@@@@@@@@@@@@#X: rs ,,s:;2;rsss5M3HH###@@@@@@
		 @@@@i ;@@@@@@:is..    :;. s@X,   r@@ ;@@;   ,@@rA :@@  X@@#@@@@@@@@@@@@@@@@@r X,:. ...  .2GHBhAMH&MMM@@@@@@@
		 @@@@@i 5@@@A2: .. .::X@X      ss B@2 2@@#   @@@r, .@@; @@@@@@@@@@@@@@@@@@@@@;.@@i  .,,;ri2ri@@@@@#@@@@@@@@@@
		 @@@@@@: ,@@@@@@@@ @@@@A  .,i@@@@ .@; 5@@@  A@@@X   @@; :@@&;2@@5H@@@@@@@@@@A .@@@&2@@@9Ss;rXAX@@@@@@@@@@@@@@
		 @@@@@@@r  3@@@@@r @@@S   X@@@@@@G @X @@@B  G@@@@:  @@,        :;H@@@@@@@@@@, ,@@@@@@@@Hh#@@H::ri#@@@@@@@@@@@
		 @@@@@@@@@ ,2XM.; &@@@B rr2@@@@@@@ .M.@@@;:@S@@@@@. #@5         555S#@@@@@@X ,h; :@@h3A@@@HM5.;i5&&@@@@@@@@@@
		 @@@@@@@@@;  2@@S G@@@Xii,G@@@@@@@@ G@@@@:@@@@@@@@@r@@@ M@@@@@@@@@@@@@@@@@@A s9        ,sS2S,;s293hA#@@@@@@@@
		 @@@@@@@@@@@@@@@rr@@@@@@.G@@@@@@@@@@&@@@2A@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##M@@@@r    ..;,  .B2,;sXi2B#@#@@@@@@@
		 @@@@@@@@@@@@@@@r.#@@@@@2 A@@@@@@@@@@@@@@@@@@@@@@;       .;i39@@2#@MBMMBM#@@@A ..   :r.  .rs::rsh@@@AAM@@@@@@
		 @@@@@@@@@B.       @@@@Br  @@@@@@@@@@@##AiGHA32XXi99r.           r3@###M###@@@. .rr  . . sX::2A@@@@##M#@@@@@@
		 @@@@@@@:   ;H##r   ;@@B   ,@@@@@@@@@@r           2@@@  @@@@@   s@#BHB#HAHM@@@@@@@@H   :s@@@@@@@@#@@@@@@@@@@@
		 @@@@@@r  5@@@@@@s   S@@5  ;@@@@@@@@M@@: i@@#@#@2@@@@@  r@@@@, .M@A&9A#@#MM##@@@@@@@@@@@@@@@@@@#HB@@@#@@@@@@@
		 @@@@@& .@@@@@@@@@#  s@@@   M@@@@@2  i@. @@@@@@@S@@@@@  ,@#@r  :3hAAM####@@##@@@@#B@@@@@@@@@@@@#B#@@@@@@@@@@@
		 @@@@@  @@@@@@@@@@@G  @@@.  :@@@@#  r@@; .2HBHHH@@@@@@ ;G:     r#@MHB##MHB#@#AM@@@@@@@@@@; rS.s@@MB#@@@@@@@@@
		 @@@@@  @@@@@@@@@@@S  #@@A   @@@3  #@@M.        ,2M@@5     ,@2@@@AMHhAAGH##@#G5#@@#A#@@@:     5@HB@@##@@@@@@@
		 @@@@H   @@@@@@@@@@;; r@@@.  S@@  :@@@@, :HAXH#@#H#H,  ,@9 ,B#@@#B###BhXM#####5H#Bs.  .::rsS,:;r:rH@@@@@@@@@@
		 @@@@M  r@@@@@@@@@M    @@@@  B@r ;@@@@@A @@@@@@@@@@; M:s@@,  H@@@@#M#@BAB###@@&A#@#hr.   :9H .:X&GHB#@@@@@@@@
		 @@@@@  ;@@@@@@@@@A  :@@@@@  r2 .@@@@@@H ,@@@h9@@BA@@@. @@2  ,22@@#@#@@BHMM##@#A#@@SXMS;. ,i;iXM#HAA#@@@@@@@@
		 @@@@@s  G@@@@@@@@s 3@@@@ M@    @@@@@@@i   .   .ir3@@@: A@@3  A;S@@@#@@@B&M##@@H#@@@X&H#9ri2X#####2A@@@@@@@@@
		 @@@@@@B   iB@@@3  r@@@@@  @i  2@@@@@@@H         ;X22@A G@@@A  @@@@@@@@@@BA##@@#H@@@@BAB&iA2rXAH3X&@@@@@@@@@@
		 @@@@@@@@9       .#@@@@@@Br@r  &@@@@@@@@.:@@@@@@@@@@@@@;@@@@@#  @@@@@@@@@@#H##@@A#@@@@@BBs&BS9HA&@@@@@@@@@@@@
		 @@@@@@@@@@@@2,,;@@@#@@@@@@@;r5;@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@  H@@@@@@@@@@B#@@@B@@@@@@@B5A&&B@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@H@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  2@@@@@@@@@@#@@@B@@@@@@@@MA#@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@H&@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			 																										"""

#********************************************************* TABLERO MAQUINA ***************************************************
#*****************************************************************************************************************************
tablero_maquina=[]
tablero_jugador1=[]
tablero_jugador2=[]
time.sleep(1)
print "Cargando............."
print ""
time.sleep(2)
os.system("clear")

#*****************************************************************************************************************************
for x in range(0,15):
	tablero_maquina.append(["O"] * 15)

#*****************************************************************************************************************************
def print_maquina(tablero_maquina):
	for fila in tablero_maquina:
		print "\t\t\t\t",
		print " | ".join(fila)

#************************************************************* BARCOS ********************************************************
#*****************************************************************************************************************************
def fila_aleatoria(tablero_maquina):
	return random.randint(0,len(tablero_maquina)-1)

def columna_aleatoria(tablero_maquina):
	return random.randint(0,len(tablero_maquina[3])-1)

def fila_aleatoria1(tablero_maquina):
	return random.randint(0,len(tablero_maquina[4])-1)

def columna_aleatoria1(tablero_maquina):
	return random.randint(0,len(tablero_maquina[1])-1)

def fila_aleatoria2(tablero_maquina):
	return random.randint(0,len(tablero_maquina[7])-1)

def columna_aleatoria2(tablero_maquina):
	return random.randint(0,len(tablero_maquina[10])-1)

#*****************************************************************************************************************************
portaaviones_fil1=fila_aleatoria(tablero_maquina)
portaaviones_col1=columna_aleatoria(tablero_maquina)

submarino_fil2=fila_aleatoria1(tablero_maquina)
submarino_col2=columna_aleatoria1(tablero_maquina)

patrullero_fil3=fila_aleatoria2(tablero_maquina)
patrullero_col3=columna_aleatoria2(tablero_maquina)
print""

#************************************************************* MAQUINA *******************************************************
#*****************************************************************************************************************************
def single_player():
	print ""
	print "\t\t\t\t\t\tLISTO, ACA EMPIEZA EL JUEGO"
	nombre_jugador=raw_input("Ingrese Su Nombre: ")
	print ""
	time.sleep(2)
	os.system("clear")
	print ""
	print " \t\t\t\t  ███╗   ███╗ █████╗  ██████╗ ██╗   ██╗██╗███╗   ██╗ █████╗  "
	print " \t\t\t\t  ████╗ ████║██╔══██╗██╔═══██╗██║   ██║██║████╗  ██║██╔══██╗ "
	print " \t\t\t\t  ██╔████╔██║███████║██║   ██║██║   ██║██║██╔██╗ ██║███████║ "
	print "  \t\t\t\t  ██║╚██╔╝██║██╔══██║██║▄▄ ██║██║   ██║██║██║╚██╗██║██╔══██║ "
	print "  \t\t\t\t  ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║██║ ╚████║██║  ██║ "
	print "  \t\t\t\t  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ "
	print ""
	print"\t\t\t\t********************DERRIBANDO BARCOS********************"
	print ""
	print "\t\t\t\tBIENVENIDO: %s"%(nombre_jugador)
	vidas=3
	total_barcos_hundidos=0
	barcos_ganados=0
	while vidas>0:
		print_maquina(tablero_maquina)
		disparos=True
		while disparos==True:
			try:
				print ""
				adivina_fila= int(input("\t\t\t\tAdivina fila: "))
				adivina_columna = int(input("\t\t\t\tAdivina columna: "))
				break
				print_maquina(tablero_maquina)
			except:
				print "Fatal Error, no se permiten letras."

		if (adivina_fila==portaaviones_fil1 and adivina_columna==portaaviones_col1):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			total_barcos_hundidos += 1
			print " Barcos Derribados: ", total_barcos_hundidos
			tablero_maquina[adivina_fila][adivina_columna]="X"

		elif (adivina_fila==submarino_fil2 and adivina_columna==submarino_col2):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			total_barcos_hundidos += 1
			print " Barcos Derribados: ", total_barcos_hundidos
			tablero_maquina[adivina_fila][adivina_columna]="X"

		elif (adivina_fila==patrullero_fil3 and adivina_columna==patrullero_col3):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			total_barcos_hundidos += 1
			print " Barcos Derribados: ", total_barcos_hundidos
			tablero_maquina[adivina_fila][adivina_columna]="X"
			break
			
			if total_barcos_hundidos==3:
				print "¡GENIAL! HAZ HUNDIDO TODOS MIS BARCOS"
				total_barcos_hundidos += 3
				ganaste()
				break
				print ""

		else:
			if (adivina_fila < 0 or adivina_fila > 14) or (adivina_columna < 0 or adivina_columna > 14):
				print "Vaya, estas loco, estas coordenada no se encuentra en el océano."
			elif(tablero_maquina[adivina_fila][adivina_columna] == "%" or tablero_maquina[adivina_fila][adivina_columna]=="x"):
				print "Ya repetiste esta opcion, vuelve a intentarlo."
			else:
				print "¡AAAAAAA! ¡Estuviste cerca de darle a mi barco!"
				print ""
			while disparos==True:
				try:
					tablero_maquina[adivina_fila][adivina_columna]="%"
					break
				except:
					print "Solo se permiten coordenadas validas"
					break
			vidas = vidas -1
		time.sleep(1)
		os.system("clear")
		print ""
		print u"\t\t\t\t************************* VIDAS RESTANTES %s *************************"%(vidas)
	print ""

#******************************************************** MULTIPLAYER ************************************************
#*********************************************************************************************************************
#*********************************************************************************************************************
	for x in range(0,14):
		tablero_jugador2.append(["O"] * 15)

	for x in range(0,14):
		tablero_jugador1.append(["O"] * 15)
	os.system("clear")

#**************************************************** BARCOS JUGADOR 1 ***********************************************
#*********************************************************************************************************************
	def fil_aleatoria1(tablero_jugador1):
		return random.randint(0,len(tablero_jugador1)-1)

	def col_aleatoria1(tablero_jugador1):
		return random.randint(0,len(tablero_jugador1[3])-1)

	def fil_aleatoria2(tablero_jugador1):
		return random.randint(0,len(tablero_jugador1[4])-1)

	def col_aleatoria2(tablero_jugador1):
		return random.randint(0,len(tablero_jugador1[1])-1)

	def fil_aleatoria3(tablero_jugador1):
		return random.randint(0,len(tablero_jugador1[7])-1)

	def col_aleatoria3(tablero_jugador1):
		return random.randint(0,len(tablero_jugador1[10])-1)

	portaaviones1_fil1=fil_aleatoria1(tablero_jugador1)
	portaaviones1_col1=col_aleatoria1(tablero_jugador1)

	submarino2_fil2=fil_aleatoria2(tablero_jugador1)
	submarino2_col2=col_aleatoria2(tablero_jugador1)

	patrullero3_fil3=fil_aleatoria3(tablero_jugador1)
	patrullero3_col3=col_aleatoria3(tablero_jugador1)
	print""

#**************************************************** BARCOS JUGADOR 2 ***********************************************
#*********************************************************************************************************************
	def fil_ale1(tablero_jugador2):
		return random.randint(0,len(tablero_jugador2)-1)

	def col_ale1(tablero_jugador2):
		return random.randint(0,len(tablero_jugador2[3])-1)

	def fil_ale2(tablero_jugador2):
		return random.randint(0,len(tablero_jugador2[4])-1)

	def col_ale2(tablero_jugador2):
		return random.randint(0,len(tablero_jugador2[1])-1)

	def fil_ale3(tablero_jugador2):
		return random.randint(0,len(tablero_jugador2[7])-1)

	def col_ale3(tablero_jugador2):
		return random.randint(0,len(tablero_jugador2[10])-1)

	carrier_f1=fil_ale1(tablero_jugador2)
	carrier_c2=col_ale1(tablero_jugador2)

	submarine_f2=fil_ale2(tablero_jugador2)
	submarine_c2=col_ale2(tablero_jugador2)

	patrol_boat_f1=fil_ale3(tablero_jugador2)
	patrol_boat_c1=col_ale3(tablero_jugador2)

#******************************************************************************************************************
	def print_jugador2(tablero_jugador2):
		for fila in tablero_jugador2:
			print " \ ".join(fila)
	print_jugador2(tablero_jugador2)

#******************************************************************************************************************
	def print_jugador1(tablero_jugador1):
		for fila in tablero_jugador1:
			print " / ".join(fila)
	os.system("clear")
	print ""
	print "\t\t\t\t\t\t\tJuguemos batalla naval"
	print ""
	time.sleep(1)
	os.system("clear")
#******************************************************************************************************************
	def multiplayer():
		for x in range(0,15):
			tablero_jugador1.append(["O"] * 15)
#****************************************************** JUGADOR 1 *************************************************
#******************************************************************************************************************
	print ""
	ingreso_nombre_jugador=raw_input("Ingrese su Nombre, jugador 1: ")
	print ""
	time.sleep(1)
	os.system("clear")
	print "BIENVENIDO: %s"%(ingreso_nombre_jugador)
	print""
	print "Esperamos que se divierta XD."
	time.sleep(2)
	os.system("clear")
	print ""
	print"\t\t\t\t\t\t\t\tTURNO JUGADOR 1"
	ganados=0
	barcos_derribados=0
	turnos1=3
	while turnos1>0:
		print ""
		print_jugador1(tablero_jugador1)
		disparos1=True
		while disparos1==True:
			try:
				print ""
				adivina_fila= int(input("Adivina fila: "))
				adivina_columna = int(input("Adivina columna: "))
				break
				print_jugador1(tablero_jugador1)
			except:
				print "Fatal Error, no se permiten letras."
		os.system("clear")

		if (adivina_fila== portaaviones1_fil1 and adivina_columna== portaaviones1_col1):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			barcos_derribados += 1
			print "Barcos Derribados: ", barcos_derribados
			tablero_jugador2[adivina_fila][adivina_columna]="X"

		elif (adivina_fila== submarino2_fil2 and adivina_columna== submarino2_col2):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			barcos_derribados += 1
			print " Barcos Derribados: ", barcos_derribados
			tablero_jugador2[adivina_fila][adivina_columna]="X"

		elif (adivina_fila== patrullero3_fil3 and adivina_columna== patrullero3_col3):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			barcos_derribados += 1
			print " Barcos Derribados: ", barcos_derribados
			tablero_jugador2[adivina_fila][adivina_columna]="X"
			break

			if barcos_derribados==3:
				print "¡GENIAL! HAZ HUNDIDO TODOS MIS BARCOS"
				barcos_derribados +=3
				ganaste()
				break
				print""
		else:
			if (adivina_fila < 0 or adivina_fila > 14) or (adivina_columna < 0 or adivina_columna > 14):
				print "Vaya, estas loco, estas coordenada no se encuentra en el Oceano."
			elif(tablero_jugador2[adivina_fila][adivina_columna] == "5" or tablero_jugador2[adivina_fila][adivina_columna]=="X"):
				print "Ya repetiste esta opcion, vuelve a intentarlo."
			else:
				print "¡AAAAAAA! ¡Estuviste cerca de darle a mi barco!"
				tablero_jugador2[adivina_fila][adivina_columna]="5"
				os.system("clear")
			while disparos1==True:
				try:
					tablero_jugador2[adivina_fila][adivina_columna]="5"
					break
				except:
					print "Solo se permiten coordenadas validas"
					break
			turnos1 = turnos1 -1
			print "Se termino tu turno."
			os.system("clear")
			break
			print jugador2
			print_jugador2(tablero_jugador2)
			print ""
		print u"\t\t\t\t************************* TURNOS RESTANTES %s *************************"%(turnos1)
	print ""

#****************************************************** JUGADOR 2 *************************************************
#******************************************************************************************************************
	print ""
	ingreso_nombre_jugador2=raw_input("Ingrese su Nombre, jugador 2: ")
	print ""
	time.sleep(1)
	os.system("clear")
	print "BIENVENIDO: %s"%(ingreso_nombre_jugador)
	print ""
	print "Esperamos que se divierta XD."
	time.sleep(2)
	os.system("clear")
	print ""
	print"\t\t\t\t\t\t\t\tTURNO JUGADOR 2"
	ganados=0
	barcos_derribados1=0
	turnos1=3
	while turnos1>0:
		print ""
		print_jugador2(tablero_jugador2)
		disparos1=True
		while disparos1==True:
			try:
				print ""
				adivina_fila= int(input("Adivina fila: "))
				adivina_columna = int(input("Adivina columna: "))
				break
				print_jugador2(tablero_jugador2)
			except:
				print "Fatal Error, no se permiten letras."
		os.system("clear")

		if (adivina_fila== carrier_f1 and adivina_columna== carrier_c2):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			barcos_derribados1 += 1
			print "Barcos Derribados: ", barcos_derribados
			tablero_jugador1[adivina_fila][adivina_columna]="X"

		elif (adivina_fila== submarine_f2 and adivina_columna== submarine_c2):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			barcos_derribados1 += 1
			print " Barcos Derribados: ", barcos_derribados
			tablero_jugador1[adivina_fila][adivina_columna]="X"

		elif (adivina_fila== patrol_boat_f1 and adivina_columna== patrol_boat_c1):
			print "¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			barcos_derribados1 += 1
			print " Barcos Derribados: ", barcos_derribados
			tablero_jugador1[adivina_fila][adivina_columna]="X"
			break

			if barcos_derribados1==3:
				print "¡GENIAL! HAZ HUNDIDO TODOS MIS BARCOS"
				barcos_derribados1 +=3
				ganaste()
				break
				print""
		else:
			if (adivina_fila < 0 or adivina_fila > 14) or (adivina_columna < 0 or adivina_columna > 14):
				print "Vaya, estas loco, estas coordenada no se encuentra en el Oceano."
			elif(tablero_jugador1[adivina_fila][adivina_columna] == "5" or tablero_jugador1[adivina_fila][adivina_columna]=="X"):
				print "Ya repetiste esta opcion, vuelve a intentarlo."
			else:
				print "¡AAAAAAA! ¡Estuviste cerca de darle a mi barco!"
				tablero_jugador1[adivina_fila][adivina_columna]="5"

			while disparos1==True:
				try:
					tablero_jugador1[adivina_fila][adivina_columna]="5"
					break
				except:
					print "Solo se permiten coordenadas validas"
					break
			turnos1 = turnos1 -1
			print "Se termino tu turno."
			break
			print jugador1
			print_jugador1(tablero_jugador1)
			print ""
		print u"\t\t\t\t************************* TURNOS RESTANTES %s *************************"%(turnos1)
	print ""

#******************************************************************************************************************
#********************************************************************************************************************
#***************************************************** MENU *********************************************************
#********************************************************************************************************************
opcion_menu=True
while opcion_menu==True:
	print "                                       ___         ___         ___         ___      "
	print "                                      /__/\       /  /\       /__/\       /__/\     "   
	print "                                     |  |::\     /  /:/_      \  \:\      \  \:\    "  
	print "                                     |  |:|:\   /  /:/ /\      \  \:\      \  \:\   "
	print "                                   __|__|:|\:\ /  /:/ /:/_ _____\__\:\ ___  \  \:\  "
	print "                                  /__/::::| \:/__/:/ /:/ //__/::::::::/__/\  \__\:\ "
	print "                                  \  \:\~~\__\\  \:\/:/ /:\  \:\~~\~~\\  \:\ /  /:/ "
	print "                                   \  \:\      \  \::/ /:/ \  \:\  ~~~ \  \:\  /:/  "
	print "                                    \  \:\      \  \:\/:/   \  \:\      \  \:\/:/   "
	print "                                     \  \:\      \  \::/     \  \:\      \  \::/    "
	print "                                      \__\/       \__\/       \__\/       \__\/     "
	print "                                                                                    " 
	print ""
	print "BIENVENIDOS A SU JUEGO BATALLA NAVAL"
	print ""
	print "¡¡¡ESPERAMOS SE DIVIERTA XD!!!"
	print ""
	print "1) Instrucciones: "
	print "2) Single Player: "
	print "3) Multiplayer:   "
	print ""
	opcion=raw_input("Desea elegir una opción? ")
	print ""
	try:
		if opcion.isalpha()==False:
			if opcion.lower()=="1":
				print "Has escogido la opción 1."
				time.sleep(1)
				os.system("clear")
				instrucciones()
				valido=True
				while valido==True:
					regresar=raw_input("Le gustaria regresar al menú SI/NO: ")
					print ""
					os.system("clear")
					try:
						if regresar.isalpha()==True:
							if regresar.lower()=="si":
								valido=False
							elif regresar.lower()=="no":
								opcion_menu=False
								print "GRACIAS POR JUGAR BATALLA NAVAL."
								break
						else:
							print "FATAL ERROR, datos no validos."
					except:
						print "No se aceptan valores alfanúmericos."
	except:
		print "GRACIAS POR JUGAR BATALLA NAVAL."

	try:
		if opcion.isalpha()==False:
			if opcion.lower()=="2":
				print "Has escogido la opción 2."
				time.sleep(1)
				os.system("clear")
				single_player()
				valido=True
				while valido==True:
					regresar=("Le gustaria regresar al menú SI/NO: ")
					print ""
					os.system("clear")
					try:
						if regresar.isalpha()==True:
							if regresar.lower()=="si":
								opcion_menu=False
							elif regresar.lower()=="no":
								opcion_menu=False
								print "GRACIAS POR JUGAR BATALLA NAVAL."
								break
						else:
							print "FATAL ERROR, datos no validos."
					except:
						print "No se aceptan valores alfanúmericos" 
	except:
		print "GRACIAS POR JUGAR BATALLA NAVAL."
		print ""
	try:
		if opcion.isalpha()==False:
			if opcion.lower()=="3":
				print "Has escogido la opción 3."
				time.sleep(1)
				os.system("clear")
				multiplayer()
				valido=True
				while valido==True:
					regresar=("Le gustaria regresar al menú SI/NO: ")
					print ""
					os.system("clear")
					try:
						if regresar.isalpha()==True:
							if regresar.lower()=="si":
								opcion_menu=False
							elif regresar.lower()=="no":
								opcion_menu=False
								print "GRACIAS POR JUGAR BATALLA NAVAL."
								break
						else:
							print "Datos no validos."
					except:
						print "No se aceptan valores alfanúmericos." 
	except:
		print "GRACIAS POR JUGAR BATALLA NAVAL."


