#-*- coding: utf-8 -*-
import random
import os 
import time
import sys

def sonido():
	try:
		import pygame
		pygame.init()
		pygame.display.set_mode((1,1))
		pygame.mixer.music.load("Obertura_Xanandra.mp3")
		pygame.mixer.music.play()
	except:
		print "no se encontro la libreria."	


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
	sonido()
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
    print "\t\t\t\t:'######::::::'###::::'##::::'##:'########:  "
    print "\t\t\t\t'##... ##::::'## ##::: ###::'###: ##.....::  "
    print "\t\t\t\t ##:::..::::'##:. ##:: ####'####: ##:::::::  "
    print "\t\t\t\t ##::'####:'##:::. ##: ## ### ##: ######:::  "
    print "\t\t\t\t ##::: ##:: #########: ##. #: ##: ##...::::  "
    print "\t\t\t\t ##::: ##:: ##.... ##: ##:.:: ##: ##::::::: "
    print "\t\t\t\t . ######::: ##:::: ##: ##:::: ##: ########: "
    print "\t\t\t\t :......::::..:::::..::..:::::..::........:: "
    print ""
    print "\t\t\t\t :'#######::'##::::'##:'########:'########:: "
    print "\t\t\t\t '##.... ##: ##:::: ##: ##.....:: ##.... ##: "
    print "\t\t\t\t  ##:::: ##: ##:::: ##: ##::::::: ##:::: ##: "
    print "\t\t\t\t  ##:::: ##: ##:::: ##: ######::: ########:: "
    print "\t\t\t\t  ##:::: ##:. ##:: ##:: ##...:::: ##.. ##::: "
    print "\t\t\t\t  ##:::: ##::. ## ##::: ##::::::: ##::. ##:: "
    print "\t\t\t\t . #######::::. ###:::: ########: ##:::. ##: "
    print "\t\t\t\t :.......::::::...:::::........::..:::::..:: " 

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
	print ""
	nombre_jugador=raw_input("Ingrese Su Nombre: ")
	print ""
	time.sleep(2)
	os.system("clear")
	def maquina():
		print ""
		print " \t\t\t\t  ███╗   ███╗ █████╗  ██████╗ ██╗   ██╗██╗███╗   ██╗ █████╗  "
		print " \t\t\t\t  ████╗ ████║██╔══██╗██╔═══██╗██║   ██║██║████╗  ██║██╔══██╗ "
		print " \t\t\t\t  ██╔████╔██║███████║██║   ██║██║   ██║██║██╔██╗ ██║███████║ "
		print "  \t\t\t\t  ██║╚██╔╝██║██╔══██║██║▄▄ ██║██║   ██║██║██║╚██╗██║██╔══██║ "
		print "  \t\t\t\t  ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║██║ ╚████║██║  ██║ "
		print "  \t\t\t\t  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ "
	maquina()

	print ""
	print "\t\t\t\tBIENVENIDO: %s"%(nombre_jugador)
	print ""
	print"\t\t\t\t********************* DERRIBANDO BARCOS *********************"
	vidas=0
	total_barcos_hundidos=0
	barcos_ganados=0
	for vidas in range(3):
		print ""
		print_maquina(tablero_maquina)
		print ""
		disparos=True
		while disparos==True:
			try:
				print ""
				adivina_fila= int(input("\t\t\t\tAdivina fila: "))
				adivina_columna = int(input("\t\t\t\tAdivina columna: "))
				print ""
				break
			except:
				print ""
				print "\t\t\t\tFatal Error, no se permiten letras."
				print ""

		if (adivina_fila==portaaviones_fil1 and adivina_columna==portaaviones_col1):
			print ""
			print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			total_barcos_hundidos += 1
			vidas += 1
			print ""
			print "\t\t\t\tRESTO VIDAS: ", vidas
			print ""
			print "\t\t\t\tBarcos Derribados: ", total_barcos_hundidos
			print ""
			tablero_maquina[adivina_fila][adivina_columna]="X"
			time.sleep(2)
			os.system("clear")

		elif (adivina_fila==submarino_fil2 and adivina_columna==submarino_col2):
			print ""
			print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			total_barcos_hundidos += 1
			vidas += 1
			print ""
			print "\t\t\t\tRESTO VIDAS: ", vidas
			print ""
			print "\t\t\t\tBarcos Derribados: ", total_barcos_hundidos
			print ""
			tablero_maquina[adivina_fila][adivina_columna]="X"
			time.sleep(2)
			os.system("clear")


		elif (adivina_fila==patrullero_fil3 and adivina_columna==patrullero_col3):
			print ""
			print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
			total_barcos_hundidos += 1
			vidas += 1
			print ""
			print "\t\t\t\tRESTO VIDAS: ", vidas
			print ""
			print "\t\t\t\tBarcos Derribados: ", total_barcos_hundidos
			print ""
			tablero_maquina[adivina_fila][adivina_columna]="X"
			time.sleep(2)
			os.system("clear")
			
			if total_barcos_hundidos==3:
				os.system("clear")
				print ""
				barcos_ganados += 1
				print "\t\t\t\tHAS DERRIBADO : ",ganados
				print ""
				print "\t\t\t\t¡GENIAL! HAZ HUNDIDO TODOS MIS BARCOS"
				ganaste()
				break
				print ""
				print_maquina(tablero_maquina)

		else:
			while disparos==True:
				try:
					if(tablero_maquina[adivina_fila][adivina_columna] == "%" ) or (tablero_maquina[adivina_fila][adivina_columna] == "X"):
						vidas +=1
						print ""						
						print "\t\t\t\tVIDAS RESTANTES: ", vidas
						print ""
						print "\t\t\t\tYa repetiste esta opcion, vuelve a intentarlo."
						break

					else:
						print "\t\t\t\t¡AAAAAAA! ¡Estuviste cerca de darle a mi barco!"
						vidas +=1
						print ""
						print "\t\t\t\tVIDAS RESTANTES: ", vidas
						print ""
						tablero_maquina[adivina_fila][adivina_columna]="%"
						time.sleep(2)
						os.system("clear")
						maquina()
						print "\t\t\t\tBIENVENIDO: %s"%(nombre_jugador)
						print ""
						print"\t\t\t\t********************* DERRIBANDO BARCOS *********************"
						break
				except:
					print ""
					print "\t\t\t\tVaya, estas loco, estas coordenada no se encuentra en el océano."
					time.sleep(2)
					os.system("clear")
					break

			if vidas==3:
				perdido=0
				os.system("clear")
				perdido +=1
				perdiste()
				time.sleep(3)
				os.system("clear")

