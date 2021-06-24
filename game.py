
################################# Project Name #################################
""" Multiplayer Car Racing Game using Python and Pygame """


##################################################################
# importing important modules
import pygame   	# It will import all the pygame modules
import random    	# It will generate random numbers
	

##################################################################
# initialize all the pygame module
''' It will initialize all the pygame sub module and returns the number of successful initialization and fail initialization '''
pygame.init()


##################################################################
# colors used in rgb format
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)	
green = (0,255,0)
silver = (192,192,192)
light_blue = (0,191,255)
navy = (0,0,128)
lime_green = (50,205,50)
crimsion = (220,20,60)
button_1 = (51,0,102)
button1_1 = (76,0,153)
block_color = (244,164,96)
block_color2 = (205,133,63)
block_color3 = (160,82,45)


##################################################################
# global variables used in the game
window_width = 1366
window_height = 768
x_car = 10  
y_car = 540
x_change = 0
y_change = 0
car_width = 75
car_height = 150
speed = 3
score = 0
score_1 = 0
score_2 = 0
road_width = 455
road_height = 768
exit_2 = False
pause = False

	
##################################################################
# loading images and transforming them so, that we can use it accordingly
logo_image = pygame.image.load("logo.png")
logo_image = pygame.transform.scale(logo_image,(32,32))

intro_image = pygame.image.load("car_image_intro.jpeg")
intro_image = pygame.transform.scale(intro_image,(window_width,window_height-250))

ce_image = pygame.image.load("image_ce.jpg")
ce_image = pygame.transform.scale(ce_image,(window_width,window_height-250))	

player1_car_image = pygame.image.load("Player1_car.jpg")
player1_car_image = pygame.transform.scale(player1_car_image,(car_width,car_height))

road_image = pygame.image.load("road.jpg")
road_image = pygame.transform.scale(road_image,(road_width,road_height))	


##################################################################
# it will set the title of the game
pygame.display.set_caption('Car Racing 2')


##################################################################
# it will set the logo for the game
pygame.display.set_icon(logo_image)

	
##################################################################
''' it will initialize a window or a screen for display and ,
	display screen is equal to the device screen
'''
game_display = pygame.display.set_mode() 
	

##################################################################
# It will create the obstacle or blocks 
def obstacle(color,obs_x,obs_y,obs_w,obs_h):
	pygame.draw.rect(game_display,color,[obs_x,obs_y,obs_w,obs_h])


##################################################################	
# It will ask for the player 1 turn
def now_turn_1():

	now = False

	while not now:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				now = True
				pygame.quit()
				quit()
		
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)

		message(" Now turn is of Player 1 ",500,300,silver,False,True,"medium")			
		
		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		button(640,655," Go Head ",button_1,white,button1_1)
		
		pygame.display.update()


##################################################################	
# It will ask for the player 2 turn
def now_turn_2():

	now = False

	while not now:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				now = True
				pygame.quit()
				quit()
		
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)

		message(" Player 1 Crashed ! ",500,250,white,False,True,"medium")
		
		message(" Now turn is of Player 2 ",450,400,silver,False,True,"medium")			
		
		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		button(640,655," Go Head  ",button_1,white,button1_1)
		
		pygame.display.update()


##################################################################
# It will ask for the number of players
def players():

	player_number = False

	while not player_number:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				player_number = True
				pygame.quit()
				quit()
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)
		
		message(" Select the number of players for the game ",300,200,silver,False,True,"medium")
		
		# (x,y,message,1st block color, text color , 2nd block color) 
		button(448,300," One ",button_1,white,button1_1)
		button(905,300," Two ",button_1,white,button1_1)

		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		pygame.display.update()


##################################################################
# It will show the Game Over Screen and compare player1 and player2 score
def finished():
	
	finish = False	

	while not finish:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finish = True
				pygame.quit()
				quit()
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)
		
		
		message(" Game Over !! ",530,200,white,False,True,"large")
					
		# (x,y,message,1st block color, text color , 2nd block color) 
		button(448,300," Play Again ",lime_green,black,green,130)
		button(905,300," Game Exit ",crimsion,black,red,130)

		message(f"Player 1 Score is : {score_1} and Player 2 Score is : {score_2} ",350,450,silver,False,True,"medium")

		if score_1 == score_2:
			message(' "  Match Tie  " ',610,550,silver,False,True,"medium")
		elif score_1>score_2:
			message(' "  Player 1 Win\'s the game  " ',500,550,silver,False,True,"medium")
		else:
			message(' "  Player 2 Win\'s the game  " ',500,550,silver,False,True,"medium")
	

		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		pygame.display.update()


