import pygame
pygame.init()
screen = pygame.display.set_mode()


#import your controller
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()
print (width, height)

x_center = width/2
y_center = height/2

screen.fill("white")
font = pygame.font.Font(None, 40)
font_two = pygame.font.Font(None, 80)
text = font_two.render("Superhero Personality Quiz", True, "Blue")
screen.blit(text, (x_center/3, y_center/2))
text_two = font.render("Answer the following questions to find out which Marvel superhero is most like you!", True, "Red")
screen.blit(text_two, (x_center/7, y_center))
purple = pygame.draw.rect(screen, "purple", (400, 400, 300, 120))
text_three = font_two.render("START!", True, "White")
screen.blit(text_three, (460, 440))
pygame.display.flip()



Green = pygame.draw.rect(screen, "green", (75, 130, 500, 250))
Blue = pygame.draw.rect(screen, "blue", (x_center, 130, 500, 250))
Red = pygame.draw.rect(screen, "red", (75, y_center+50, 500, 250))
Yellow = pygame.draw.rect(screen, "yellow", (x_center, y_center+50, 500, 250))

def boxes(green, blue, red, yellow):
    green
    blue
    red
    yellow
    pygame.display.flip()

def answer(green, blue, red, yellow):
        boxes(green=Green, blue=Blue, red=Red, yellow=Yellow)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if pygame.Rect.collidepoint(green, mouse_position):
                        option1 =1 
                    elif pygame.Rect.collidepoint(blue, mouse_position):
                        option2 =1
                    elif pygame.Rect.collidepoint(red, mouse_position):
                        option3 =1
                    elif pygame.Rect.collidepoint(yellow, mouse_position):
                        option4 =1
                    screen.fill("white")
                    pygame.display.flip()

def question_one():
    boxes(green=Green, blue=Blue, red=Red, yellow=Yellow)
    question = font_two.render("What's your favorite color?", True, "Black")
    screen.blit(question, (x_center/3, y_center/6))
    one = font_two.render("Green", True, "Black")
    screen.blit(one, (115, 245))
    two = font_two.render("Blue", True, "Black")
    screen.blit(two, (x_center+200, 245))
    three = font_two.render("Red", True, "Black")
    screen.blit(three, (115, y_center+100))
    four = font_two.render("Yellow", True, "Black")
    screen.blit(four, (x_center+200, y_center+100))
    pygame.display.flip()
    answer(green=Green, blue=Blue, red=Red, yellow=Yellow)

def question_two():
    boxes(green=Green, blue=Blue, red=Red, yellow=Yellow)
    question = font_two.render("What's your favorite hobby?", True, "Black")
    screen.blit(question, (x_center/3, y_center/6))
    one = font_two.render("Reading", True, "Black")
    screen.blit(one, (115, 245))
    two = font_two.render("Playing an Instrument", True, "Black")
    screen.blit(two, (x_center+200, 245))
    three = font_two.render("Coding", True, "Black")
    screen.blit(three, (115, y_center+100))
    four = font_two.render("Playing a Sport", True, "Black")
    screen.blit(four, (x_center+200, y_center+100))
    pygame.display.flip()
    answer(green=Green, blue=Blue, red=Red, yellow=Yellow)

    



def main():
    #Create an instance on your controller object
    #Call your mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(purple, mouse_position):
                    screen.fill("white")
                    pygame.display.flip()
                    question_one()
                    question_two()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
