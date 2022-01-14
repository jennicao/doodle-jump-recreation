"""Author: Jennifer Cao
   Date: Mon, May 27th, 2019
   Description: Sprites for the Doodle Jump game
"""

import pygame, random

class GreenPlatform(pygame.sprite.Sprite):
    '''A sprite subclass to represent a static Green Platform sprite.'''
    def __init__(self, screen, yCoordinate):
        '''This initializer takes a screen surface and y coordinate as 
        parameters. It sets the image/rect attributes and position of the 
        Platform.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes
        self.image = pygame.image.load("objects/green.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
        # Instance variable to keep track of the screen surface
        self.window = screen
        
        # Initiate the Platform's position
        self.reset(yCoordinate)
        
    def reset(self, yCoordinate):
        '''This method accepts the yCoordinate of the screen as a parameter and 
        resets the Platform's position.'''
        # Determining a random x position
        xCoordinate = random.randint(35, self.window.get_width() - 35) 
        
        self.rect.center = (xCoordinate, yCoordinate)   
        
class BrownPlatform(pygame.sprite.Sprite):
    '''A sprite subclass to represent a fragile Brown Platform sprite.'''
    def __init__(self, screen, yCoordinate):
        '''This initializer takes takes a screen surface and y coordinate as 
        parameters. It sets the image/rect attributes and position of the 
        Platform.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load the Platform images
        self.brown1 = pygame.image.load("objects/brown1.png")
        self.brown2 = pygame.image.load("objects/brown2.png")

        # Instance variable to keep track of the screen surface
        self.window = screen

        # Initiate the Platform's image/rect attributes and position
        self.reset(yCoordinate)
        
    def reset(self, yCoordinate):
        '''This method accepts the yCoordinate of the screen as a parameter and 
        resets the Platform's falling variables, image/rect attributes, and
        position.'''        
        self.isBroken = False
        self.velocity = 0
        
        # Set the image and rect attributes        
        self.image = self.brown1
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
        # Determining a random x position
        xCoordinate = random.randint(35, self.window.get_width() - 35) 
        
        self.rect.center = (xCoordinate, yCoordinate)           
    
    def platformBreaks(self):
        '''This method will initiate the Platform's fall.'''
        self.image = self.brown2
        self.image = self.image.convert_alpha()
        self.isBroken = True        
        
    def update(self):
        '''This method will automatically be called to update the Platform
        sprite's position.'''
        if self.isBroken:
            self.rect.centery += self.velocity
            # Velocity increases as the Platform falls                                    
            self.velocity += 1              
            
class BluePlatform(GreenPlatform):
    '''A sprite subclass to represent a moving Blue Platform sprite.'''
    def __init__(self, screen, yCoordinate):
        '''This initializer takes a screen surface and y coordinate as 
        parameters. It sets the image/rect attributes and position of the 
        Platform.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes
        self.image = pygame.image.load("objects/blue.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
        # Instance variables to keep track of the screen
        # surface and set the initial x direction
        self.window = screen 
        self.dx = 3
        
        # Initiate the Platform's position using the 
        # reset method inherited from the Green Platform
        self.reset(yCoordinate)        
        
    def update(self):
        '''This method will automatically be called to update the Platform
        sprite's position.'''
        self.rect.centerx += self.dx
        # Reverse the x direction if the Platform hits the sides of the screen
        if (self.rect.left < 0) or (self.rect.right > self.window.get_width()):
            self.dx = -self.dx
            
