# Imports
import pygame, sys, random, time

# Setup Variables
Width = 720 #Width of screen in pixels
Height = 460 #Height of screen in pixels
FPS_Controller = pygame.time.Clock() #FPS Controller
Snake_POS = [100, 50] #Set Snake Head Position
Snake_Body = [[100, 50], [90, 50], [80, 50]] #Set Snake Body Position
Food_POS = [random.randrange(1, Width/10)*10, random.randrange(1, Height/10)*10] #Set Food Position
Food_Spawn = True #Choose if food should spawn
direction = "DOWN" #Direction of snake
Change_To = direction #Direction snake should change to

# Setup Color Variables
Red = pygame.Color(255, 0, 0) #Gameover Text
Green = pygame.Color(0, 255, 0) #Snake
Black = pygame.Color(0, 0, 0) #Score Text
White = pygame.Color(255, 255, 255) #Background
Brown = pygame.Color(163, 71, 0) #Food

# Initialize PyGame
Check_Errors = pygame.init()
# Check for initialisation errors
if Check_Errors[1] > 0:
    # Prints amount of errors and exits
    print("(!)There were {0} initializing errors, exiting...".format(Check_Errors[1]))
    sys.exit(-1)
else:
    # Print success message
    print("(+)PyGame Successfully Initialized!")

# Setup Play Surface
Play_Surface = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake Game!")

# GameOver Function
def Game_Over():
    # Make and Show Game Over Text
    My_Font = pygame.font.SysFont('Comis Sans', 72) #Set Font
    GO_Surf = My_Font.render('Game Over!', True, Red) #Set Text, Color and Anti-Aliasing
    GO_Rect = GO_Surf.get_rect() #Get Rectangle Arount Text
    GO_Rect.midtop = (Width/2, 15) #Set Text Location
    Play_Surface.blit(GO_Surf, GO_Rect) #Add Text To Game
    pygame.display.flip() #Update Display
    # Close
    time.sleep(4.5) #Wait Before Close
    pygame.quit() #Close PyGame Window
    sys.exit() #Close Python Console

# Main Logic
while True:
    for event in pygame.event.get(): #Get all events
        if event.type == pygame.QUIT: #Check For Event 'QUIT'
            pygame.quit() #Close PyGame Window
            sys.exit() #Close Python Console
            # Check if the Arrow Keys WASD is pressed and change direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Change_To = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                Change_To = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                Change_To = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                Change_To = 'DOWN'
            # Check if Escape key is pressed an post event 'QUIT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Direction Validation
    if Change_To == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if Change_To == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if Change_To == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if Change_To == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update Head Position
    if direction == 'RIGHT':
        Snake_POS[0] += 10
    if direction == 'LEFT':
        Snake_POS[0] -= 10
    if direction == 'UP':
        Snake_POS[1] -= 10
    if direction == 'DOWN':
        Snake_POS[1] += 10

    # Update Body Position
    Snake_Body.insert(0, list(Snake_POS))
    if Snake_POS[0] == Food_POS[0] and Snake_POS[1] == Food_POS[1]:
        Food_Spawn = False
    else:
        Snake_Body.pop()

    # Food Spawning
    if Food_Spawn == False:
        Food_POS = [random.randrange(1, Width/10)*10, random.randrange(1, Height/10)*10]
        Food_Spawn = True
    
    # Draw Play Surface
    Play_Surface.fill(White)
    
    # Draw Snake
    for pos in Snake_Body:
        pygame.draw.rect(Play_Surface, Green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw Food
    pygame.draw.rect(Play_Surface, Brown, pygame.Rect(Food_POS[0], Food_POS[1], 10, 10))
    
    # Update Screen
    pygame.display.flip()
    
    # Leave Screen GameOver
    if Snake_POS[0] >= Width or Snake_POS[0] <0 or Snake_POS[1] >= Height or Snake_POS[1] < 0:
        Game_Over()
    # Hit Body GameOver
    for block in Snake_Body[1:]:
        if Snake_POS[0] == block[0] and Snake_POS[1] == block[1]:
            Game_Over()
    
    # Set FPS Controller tick
    FPS_Controller.tick(17)