#******************************************************** MULTIPLAYER ************************************************
#*********************************************************************************************************************
#*********************************************************************************************************************
for x in range(0,14):
    tablero_jugador2.append(["O"] * 15)

for x in range(0,14):
    tablero_jugador1.append(["O"] * 15)         
os.system('clear')


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
    	print "\t\t\t\t",
        print " \ ".join(fila)
print_jugador2(tablero_jugador2)

#******************************************************************************************************************
def print_jugador1(tablero_jugador1):
    for fila in tablero_jugador1:
    	print "\t\t\t\t",
        print " / ".join(fila)
os.system("clear")
print """
            
     ▄█ ███    █▄     ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄    ▄██████▄     ▄████████ 
    ███ ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███ 
    ███ ███    ███   ███    █▀    ███    █▀  ███   ███   ███ ███    ███   ███    █▀  
    ███ ███    ███  ▄███         ▄███▄▄▄     ███   ███   ███ ███    ███   ███        
    ███ ███    ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███   ███ ███    ███ ▀███████████ 
    ███ ███    ███   ███    ███   ███    █▄  ███   ███   ███ ███    ███          ███ 
    ███ ███    ███   ███    ███   ███    ███ ███   ███   ███ ███    ███    ▄█    ███ 
█▄ ▄███ ████████▀    ████████▀    ██████████  ▀█   ███   █▀   ▀██████▀   ▄████████▀  
▀▀▀▀▀▀                                                                               

				▀█████████▄     ▄████████     ███        ▄████████  ▄█        ▄█          ▄████████ 
				  ███    ███   ███    ███ ▀█████████▄   ███    ███ ███       ███         ███    ███ 
				  ███    ███   ███    ███    ▀███▀▀██   ███    ███ ███       ███         ███    ███ 
				 ▄███▄▄▄██▀    ███    ███     ███   ▀   ███    ███ ███       ███         ███    ███ 
				▀▀███▀▀▀██▄  ▀███████████     ███     ▀███████████ ███       ███       ▀███████████ 
				  ███    ██▄   ███    ███     ███       ███    ███ ███       ███         ███    ███ 
				  ███    ███   ███    ███     ███       ███    ███ ███▌    ▄ ███▌    ▄   ███    ███ 
				▄█████████▀    ███    █▀     ▄████▀     ███    █▀  █████▄▄██ █████▄▄██   ███    █▀  
				                                                   ▀         ▀                      
										███▄▄▄▄      ▄████████  ▄█    █▄     ▄████████  ▄█       
										███▀▀▀██▄   ███    ███ ███    ███   ███    ███ ███       
										███   ███   ███    ███ ███    ███   ███    ███ ███       
										███   ███   ███    ███ ███    ███   ███    ███ ███       
										███   ███ ▀███████████ ███    ███ ▀███████████ ███       
										███   ███   ███    ███ ███    ███   ███    ███ ███       
										███   ███   ███    ███ ███    ███   ███    ███ ███▌    ▄ 
										 ▀█   █▀    ███    █▀   ▀██████▀    ███    █▀  █████▄▄██ 
										                                               ▀         
"""
print ""
time.sleep(4)
os.system("clear")
#******************************************************************************************************************
def multiplayer():
    