#################################################################
# It will show the You Crashed Screen and show player1 score
def over():
	
	over_game_now = False	

	while not over_game_now:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				over_game_now = True
				pygame.quit()
				quit()
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)
		
		
		message(" You Crashed !! ",530,200,white,False,True,"large")
					
		# (x,y,message,1st block color, text color , 2nd block color) 
		button(448,300," Play Again ",lime_green,black,green,130)
		button(905,300," Game Exit ",crimsion,black,red,130)

		message(f"Your Score is : {score}",580,450,silver,False,True,"medium")

		if score == 0:
			message(' "  better luck next time !  " ',610,550,silver,False,True,"small")
		elif 1<=score<=50:
			message(' "  You\'re driving skills are good  !  " ',570,550,silver,False,True,"small")
		elif 51<=score<=100:
			message(' "  You\'re driving skills are better than other\'s  !  " ',530,550,silver,False,True,"small")
		elif 100<=score<=200:
			message(' "  You\'re among the best gamer\'s !  " ',580,550,silver,False,True,"small")
		elif score>=201:
			message(' "  You\'re among the legend gamer\'s  !  " ',570,550,silver,False,True,"small")
	

		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		pygame.display.update()


##################################################################
# It will show a Screen whether you want to exit the game or not
def end():

	global exit_2

	while not exit_2:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_2 = True
				pygame.quit()
				quit()
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)
		
		message(" Are You Sure, You Want To Exit The Game ",300,200,silver,False,True,"medium")
		
		# (x,y,message,1st block color, text color , 2nd block color) 
		button(448,300,"  YES ",lime_green,black,green)
		button(905,300,"  NO ",crimsion,black,red)

		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		pygame.display.update()


##################################################################
# It will pause the game and pause screen pops up
def paused():

	global pause

	while not pause:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pause = True
				pygame.quit()
				quit()
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)
		
		message(" Press Your Action ! ",560,200,silver,False,True,"medium")
		
		# (x,y,message,1st block color, text color , 2nd block color) 
		button(448,300," Continue ",lime_green,black,green,130)
		button(905,300," Start Again ",crimsion,black,red,130)

		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		pygame.display.update()


##################################################################	
# It will show the Instructions screen 
def instruction():

	con_trol = False

	while not con_trol:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				con_trol = True
				pygame.quit()
				quit()
		
		# message,x-position,y-position,color,bold,italic,size,style	
		message("Instructions",540,35,red,False,True,"large")

		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)

		message(" General Instructions: ",0,150,crimsion,False,True,"small")

		message(" >> If the car collide either with the boundary ( left or right ) or with the blocks then, the game is over .",0,200,silver,False,True,"small")
		message(" >> Use p key to pause the game .",0,230,silver,False,True,"small")
		message(" >> Use q key to quit the game .",0,260,silver,False,True,"small")

		message(" For Player 1 and Player 2: ",0,310,crimsion,False,True,"small")
		
		message(" Player 1 : Use Up key to move up .",0,360,silver,False,True,"small")
		message(" Player 1 : Use Down key to move down .",0,390,silver,False,True,"small")
		message(" Player 1 : Use Left key to move left .",0,420,silver,False,True,"small")
		message(" Player 1 : Use Right key to move right .",0,450,silver,False,True,"small")
		
		message(" Player 2 : Use w key to move up .",600,360,silver,False,True,"small")
		message(" Player 2 : Use s key to move down .",600,390,silver,False,True,"small")
		message(" Player 2 : Use a key to move left .",600,420,silver,False,True,"small")
		message(" Player 2 : Use d key to move right .",600,450,silver,False,True,"small")
			
		
		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		button(640,655," <- Back ",navy,white,blue)
		
		pygame.display.update()

		