class Spring(pygame.sprite.Sprite):
    '''A sprite subclass to represent a Spring sprite.'''
    def __init__(self, platforms):
        '''This initializer takes a list of platforms as a parameter. It sets
        the image/rect attributes and position of the Spring.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)  
        
        # Load the Spring images
        self.spring1 = pygame.image.load("objects/spring1.png")
        self.spring2 = pygame.image.load("objects/spring2.png")   
        
        self.reset(platforms)

    def changeImage(self):
        '''This method changes the spring image.'''
        self.image = self.spring2
        self.image = self.image.convert_alpha()        
        
    def reset(self, platforms):
        '''This method accepts a list of platforms as a paramter and 
        resets the Spring's image/rect attributes and position.'''         
        # Set the image and rect attributes        
        self.image = self.spring1
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
        # Making sure the Spring only appears higher up on the screen
        index = 0
        while platforms[index].rect.top >= 0:
            index = random.randint(0, len(platforms) - 1)
            
        # Placing the Spring on the chosen Platform
        xLocation = random.randint(-10, 10)
        self.rect.centerx = platforms[index].rect.centerx + xLocation
        self.rect.bottom = platforms[index].rect.top + 5
  
class Monster(pygame.sprite.Sprite):
    '''A sprite subclass to represent a Monster sprite.'''
    def __init__(self, screen, yCoordinate):
        '''This initializer takes a screen surface and y coordinate as
        parameters. It sets the image/rect attributes and position of the 
        Monster.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)    
        
        # Store the different monster in tuples categorized
        # by whether they have one or two images
        self.singleImages = ("monsters/big_blue.png", "monsters/big_green.png", \
                            "monsters/red.png")
        self.doubleImages = (("monsters/alien_down.png", "monsters/alien_up.png"), \
                       ("monsters/alien2_green.png", "monsters/alien2_red.png"), \
                       ("monsters/green_yellow_eyed.png", "monsters/green_red_eyed.png"), \
                       ("monsters/winged_down.png", "monsters/winged_up.png"))
        
        # Instance variables to keep track of the screen 
        # surface and set initial integer variables
        self.window = screen
        self.switchTime = 0
        self.velocity = -5
        self.dx = 5      
        
        # Initiate the Monster's image/rect attributes and position
        self.reset(yCoordinate)        
        
    def reset(self, yCoordinate):
        '''This method accepts the y coordinate of the screen as a parameter and 
        resets the Monster's images and position.'''
        # Determining a random image number
        self.imageNum = random.randint(1, 2)
        # Determining a random index to get a random monster
        self.index = random.randint(0, self.imageNum + 1)   
        # Determining a random x position
        xCoordinate = random.randint(50, self.window.get_width() - 50) 
        # Set the monster higher up off the screen
        yCoordinate -= random.randint(1500, 2000)    
        
        # Set image and rect attributes
        if self.imageNum == 1:
            self.image = pygame.image.load(self.singleImages[self.index])
        else:
            # For monsters with two images, set it to the first one for now
            self.image = pygame.image.load(self.doubleImages[self.index][0])
        self.image = self.image.convert_alpha() 
        self.rect = self.image.get_rect()   
        self.rect.center = (xCoordinate, yCoordinate)        
        
    def update(self):
        '''This method will be called automatically to reposition the Monster
        sprite on the screen.'''  
        # Monster will continually switch images if it has double images        
        if self.imageNum == 2:
            if self.switchTime % 14 == 0:
                self.image = pygame.image.load(self.doubleImages[self.index][1])
            elif self.switchTime % 7 == 0:
                self.image = pygame.image.load(self.doubleImages[self.index][0])
            self.image = self.image.convert_alpha() 
            self.switchTime += 1            
     
        # Monster will be "boucing" up and down as it moves left and right
        self.rect.centery += self.velocity
        # Velocity decreases as the Monster gets higher 
        # and increases as the Monster falls lower        
        self.velocity += 1
        # Reset the velocity time for the bouncing effect
        if self.velocity > 5:
            self.velocity = -5
              
        self.rect.centerx += self.dx
        # Reverse the x direction if the Monster hits the sides of the screen
        if (self.rect.left < 0) or (self.rect.right > self.window.get_width()):
            self.dx = -self.dx
            