#****************************************************** JUGADOR 1 *************************************************
#******************************************************************************************************************
    print ""
    ingreso_nombre_jugador=raw_input("Ingrese su Nombre, jugador 1: ")
    print ""
    time.sleep(2)
    os.system("clear")
    print "\t\t\t\t\t\tLISTO, ACA EMPIEZA EL JUEGO"
    time.sleep(2)
    os.system("clear")
    print "Esperamos que se divierta XD."
    print ""
    time.sleep(1)
    os.system("clear")
    def jugador1():
    	print "\t\t\t\t       _                       _              __ "
    	print "\t\t\t\t      | |                     | |            /_ |"
    	print "\t\t\t\t      | |_   _  __ _  __ _  __| | ___  _ __   | |"
    	print "\t\t\t\t  _   | | | | |/ _` |/ _` |/ _` |/ _ \| '__|  | |"
    	print "\t\t\t\t | |__| | |_| | (_| | (_| | (_| | (_) | |     | |"
    	print "\t\t\t\t  \____/ \__,_|\__, |\__,_|\__,_|\___/|_|     |_|"
    	print "\t\t\t\t               __/ |                             "
    	print "\t\t\t\t              |___/                              "                                             
    jugador1()
    print "\t\t\t\tBIENVENIDO: %s"%(ingreso_nombre_jugador)
    print ""
    print"\t\t\t\t********************** JUGADOR 1 **********************"
    print ""
    print"\t\t\t\t\t\t\tTURNO JUGADOR 1"
    turnos1=0
    barcos_hundidos1=0
    barcos_ganados1=0
    for turnos1 in range(3):

    	print ""
    	print_jugador1(tablero_jugador1)
    	print ""
    	disparos1=True
    	while disparos1==True:
    		try:
    			print ""
    			adivina_fila= int(input("\t\t\t\tAdivina fila: "))
    			adivina_columna = int(input("\t\t\t\tAdivina columna: "))
    			print ""
    			break
    		except:
    			print ""
    			print "\t\t\t\tFatal Error, no se permiten letras."
    			print ""

    	if (adivina_fila==portaaviones1_fil1 and adivina_columna==portaaviones1_col1):
    		print ""
    		print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
    		barcos_hundidos1 += 1
    		turnos1 += 1
    		print ""
    		print "\t\t\t\tRESTO TURNOS: ", turnos1
    		print ""
    		print "\t\t\t\tBarcos Derribados: ", barcos_hundidos1
    		print ""
    		tablero_jugador2[adivina_fila][adivina_columna]="X"
    		time.sleep(2)
    		os.system("clear")

    	elif (adivina_fila==submarino2_fil2 and adivina_columna==submarino2_col2):
    		print ""
    		print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
    		barcos_hundidos1 += 1
    		turnos1 += 1
    		print ""
    		print "\t\t\t\tRESTO TURNOS: ", turnos1
    		print ""
    		print "\t\t\t\tBarcos Derribados: ", barcos_hundidos1
    		print ""
    		tablero_jugador2[adivina_fila][adivina_columna]="X"
    		time.sleep(2)
    		os.system("clear")


    	elif (adivina_fila==patrullero3_fil3 and adivina_columna==patrullero3_col3):
    		print ""
    		print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
    		barcos_hundidos1 += 1
    		turnos1 += 1
    		print ""
    		print "\t\t\t\tRESTO TURNOS: ", turnos1
    		print ""
    		print "\t\t\t\tBarcos Derribados: ", barcos_hundidos1
    		print ""
    		tablero_jugador2[adivina_fila][adivina_columna]="X"
    		time.sleep(2)
    		os.system("clear")
    		
    		if barcos_hundidos1==3:
    			os.system("clear")
    			print ""
    			barcos_ganados1 += 1
    			print "\t\t\t\tHAS DERRIBADO : ", barcos_ganados1
    			print ""
    			print "\t\t\t\t¡GENIAL! HAZ HUNDIDO TODOS MIS BARCOS"
    			ganaste()
    			break
    			print ""
    			print_jugador2(tablero_jugador2)

    	else:
    		while disparos1==True:
    			try:
    				if(tablero_jugador2[adivina_fila][adivina_columna] == "5" ) or (tablero_jugador1[adivina_fila][adivina_columna] == "X"):
    					turnos1 +=1
    					print ""						
    					print "\t\t\t\tTURNOS RESTANTES: ", turnos1
    					print ""
    					print "\t\t\t\tYa repetiste esta opcion, vuelve a intentarlo."
    					break

    				else:
    					print "\t\t\t\t¡AAAAAAA! ¡Estuviste cerca de darle a mi barco!"
    					turnos1 +=1
    					print ""
    					print "\t\t\t\tTURNOS RESTANTES: ", turnos1
    					print ""
    					tablero_jugador2[adivina_fila][adivina_columna]="%"
    					time.sleep(3)
    					os.system("clear")
    					jugador1()
    					print "\t\t\t\tBIENVENIDO: %s"%(ingreso_nombre_jugador)
    					print ""
    					print"\t\t\t\t********************** JUGADOR 1 **********************"
    					
    					break
    			except:
    				print ""
    				print "\t\t\t\tVaya, estas loco, estas coordenada no se encuentra en el océano."
    				time.sleep(2)
    				os.system("clear")
    				

    		if turnos1==3:
    			perdidos=0
    			os.system("clear")
    			perdidos +=1
    			perdiste()
    			time.sleep(3)
    			os.system("clear")

