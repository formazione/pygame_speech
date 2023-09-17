import pygame


screen = pygame.display.set_mode((800, 600))
buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    ''' Create a button clickable with changing hover color'''

    def __init__(self,
                pos=(0,0),
                text="Click",
                fontsize=16,
                colors="white on blue",
                hover_colors="red on green",
                # style=1,
                borderc=(255,255,255),
                command=lambda: print("No command activated for this button")):

        super().__init__()
        self.text = text
        self.command = command
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        self.fgh, self.bgh = hover_colors.split(" on ")
        self.borderc = borderc # for the style2
        self.font = pygame.font.SysFont("Arial", fontsize)
        self.pos = pos
        self.x, self.y = self.pos
        self.image = self.create_image(self.text, self.fg, self.bg)
        self.original_image = self.image.copy()
        self.hover_image = self.create_image(self.text, self.fgh, self.bgh)
        self.pressed = 1
        buttons.add(self)


    def create_image(self, text, fg, bg):
        self.text = text
        image = self.font.render(self.text, 1, fg)
        self.rect = image.get_rect()
        bgo = pygame.Surface((self.rect.w, self.rect.h))
        bgo.fill(bg)
        bgo.blit(image, (0,0))
        return bgo


    def update(self):
        ''' called by buttons.update, the group of buttons '''
        self.hover()
        self.click()


    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hover_image
        else:
            self.image = self.original_image
            

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                # print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1
