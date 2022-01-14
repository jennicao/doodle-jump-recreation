"""Author: Jennifer Cao
   Date: Mon, May 27th, 2019
   Description: Doodle Jump game
"""

# I - IMPORT AND INITIALIZE
import pygame, doodleJumpSprites
pygame.init()

def displayMainMenu():
    '''This function displays the main menu for the Doodle Jump game. It returns
    the next action for the game: quit or play.'''
    # D - DISPLAY
    screen = pygame.display.set_mode((401, 620))
    pygame.display.set_caption("Main Menu")
     
    # E - ENTITIES
    background = pygame.image.load("backgrounds/main_menu.png")
    background = background.convert()
    screen.blit(background, (0, 0))

    # Sprites for: play button, doodle
    playButton = doodleJumpSprites.Button(0, (140, 200))        
    doodle = doodleJumpSprites.Doodle(screen, (80, screen.get_height()), -17)
    allSprites = pygame.sprite.LayeredUpdates(playButton, doodle)  
    
    # Instructions for the game
    font = pygame.font.Font("doodle_jump_font.ttf", 20)
    messages = ("   use the left", " and right arrow", "   keys to move", \
                "use the up arrow", "   key or space", "   bar to shoot")
    yCoordinate = 375
    for message in messages:
        instructions = font.render(message, 1, (0, 0, 0))
        screen.blit(instructions, (248, yCoordinate))
        if message == "   keys to move":
            yCoordinate += 40
        else:
            yCoordinate += 25
    
    # Music and Sound Effects
    pygame.mixer.music.load("sounds/music.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)        
    click = pygame.mixer.Sound("sounds/click.ogg")
    
    # A - ACTION
    
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True

    # L - LOOP
    while keepGoing:
        # TIME
        clock.tick(30)
     
        # E - EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(700)                
                keepGoing = False
                nextAction = "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.rect.collidepoint(pygame.mouse.get_pos()):
                    click.play()
                    keepGoing = False
                    nextAction = "play"
                    
        # If the Doodle hits the "imaginary" platform, it jumps up
        if doodle.rect.bottom >= screen.get_height() - 120:
            doodle.jump(-17)

        # R - REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()    
    
    return nextAction

def displayGameOver(highScore, score, doodleCenterX):
    '''This function accepts the highscore, score, and the Doodle's center x as 
    parameters. It displays the game over screen for the Doodle Jump game. It 
    returns the next action for the game: quit, play, or main menu.'''
    # D - DISPLAY
    screen = pygame.display.set_mode((401, 620))
    pygame.display.set_caption("Game Over")
     
    # E - ENTITIES
    background = pygame.image.load("backgrounds/game_over.png")
    background = background.convert()
    screen.blit(background, (0, 0))
    
    # Sprites for: score, high score, play again button, main menu button, doodle 
    score = doodleJumpSprites.ScoreKeeper("score: ", score, \
                                     screen.get_width() / 2 - 70, 250)
    highScore = doodleJumpSprites.ScoreKeeper("high score: ", highScore, \
                                         screen.get_width() / 2 - 90, 300)
    playAgainButton = doodleJumpSprites.Button(1, (screen.get_width() /2 , 390))    
    menuButton = doodleJumpSprites.Button(2, (screen.get_width() / 2, 450))
    doodle = doodleJumpSprites.Doodle(screen, (doodleCenterX, -20), 10)
    allSprites = pygame.sprite.LayeredUpdates(score, highScore, \
                                              playAgainButton, menuButton, doodle)     
    
    # Music and Sound Effects
    pygame.mixer.music.load("sounds/music.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)        
    click = pygame.mixer.Sound("sounds/click.ogg")
    
    # A - ACTION
    
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True

    # L - LOOP
    while keepGoing:
        # TIME
        clock.tick(30)
     
        # E - EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(700)                
                keepGoing = False
                nextAction = "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playAgainButton.rect.collidepoint(pygame.mouse.get_pos()):
                    click.play()
                    keepGoing = False
                    nextAction = "play"
                elif menuButton.rect.collidepoint(pygame.mouse.get_pos()):
                    click.play()
                    keepGoing = False
                    nextAction = "main menu"
           
        # While the Doodle falls, if it touches
        # the bottom of the screen, it dies
        if doodle.rect.top >= screen.get_height():
            doodle.kill()
            
        # R - REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()    
    
    return nextAction    
    
def displayPause(screen):
    '''This function accepts the screen as a parameter. It displays the pause 
    screen when the game is paused.'''     
    # E - ENTITIES
    background = pygame.image.load("backgrounds/paused.png")
    background = background.convert()
    # Make background translucent
    background.set_alpha(220)            
    screen.blit(background, (0, 0))
    
    resumeButton = doodleJumpSprites.Button(4, (screen.get_width() /2 , 450))  
    allSprites = pygame.sprite.LayeredUpdates(resumeButton)
    
    # Sound Effects      
    click = pygame.mixer.Sound("sounds/click.ogg")
    
    # A - ACTION
    
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True

    # L - LOOP
    while keepGoing:
        # TIME
        clock.tick(30)
     
        # E - EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                nextAction = "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resumeButton.rect.collidepoint(pygame.mouse.get_pos()):
                    click.play()                    
                    keepGoing = False
            
        # R - REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()    
    
def playGame():
    '''This function is the actual Doodle Jump game. It returns the next action:
    quit or game over, the score when the game is over, and the Doodle's center 
    x.'''    
    # D - DISPLAY
    screen = pygame.display.set_mode((401, 620))
    pygame.display.set_caption("Doodle Jump Game")
     
    # E - ENTITIES
    background = pygame.image.load("backgrounds/background.png")
    background = background.convert()
    screen.blit(background, (0, 0))
    
    # Sprites for: doodle, score keeper, score bar, pause button
    #              25 blue/brown/green platforms, 1 spring, 1 monster
    doodle = doodleJumpSprites.Doodle(screen, (screen.get_width() / 2, \
                                             screen.get_height() - 50), -17)
    scoreKeeper = doodleJumpSprites.ScoreKeeper("", 0, 12, 0) 
    scoreBar = doodleJumpSprites.ScoreBar()
    pauseButton = doodleJumpSprites.Button(3, (screen.get_width() - 20, 20))
    
    yCoordinate = screen.get_height() - 20
    platformGroup = pygame.sprite.Group()
    brownPlatforms = pygame.sprite.Group()
    greenPlatforms = []
    # Create 25 platforms 
    for platformNum in range(25):
        # Blue platforms are the rarest, green platforms are the most common
        if platformNum % 7 == 0:
            platform = doodleJumpSprites.BluePlatform(screen, yCoordinate)
        elif platformNum % 4 == 0:
            platform = doodleJumpSprites.BrownPlatform(screen, yCoordinate) 
            # Add to the brownPlatforms group for collision detection later
            brownPlatforms.add(platform)
        else:   
            platform = doodleJumpSprites.GreenPlatform(screen, yCoordinate)
            # Append to the greenPlatforms list for creating a spring later           
            greenPlatforms.append(platform)
        platformGroup.add(platform)
        yCoordinate -= 30
        
    spring = doodleJumpSprites.Spring(greenPlatforms)
    monster = doodleJumpSprites.Monster(screen, yCoordinate)    
    
    bulletGroup = pygame.sprite.Group()
    allSprites = pygame.sprite.LayeredUpdates(platformGroup, spring, monster, \
                                    doodle, scoreBar, scoreKeeper, pauseButton)  
    
    # Music and Sound Effects
    pygame.mixer.music.load("sounds/music.ogg")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)        
    boing = pygame.mixer.Sound("sounds/boing.ogg")
    shoot = pygame.mixer.Sound("sounds/shoot.ogg")
    shoot.set_volume(0.7)    
    falling = pygame.mixer.Sound("sounds/falling.ogg")
    falling.set_volume(0.5)      
    breaking = pygame.mixer.Sound("sounds/breaking.ogg")
    breaking.set_volume(0.6)  
    poof = pygame.mixer.Sound("sounds/poof.ogg")
    poof.set_volume(0.6)    
    dizzy = pygame.mixer.Sound("sounds/dizzy.ogg")
    dizzy.set_volume(0.7) 
    click = pygame.mixer.Sound("sounds/click.ogg")
    growl = pygame.mixer.Sound("sounds/growl.ogg")
    growl.set_volume(0.3) 
    boing2 = pygame.mixer.Sound("sounds/boing2.ogg")
    boing2.set_volume(0.6) 
    
    # A - ACTION
    
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    goingLeft = False
    goingRight = False
    hitMonster = False        
    extraHeight = 0
    # Spacing between platforms
    spaceBetween = 30
    # Height that needs to be reached before spacing between platforms increase
    goalHeight = 500
 
    # L - LOOP
    while keepGoing:
        # TIME
        clock.tick(30)
            
        # E - EVENT HANDLING: Player uses left, right, up arrow keys + space bar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(700)
                keepGoing = False
                nextAction = "quit"
            # If the Doodle hits a Monster and is falling, it cannot move
            if not hitMonster:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        goingLeft = True
                    elif event.key == pygame.K_RIGHT:
                        goingRight = True
                    elif (event.key == pygame.K_UP) or (event.key == pygame.K_SPACE):
                        growl.stop()
                        shoot.play()
                        bullet = doodleJumpSprites.Bullet(screen, doodle.rect.centerx - 5, \
                                                      doodle.rect.top)
                        bulletGroup.add(bullet)
                        allSprites.add(bullet)
                        doodle.shootUp()                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        goingLeft = False
                    elif event.key == pygame.K_RIGHT:
                        goingRight = False     
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pauseButton.rect.collidepoint(pygame.mouse.get_pos()):
                        click.play()
                        displayPause(screen)
                        screen.blit(background, (0, 0))                        
                    
        # Doodle goes left/right as long as player holds down arrow key
        if not hitMonster:
            if goingLeft:
                doodle.goLeft()
            elif goingRight:
                doodle.goRight()
                     
        # If the Doodle passes the bottom of the screen, game over
        if doodle.rect.top >= screen.get_height():
            growl.stop()
            falling.play()
            keepGoing = False
            nextAction = "game over"
            
        # If the Doodle and Monster collide, the Doodle falls
        if (not hitMonster) and (doodle.rect.colliderect(monster.rect)):
            growl.stop()
            poof.play()
            dizzy.play()
            dizziness = doodleJumpSprites.Dizziness(doodle.rect.center)
            allSprites.add(dizziness)
            doodle.fall()
            hitMonster = True
            
        if hitMonster:
            # Dizziness follows the Doodle as it falls
            dizziness.setPosition(doodle.rect.center)
        
        # If a Monster collides with a bullet, reset the
        # Monster higher up the screen and destroy the bullet
        collisions = pygame.sprite.spritecollide(monster, bulletGroup, False, \
                                                 pygame.sprite.collide_mask)
        if collisions:
            growl.stop()
            poof.play()
            allSprites.add(doodleJumpSprites.Poof(monster.rect.center))
            monster.reset(yCoordinate)
            for collision in collisions:
                collision.kill()
        # If the Doodle hasn't hit the Monster and is within 
        # 500 pixels of the Monster, a growling sound plays
        elif (not hitMonster) and (monster.rect.centery - doodle.rect.centery >= -500):
            growl.play()
            
        # Only check for collisions between Doodle and platforms/spring when
        # the Doodle hasn't hit a Monster and is falling (velocity > 0)
        if (not hitMonster) and (doodle.getVelocity() > 0):
            collisions = pygame.sprite.spritecollide(doodle, platformGroup, False, \
                                                     pygame.sprite.collide_mask)
            if collisions:
                # Making sure it's the Doodle's bottom that touches the platform
                if doodle.rect.bottom <= collisions[0].rect.bottom:
                    # Doodle is repositioned on platform and jumps again   
                    doodle.rect.bottom = collisions[0].rect.top
                    boing.play()                    
                    doodle.jump(-17)  
                    
                    # If platform is brown...
                    if collisions[0] in brownPlatforms:
                        breaking.play()
                        # ...it breaks and falls after Doodle touches it
                        collisions[0].platformBreaks()   
                        
            # Doodle jumps even higher if it lands on a Spring
            if doodle.rect.colliderect(spring.rect):
                # Making sure it's the Doodle's bottom that touches the Spring            
                if doodle.rect.bottom <= spring.rect.bottom:
                    doodle.rect.bottom = spring.rect.top  
                    spring.changeImage()
                    growl.stop()
                    boing2.play()
                    doodle.jump(-30)      

        # If the Doodle reaches half way up the screen, move the sprites down
        # the screen (only while jumping, meaning velocity < 0)
        if (doodle.getVelocity() < 0) and (doodle.rect.top <= screen.get_height() / 2):
            # Sprites move down at the current velocity of the Doodle
            # (so the transition looks smooth)
            doodle.rect.top += -doodle.getVelocity()
            
            # If a Monster touches the bottom of the screen, reset its
            # image to a new monster and have a new position
            if monster.rect.top >= screen.get_height():
                growl.fadeout(800)
                monster.reset(yCoordinate) 
            monster.rect.top += -doodle.getVelocity()              
                   
            # If a Spring touches the bottom of the screen,
            # reset its position higher up the screen                 
            if spring.rect.centery >= screen.get_height():
                spring.reset(greenPlatforms)
            spring.rect.top += -doodle.getVelocity()            
            
            for platform in platformGroup.sprites():
                platform.rect.top += -doodle.getVelocity()
                # If a Platforn touches the bottom of the screen,
                # reset its position higher up the screen                 
                if platform.rect.top >= screen.get_height():
                    platform.reset(yCoordinate)
                    yCoordinate -= spaceBetween
                    
            # Since the screen moves down by the Doodle's
            # velocity, increase the height by that much
            extraHeight += -doodle.getVelocity()
            # y coordinate for making new platforms also moves down 
            yCoordinate += -doodle.getVelocity() 
            
        # Increase the spacing between platforms as the Doodle gets higher
        if (spaceBetween < 55) and (scoreKeeper.getScore() >= goalHeight):
            spaceBetween += 1
            goalHeight += 500
                
        # Reverse the y coordinates (eg. 0 becomes 620, 620 becomes 0)
        # Add back the height from moving the screen down (if necessary)
        score = -doodle.rect.top + screen.get_height() + extraHeight
        # Compare it to the highest score and change if necessary
        scoreKeeper.setScore(score)
        
        # R - REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
    
    return nextAction, scoreKeeper.getScore(), doodle.rect.centerx
    
def main():
    '''This function defines the 'mainline logic' for the game.'''    
    quitGame = False
    highScore = 0
    nextAction = displayMainMenu()    
    while not quitGame:
        if nextAction == "play":
            nextAction, score, doodleCenterX = playGame()
        elif nextAction == "game over":
            highScore = max(highScore, score)
            nextAction = displayGameOver(highScore, score, doodleCenterX)
        elif nextAction == "main menu":
            nextAction = displayMainMenu()
        else:
            quitGame = True

    # Close the game window after less than a second (to let music fadeout)
    pygame.time.delay(700)
    pygame.quit()    
     
# Call the main function
main()