#****************************************************** JUGADOR 2 *************************************************
#******************************************************************************************************************
    print ""
    ingreso_nombre_jugador2=raw_input("Ingrese su Nombre, jugador 2: ")
    print ""
    time.sleep(1)
    os.system("clear")
    print ""
    print "Esperamos que se divierta XD."
    time.sleep(2)
    os.system("clear")
    def jugador2():
    	print"\t\t\t\t             _                       _              ___  "
    	print"\t\t\t\t            | |                     | |            |__ \ "
    	print"\t\t\t\t            | |_   _  __ _  __ _  __| | ___  _ __     ) | "
    	print"\t\t\t\t        _   | | | | |/ _` |/ _` |/ _` |/ _ \| '__|   / /  "
    	print"\t\t\t\t       | |__| | |_| | (_| | (_| | (_| | (_) | |     / /_  "
    	print"\t\t\t\t        \____/ \__,_|\__, |\__,_|\__,_|\___/|_|    |____| "
    	print"\t\t\t\t                      __/ |                               "
    	print"\t\t\t\t                     |___/                                "
    jugador2()
    print ""
    print "\t\t\t\tBIENVENIDO: %s"%(ingreso_nombre_jugador2)
    print ""
    print"\t\t\t\t********************** JUGADOR 2 **********************"
    print ""
    print"\t\t\t\t\t\t\tTURNO JUGADOR 2"
    turnos2=0
    barcos_hundidos2=0
    barcos_ganados2=0
    for turnos2 in range(3):
    	print ""
    	print_jugador2(tablero_jugador2)
    	print ""
    	disparos2=True
    	while disparos2==True:
    		try:
    			print ""
    			adivina_fila= int(input("\t\t\t\tAdivina fila: "))
    			adivina_columna = int(input("\t\t\t\tAdivina columna: "))
    			print ""
    			break
    		except:
    			print ""
    			print "\t\t\t\tFatal Error, no se permiten letras."
    			print ""

    	if (adivina_fila==carrier_f1 and adivina_columna==carrier_f2):
    		print ""
    		print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
    		barcos_hundidos2 += 1
    		turnos2 += 1
    		print ""
    		print "\t\t\t\tRESTO TURNOS: ", turnos2
    		print ""
    		print "\t\t\t\tBarcos Derribados: ", barcos_hundidos2
    		print ""
    		tablero_jugador1[adivina_fila][adivina_columna]="X"
    		time.sleep(2)
    		os.system("clear")

    	elif (adivina_fila==submarino2_fil2 and adivina_columna==submarino2_col2):
    		print ""
    		print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
    		barcos_hundidos2 += 1
    		turnos2 += 1
    		print ""
    		print "\t\t\t\tRESTO TURNOS: ", turnos2
    		print ""
    		print "\t\t\t\tBarcos Derribados: ", barcos_hundidos2
    		print ""
    		tablero_jugador1[adivina_fila][adivina_columna]="X"
    		time.sleep(2)
    		os.system("clear")


    	elif (adivina_fila==patrol_boat_f1 and adivina_columna==patrol_boat_c1):
    		print ""
    		print "\t\t\t\t¡Genial! ¡Sigue asi, le has dado a uno de mis Barcos!"
    		barcos_hundidos2 += 1
    		turnos2 += 1
    		print ""
    		print "\t\t\t\tRESTO TURNOS: ", turnos2
    		print ""
    		print "\t\t\t\tBarcos Derribados: ", barcos_hundidos2
    		print ""
    		tablero_jugador1[adivina_fila][adivina_columna]="X"
    		time.sleep(2)
    		os.system("clear")
    		
    		if barcos_hundidos2==3:
    			os.system("clear")
    			print ""
    			barcos_ganados2 += 1
    			print "\t\t\t\tHAS DERRIBADO : ", barcos_ganados2
    			print ""
    			print "\t\t\t\t¡GENIAL! HAZ HUNDIDO TODOS MIS BARCOS"
    			ganaste()
    			break
    			print ""
    			print_jugador1(tablero_jugador1)

    	else:
    		while disparos2==True:
    			try:
    				if(tablero_jugador1[adivina_fila][adivina_columna] == "+" ) or (tablero_jugador2[adivina_fila][adivina_columna] == "X"):
    					turnos2 +=1
    					print ""						
    					print "\t\t\t\tTURNOS RESTANTES: ", turnos2
    					print ""
    					print "\t\t\t\tYa repetiste esta opcion, vuelve a intentarlo."
    					break

    				else:
    					print "\t\t\t\t¡AAAAAAA! ¡Estuviste cerca de darle a mi barco!"
    					turnos2 +=1
    					print ""
    					print "\t\t\t\tTURNOS RESTANTES: ", turnos2
    					print ""
    					tablero_jugador1[adivina_fila][adivina_columna]="+"
    					time.sleep(3)
    					os.system("clear")
    					break
    			except:
    				print ""
    				print "\t\t\t\tVaya, estas loco, estas coordenada no se encuentra en el océano."
    				time.sleep(2)
    				os.system("clear")
    				jugador2()
    				print "\t\t\t\tBIENVENIDO: %s"%(ingreso_nombre_jugador2)
    				print ""
    				print"\t\t\t\t********************** JUGADOR 2 **********************"
    				break

    		if turnos2==3:
    			perdidos2=0
    			os.system("clear")
    			perdidos2 +=1
    			perdiste()
    			time.sleep(3)
    			os.system("clear")