class Poof(pygame.sprite.Sprite):
    '''A sprite subclass to represent a Poof sprite (when Monster is shot).'''
    def __init__(self, position):
        '''This initializer takes a position tuple as a parameter. It sets the 
        image/rect attributes and position of the Poof.'''        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)  
        
        # Set the image and rect attributes for the Poof
        self.image = pygame.image.load("poof/poof0.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
 
        self.imageNum = 0
             
    def update(self):
        '''This method will be called automatically to reposition the Poof 
        sprite on the screen.'''
        # Load the images of the Poof
        self.image = pygame.image.load("poof/poof" + str(self.imageNum) + ".png")
        self.imageNum += 1
        
        # After all the images are loaded, it dies
        if self.imageNum == 8:
            self.kill()        
        
class Doodle(pygame.sprite.Sprite):
    '''A sprite subclass to represent a Doodle sprite.'''
    def __init__(self, screen, position, velocity):
        '''This initializer takes a screen surface, position tuple, and starting
        velocity as parameters. It sets the image/rect attributes and jumping 
        abilities of the Doodle.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Store the Doodle images in a tuple
        self.doodleImages = (("objects/left_face.png", "objects/left_jump.png"), \
                            ("objects/right_face.png", "objects/right_jump.png"), \
                            ("objects/shoot_face.png", "objects/shoot_jump.png"))
             
        # Set image and rect attributes
        # Make the Doodle face the right side to start off
        self.image = pygame.image.load(self.doodleImages[1][0])
        self.image = self.image.convert_alpha() 
        self.rect = self.image.get_rect()   
        self.rect.center = position
        
        # Instance variables to keep track of the screen surface,
        # and set the initial indexes, shooting time, and velocity
        self.window = screen
        self.index = 1
        self.index2 = 0
        self.shootingTime = 0        
        self.velocity = velocity
        
    def goLeft(self):
        '''This method will make the Doodle go left once and set the Doodle's 
        face to the left by changing the index of the tuple it refers to.'''   
        self.rect.centerx -= 7
        # Only change the face when the Doodle isn't shooting
        if not self.shootingTime:
            self.index = 0
                 
    def goRight(self):
        '''This method will make the Doodle go right once and set the Doodle's 
        face to the right by changing the index of the tuple it refers to.'''
        self.rect.centerx += 7
        # Only change the face when the Doodle isn't shooting        
        if not self.shootingTime:
            self.index = 1
        
    def shootUp(self):
        '''This method will initate the shooting time and set the Doodle's face 
        upwards by changing the index of the tuple it refers to.''' 
        self.shootingTime = 10   
        self.index = 2        
        
    def jump(self, velocity):
        '''This method accepts the velocity as a parameter and will initiate the 
        Doodle's jump by setting up the velocity. It gets the Doodle into 
        jumping position by setting the second index of the tuple it refers to.'''
        self.velocity = velocity
        self.index2 = 1
        
    def fall(self):
        '''This method will initiate the Doodle's fall (when it hits a Monster).'''
        self.velocity = -5
    
    def getVelocity(self):
        '''This accessor returns the integer variable: self.velocity, 
        which stores the current velocity the Doodle is at.'''
        return self.velocity
        
    def update(self):
        '''This method will be called automatically to reposition the Doodle 
        sprite on the screen.'''
        # Set the Doodle's faces (left, right, up) and position (jump or not)
        self.image = pygame.image.load(self.doodleImages[self.index][self.index2])
        self.image = self.image.convert_alpha()    
            
        # If the Doodle is still shooting, do not reset it's position yet
        if self.shootingTime:
            self.shootingTime -= 1
            # Reset the Doodle's position to the right side as default           
            if not self.shootingTime:               
                self.index = 1
                self.index2 = 0
            
        # Velocity decreases as the Doodle gets higher 
        # and increases as the Doodle falls lower
        self.rect.centery += self.velocity    
        
        # Switching the Doodle's jumping position back to
        # regular position when it starts falling
        if self.velocity == 0:
            self.index2 = 0            
        
        # Increasing velocity only to a certain point
        # so the Doodle doesn't fall through the platform      
        if self.velocity < 10:
            self.velocity += 1  
              
        # If the Doodle passes the left side of
        # the screen, it appears on the right
        if self.rect.right < 0:
            self.rect.centerx = self.window.get_width()
        # If the Doodle passes the right side
        # the screen, it appears on the left
        elif self.rect.left > self.window.get_width():
            self.rect.centerx = 0     

class Bullet(pygame.sprite.Sprite):
    '''A sprite subclass to represent a Bullet sprite.'''
    def __init__(self, screen, xCoordinate, yCoordinate):
        '''This initializer takes a screen surface, x, and y coordinate as 
        parameters. It sets the image/rect attributes and position of the 
        Bullet.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes
        self.image = pygame.image.load("objects/bullet.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = xCoordinate
        self.rect.top = yCoordinate
        
        # Instance variables to keep track of the screen
        # surface and set the initial y direction
        self.window = screen 
        self.dy = -20
        
    def update(self):
        '''This method will be called automatically to reposition the Bullet 
        sprite on the screen.'''  
        self.rect.centery += self.dy

        # If the bullet touches the top of the screen, it dies
        if self.rect.top <= 0:
            self.kill()
            
class Dizziness(pygame.sprite.Sprite):
    '''A sprite subclass to represent dizziness (for the Doodle).'''
    def __init__(self, position):
        '''This initializer takes a position tuple as a parameter and sets 
        the objects/rect attributes of the Dizziness.'''   
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes
        self.image = pygame.image.load("objects/dizzy0.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
        self.imageNum = 0
        self.setPosition(position)
        
    def setPosition(self, position):
        '''This mutator sets the position of the Dizziness (follows Doodle).'''
        self.rect.centerx = position[0]
        self.rect.centery = position[1] - 8
        
    def update(self):
        '''This method will be called automatically to display 
        the Dizziness on the Doodle.'''   
        # Images change to make it look like the stars go in a circle
        self.imageNum += 1
        self.image = pygame.image.load("objects/dizzy" + str(self.imageNum % 3) + ".png")
        self.image = self.image.convert_alpha()
        
class ScoreBar(pygame.sprite.Sprite):
    '''A sprite subclass to represent a static, translucent score bar.'''
    def __init__(self):
        '''This initializer sets the image/rect attributes of the score bar
        and makes it translucent.'''   
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes
        self.image = pygame.image.load("backgrounds/score_bar.png")
        self.image = self.image.convert()
        # This makes the image translucent
        self.image.set_alpha(150)        
        self.rect = self.image.get_rect()  
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self, string, score, xCoordinate, yCoordinate):
        '''This initializer takes a string, score, x, and y coordinate as 
        parameters. It loads the custom font "doodle_jump_font.ttf", and sets 
        the starting word (if applicable), score, and position.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load custom font, and initialize the starting word, score, and position
        self.font = pygame.font.Font("doodle_jump_font.ttf", 30)
        self.string = string
        self.score = score
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
         
    def getScore(self):
        '''This accessor returns the integer variable: self.score, which
        stores the current score (height) of the Doodle.'''
        return self.score
        
    def setScore(self, score):
        '''This mutator accepts an integer score as a parameter. If this score
        is greater than self.score, self.score is set to this score.'''
        self.score = max(self.score, score)
     
    def update(self):
        '''This method will be called automatically to display the current score.'''
        self.image = self.font.render(self.string + str(self.score), 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = self.xCoordinate
        self.rect.top = self.yCoordinate
        
class Button(pygame.sprite.Sprite):
    '''A sprite subclass to represent a static Button sprite.'''
    def __init__(self, index, position):
        '''This initializer takes an index and position tuple as parameters. It 
        sets the image/rect attributes and position of the Button.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Store the Button images in a tuple to be accessed by index
        self.buttons = ("buttons/play.png", "buttons/play_again.png", \
                        "buttons/menu.png", "buttons/pause.png", "buttons/resume.png")   
        
        # Set the image and rect attributes
        self.image = pygame.image.load(self.buttons[index])
        self.image = self.image.convert_alpha()  
        self.rect = self.image.get_rect()
        self.rect.center = position