##################################################################
# It will show the exit screen
def exit():

	exit = False

	while not exit:

		game_display.fill(black)
		game_display.blit(ce_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
				pygame.quit()
				quit()
		
		pygame.draw.line(game_display,silver,(0,window_height-668),(window_width,window_height-668),1)
		
		message(" Are You Sure, You Want To Exit The Game ",300,200,silver,False,True,"medium")
		
		# (x,y,message,1st block color, text color , 2nd block color) 
		button(448,300," YES ",lime_green,black,green)
		button(905,300," NO ",crimsion,black,red)

		pygame.draw.line(game_display,silver,(0,window_height-150),(window_width,window_height-150),1)

		pygame.display.update()
	
		
##################################################################		
# It will create a car
def car(x,y,name):
	game_display.blit(name,(x,y))
	

##################################################################	
# It will create a button on the screen
def button(x_button,y_button,msg,color1,color2,color3,length_b=100,widht_b=30):

	global score,score_1,score_2,pause,exit_2
	global x_car,y_car,x_change,y_change

	pygame.draw.rect(game_display,color1,[x_button,y_button,length_b,widht_b])
	message(msg,x_button+5,y_button+5,color2)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x_button<mouse[0]<x_button+length_b and y_button<mouse[1]<y_button+widht_b:
		pygame.draw.rect(game_display,color3,[x_button,y_button,length_b,widht_b])
		message(msg,x_button+5,y_button+5,color2)	
		if click == (1,0,0) and msg == " <- Back ":
			welcome_screen()
		elif click == (1,0,0) and msg == " YES ":
			pygame.quit()
			quit()
		elif click == (1,0,0) and msg == " NO ":
			welcome_screen()
		elif click == (1,0,0) and msg == " Instructions ":
			instruction()
		elif click == (1,0,0) and msg == " Exit ":
			exit()
		elif click == (1,0,0) and msg == " Play ":
			players()
		elif click == (1,0,0) and msg == " Continue ":
			pause = True
		elif click == (1,0,0) and msg == " Start Again ":		
			x_car = 10
			y_car = 540
			x_change = 0
			y_change = 0
			welcome_screen()
		elif click == (1,0,0) and msg == "  YES ":
			pygame.quit()
			quit()
		elif click == (1,0,0) and msg == "  NO ":
			exit_2 = True
		elif click == (1,0,0) and msg == " Game Exit ":
			pygame.quit()
			quit()
		elif click == (1,0,0) and msg == " Play Again ":
			x_car = 10
			y_car = 540
			x_change = 0
			y_change = 0
			welcome_screen()
		elif click == (1,0,0) and msg == " One ":
			score = 0
			main_game_loop()
		elif click == (1,0,0) and msg == " Two ":
			score_1=score_2=0
			now_turn_1()
		elif click == (1,0,0) and msg == " Go Head ":
			x_car = 10
			y_car = 540
			x_change = 0
			y_change = 0
			player1_game_loop()
		elif click == (1,0,0) and msg == " Go Head  ":
			x_car = 10
			y_car = 540
			x_change = 0
			y_change = 0
			player2_game_loop()
			

##################################################################
# message function it is used to display message on the screen
# (message,x-position,y-position,color,bold,italic,size,style)
def message(msg,x_pos,y_pos,color,b=False,i=True,size = "small",style = "Chilanka"):

	if size == "small":
		font = pygame.font.SysFont(style,20,bold = b,italic = i)	
	elif size == "medium":
		font = pygame.font.SysFont(style,40,bold = b,italic = i)
	elif size == "large":
		font = pygame.font.SysFont(style,60,bold = b,italic = i)

	render = font.render(msg,True,color)
	game_display.blit(render,(x_pos,y_pos))


##################################################################
# game intro loop 
def welcome_screen():
	
	intro = False

	while not intro:
		game_display.fill(black)
		game_display.blit(intro_image,(0,window_height-668))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = True
				pygame.quit()
				quit()
		
		message("Car Racing 2",540,25,red,False,True,"large")

		#(surface,color,(start point [x,y]),(end point [x,y]),width) 
		pygame.draw.line(game_display,black,(0,window_height-668),(window_width,window_height-668),5)
		pygame.draw.line(game_display,black,(0,window_height-150),(window_width,window_height-150),5)

		# x_button,y_button,msg,color1,color2,color3
		button(200,650," Play ",lime_green,black,green)
		button(633,650," Instructions ",blue,black,light_blue,140)
		button(1060,650," Exit ",crimsion,black,red)
		
		pygame.display.update()


##################################################################
# It is the main game loop for the player2
def player2_game_loop():

	obs_start_x = random.randrange(0,320)
	obs_start_x2 = random.randrange(340,660)
	obs_start_x3 = random.randrange(680,1000)
	obs_start_x4 = random.randrange(1020,1340)
	obs_start_y = 100
	obs_start_y2 = 100
	obs_start_y3 = 100
	obs_start_y4 = 100
	obs_speed = 1
	obs_w = 100
	obs_h = 100
	level = 1

	gameExit = False

	while not gameExit:
		
		global x_car,y_car,x_change,y_change,score_1,score_2
			
		game_display.fill(black)
		game_display.blit(road_image,(0,0))
		game_display.blit(road_image,(456,0))
		game_display.blit(road_image,(911,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit=True
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					global pause
					pause = False
					paused()
				elif event.key == pygame.K_q:
					global exit_2
					exit_2 = False
					end()
				elif event.key == pygame.K_a:
					x_change = -1*speed
					y_change = 0
				elif event.key == pygame.K_d:
					x_change = speed
					y_change = 0
				elif event.key == pygame.K_w:
					y_change = -1*speed
					x_change = 0
				elif event.key == pygame.K_s:
					y_change = speed
					x_change = 0 

			if event.type == pygame.KEYUP:
				if event.type == pygame.K_RIGHT or pygame.K_LEFT or pygame.K_UP or pygame.K_DOWN:
					x_change = 0
					y_change = 0


		x_car+=x_change
		y_car+=y_change

		obstacle(block_color,obs_start_x,obs_start_y,obs_w,obs_h)
		obstacle(block_color,obs_start_x2,obs_start_y2,obs_w,obs_h)
		obstacle(block_color,obs_start_x3,obs_start_y3,obs_w,obs_h)
		obstacle(block_color,obs_start_x4,obs_start_y4,obs_w,obs_h)
		
		obs_start_y+=obs_speed
		obs_start_y2+=obs_speed
		obs_start_y3+=obs_speed
		obs_start_y4+=obs_speed

		car(x_car,y_car,player1_car_image)
	
		message(f"Score : {score_2}",20,35,red,True,True,"small")
		
		if x_car<0 or x_car>window_width-car_width:
			finished()

		if obs_start_y>window_height: 
			score_2+=1
			obs_speed+=0.20
			obs_start_y = 0
			obs_start_x = random.randrange(0,320)
			
		if obs_start_y2>window_height:
			score_2+=1
			obs_start_y2 = 0
			obs_start_x2 = random.randrange(340,660)
			
		if obs_start_y3>window_width:
			score_2+=1
			obs_start_y3 = 0
			obs_start_x3 = random.randrange(680,1000)

		if obs_start_y4>window_width:
			score_2+=1
			obs_start_y4 = 0
			obs_start_x4 = random.randrange(1020,1340)

		if y_car<obs_start_y+obs_h and y_car+car_height>obs_start_y:
			if x_car>obs_start_x and x_car<obs_start_x+obs_w or x_car+car_width>obs_start_x and x_car+car_width<obs_start_x+obs_w:
				finished()

		if y_car<obs_start_y2+obs_h and y_car+car_height>obs_start_y2:
			if x_car>obs_start_x2 and x_car<obs_start_x2+obs_w or x_car+car_width>obs_start_x2 and x_car+car_width<obs_start_x2+obs_w:
				finished()

		if y_car<obs_start_y3+obs_h and y_car+car_height>obs_start_y3:
			if x_car>obs_start_x3 and x_car<obs_start_x3+obs_w or x_car+car_width>obs_start_x3 and x_car+car_width<obs_start_x3+obs_w:
				finished()

		if y_car<obs_start_y4+obs_h and y_car+car_height>obs_start_y4:
			if x_car>obs_start_x4 and x_car<obs_start_x4+obs_w or x_car+car_width>obs_start_x4 and x_car+car_width<obs_start_x4+obs_w:
				finished()

		pygame.display.update()


##################################################################
# It is the main game loop for the player1
def player1_game_loop():

	obs_start_x = random.randrange(0,320)
	obs_start_x2 = random.randrange(340,660)
	obs_start_x3 = random.randrange(680,1000)
	obs_start_x4 = random.randrange(1020,1340)
	obs_start_y = 100
	obs_start_y2 = 100
	obs_start_y3 = 100
	obs_start_y4 = 100
	obs_speed = 1
	obs_w = 100
	obs_h = 100
	level = 1

	gameExit = False

	while not gameExit:
		
		global x_car,y_car,x_change,y_change,score_1,score_2
			
		game_display.fill(black)
		game_display.blit(road_image,(0,0))
		game_display.blit(road_image,(456,0))
		game_display.blit(road_image,(911,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit=True
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					global pause
					pause = False
					paused()
				elif event.key == pygame.K_q:
					global exit_2
					exit_2 = False
					end()
				elif event.key == pygame.K_LEFT:
					x_change = -1*speed
					y_change = 0
				elif event.key == pygame.K_RIGHT:
					x_change = speed
					y_change = 0
				elif event.key == pygame.K_UP:
					y_change = -1*speed
					x_change = 0
				elif event.key == pygame.K_DOWN:
					y_change = speed
					x_change = 0 

			if event.type == pygame.KEYUP:
				if event.type == pygame.K_RIGHT or pygame.K_LEFT or pygame.K_UP or pygame.K_DOWN:
					x_change = 0
					y_change = 0


		x_car+=x_change
		y_car+=y_change

		obstacle(block_color3,obs_start_x,obs_start_y,obs_w,obs_h)
		obstacle(block_color3,obs_start_x2,obs_start_y2,obs_w,obs_h)
		obstacle(block_color3,obs_start_x3,obs_start_y3,obs_w,obs_h)
		obstacle(block_color3,obs_start_x4,obs_start_y4,obs_w,obs_h)
		
		obs_start_y+=obs_speed
		obs_start_y2+=obs_speed
		obs_start_y3+=obs_speed
		obs_start_y4+=obs_speed

		car(x_car,y_car,player1_car_image)
	
		message(f"Score : {score_1}",20,35,red,True,True,"small")
		
		if x_car<0 or x_car>window_width-car_width:
			now_turn_2()


		if obs_start_y>window_height: 
			score_1+=1
			obs_speed+=0.20
			obs_start_y = 0
			obs_start_x = random.randrange(0,320)
			
		if obs_start_y2>window_height:
			score_1+=1
			obs_start_y2 = 0
			obs_start_x2 = random.randrange(340,660)
			
		if obs_start_y3>window_width:
			score_1+=1
			obs_start_y3 = 0
			obs_start_x3 = random.randrange(680,1000)

		if obs_start_y4>window_width:
			score_1+=1
			obs_start_y4 = 0
			obs_start_x4 = random.randrange(1020,1340)

		if y_car<obs_start_y+obs_h and y_car+car_height>obs_start_y:
			if x_car>obs_start_x and x_car<obs_start_x+obs_w or x_car+car_width>obs_start_x and x_car+car_width<obs_start_x+obs_w:
				now_turn_2()

		if y_car<obs_start_y2+obs_h and y_car+car_height>obs_start_y2:
			if x_car>obs_start_x2 and x_car<obs_start_x2+obs_w or x_car+car_width>obs_start_x2 and x_car+car_width<obs_start_x2+obs_w:
				now_turn_2()

		if y_car<obs_start_y3+obs_h and y_car+car_height>obs_start_y3:
			if x_car>obs_start_x3 and x_car<obs_start_x3+obs_w or x_car+car_width>obs_start_x3 and x_car+car_width<obs_start_x3+obs_w:
				now_turn_2()

		if y_car<obs_start_y4+obs_h and y_car+car_height>obs_start_y4:
			if x_car>obs_start_x4 and x_car<obs_start_x4+obs_w or x_car+car_width>obs_start_x4 and x_car+car_width<obs_start_x4+obs_w:
				now_turn_2()

		pygame.display.update()


##################################################################
# It is main game loop for the default playing
def main_game_loop():

	obs_start_x = random.randrange(0,320)
	obs_start_x2 = random.randrange(340,660)
	obs_start_x3 = random.randrange(680,1000)
	obs_start_x4 = random.randrange(1020,1340)
	obs_start_y = 100
	obs_start_y2 = 100
	obs_start_y3 = 100
	obs_start_y4 = 100
	obs_speed = 1
	obs_w = 100
	obs_h = 100
	
	gameExit = False

	while not gameExit:
		
		global x_car,y_car,x_change,y_change,score
			
		game_display.fill(black)
		game_display.blit(road_image,(0,0))
		game_display.blit(road_image,(456,0))
		game_display.blit(road_image,(911,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit=True
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					global pause
					pause = False
					paused()
				elif event.key == pygame.K_q:
					global exit_2
					exit_2 = False
					end()
				elif event.key == pygame.K_LEFT:
					x_change = -1*speed
					y_change = 0
				elif event.key == pygame.K_RIGHT:
					x_change = speed
					y_change = 0
				elif event.key == pygame.K_UP:
					y_change = -1*speed
					x_change = 0
				elif event.key == pygame.K_DOWN:
					y_change = speed
					x_change = 0 

			if event.type == pygame.KEYUP:
				if event.type == pygame.K_RIGHT or pygame.K_LEFT or pygame.K_UP or pygame.K_DOWN:
					x_change = 0
					y_change = 0


		x_car+=x_change
		y_car+=y_change

		obstacle(block_color2,obs_start_x,obs_start_y,obs_w,obs_h)
		obstacle(block_color2,obs_start_x2,obs_start_y2,obs_w,obs_h)
		obstacle(block_color2,obs_start_x3,obs_start_y3,obs_w,obs_h)
		obstacle(block_color2,obs_start_x4,obs_start_y4,obs_w,obs_h)
		
		obs_start_y+=obs_speed
		obs_start_y2+=obs_speed
		obs_start_y3+=obs_speed
		obs_start_y4+=obs_speed

		car(x_car,y_car,player1_car_image)
	
		message(f"Score : {score}",20,35,red,True,True,"small")
		
		if x_car<0 or x_car>window_width-car_width:
			over()


		if obs_start_y>window_height: 
			score+=1
			obs_speed+=0.20
			obs_start_y = 0
			obs_start_x = random.randrange(0,320)
			
		if obs_start_y2>window_height:
			score+=1
			obs_start_y2 = 0
			obs_start_x2 = random.randrange(340,660)
			
		if obs_start_y3>window_width:
			score+=1
			obs_start_y3 = 0
			obs_start_x3 = random.randrange(680,1000)

		if obs_start_y4>window_width:
			score+=1
			obs_start_y4 = 0
			obs_start_x4 = random.randrange(1020,1340)

		if y_car<obs_start_y+obs_h and y_car+car_height>obs_start_y:
			if x_car>obs_start_x and x_car<obs_start_x+obs_w or x_car+car_width>obs_start_x and x_car+car_width<obs_start_x+obs_w:
				over()

		if y_car<obs_start_y2+obs_h and y_car+car_height>obs_start_y2:
			if x_car>obs_start_x2 and x_car<obs_start_x2+obs_w or x_car+car_width>obs_start_x2 and x_car+car_width<obs_start_x2+obs_w:
				over()

		if y_car<obs_start_y3+obs_h and y_car+car_height>obs_start_y3:
			if x_car>obs_start_x3 and x_car<obs_start_x3+obs_w or x_car+car_width>obs_start_x3 and x_car+car_width<obs_start_x3+obs_w:
				over()

		if y_car<obs_start_y4+obs_h and y_car+car_height>obs_start_y4:
			if x_car>obs_start_x4 and x_car<obs_start_x4+obs_w or x_car+car_width>obs_start_x4 and x_car+car_width<obs_start_x4+obs_w:
				over()

		pygame.display.update()

		
##################################################################
# calling welcome screen
welcome_screen()


##################################################################
# un-initialize all the pygame module
pygame.quit()


##################################################################
# quit the execution 
quit()	
	