#********************************************************************************************************************
#********************************************************************************************************************
#***************************************************** MENU *********************************************************
#********************************************************************************************************************
class opciones():
	menu=True
	while menu==True:
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
						print""
						regresar=raw_input("Le gustaria regresar al menú SI/NO: ")
						print""
						try:
							if regresar.isalpha()==True:
								if regresar.lower()=="si":
									valido=False
								elif regresar.lower()=="no":
									menu=False
									print "GRACIAS POR JUGAR BATALLA NAVAL."
									break
							else:
								print "FATAL ERROR, datos no validos."
						except:
							print "No se aceptan valores alfanúmericos."
		except:
			print "GRACIAS POR JUGAR BATALLA NAVAL."
		time.sleep(2)
		os.system("clear")

		try:
			if opcion.isalpha()==False:
				if opcion.lower()=="2":
					print "Has escogido la opción 2."
					time.sleep(1)
					os.system("clear")
					single_player()
					valido=True
					while valido==True:
						print""
						regresar=raw_input("Le gustaria regresar al menú SI/NO: ")
						print""
						try:
							if regresar.isalpha()==True:
								if regresar.lower()=="si":
									valido=False
								elif regresar.lower()=="no":
									menu=False
									print "GRACIAS POR JUGAR BATALLA NAVAL."
									break
							else:
								print "FATAL ERROR, datos no validos."
						except:
							print "No se aceptan valores alfanúmericos."
		except:
			print "GRACIAS POR JUGAR BATALLA NAVAL."
		time.sleep(3)
		os.system("clear")

		try:
			if opcion.isalpha()==False:
				if opcion.lower()=="3":
					print "Has escogido la opción 3."
					time.sleep(1)
					os.system("clear")
					multiplayer()
					valido=True
					while valido==True:
						print""
						regresar=raw_input("Le gustaria regresar al menú SI/NO: ")
						print""
						try:
							if regresar.isalpha()==True:
								if regresar.lower()=="si":
									valido=False
								elif regresar.lower()=="no":
									menu=False
									print "GRACIAS POR JUGAR BATALLA NAVAL."
									break
							else:
								print "FATAL ERROR, datos no validos."
						except:
							print "No se aceptan valores alfanúmericos."
		except:
			print "GRACIAS POR JUGAR BATALLA NAVAL."
		time.sleep(2)
		os.system("clear")
opciones()