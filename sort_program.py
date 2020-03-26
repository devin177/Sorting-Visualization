"""This is a visualization of bubble sort using pygame"""
import pygame
from value import Value
from button import Button

pygame.init()

def main():
    """This is the main function"""

    #setup for the display window
    dimensions = (1000, 700)
    window = pygame.display.set_mode(dimensions)
    pygame.display.set_caption("Bubble Sort")

    #create buttons
    finish_button = Button(window, (0, 255, 0), 0, 700, 250, -100, "Finish")
    forward_button = Button(window, (255, 0, 0), 250, 700, 250, -100, "Forwards")
    switch_algorithm_button = Button(window, (200, 200, 200), 500, 700, 250, -100, "Switch Algorithm")

    num = [7, 2, 9, 17, 12, 1, 3, 5]

    #Create a list of bubbles based on a list of ints
    num_list = []
    for i in num:
        num_list.append(Value(i))
    width = dimensions[0]/len(num_list)
    iteration = 0

    #Game/Display loop
    #Will set the background to white
    running = True
    while running:
        #Reset the background to white
        window.fill((255, 255, 255))
        finish_button.draw()
        forward_button.draw()
        switch_algorithm_button.draw()
        pos = pygame.mouse.get_pos()

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if finish_button.above(pos):
                    finish_button.color = (0, 255, 100)
                else:
                    finish_button.color = (0, 255, 0)
                if forward_button.above(pos):
                    forward_button.color = (255, 0, 100)
                else:
                    forward_button.color = (255, 0, 0)
                if switch_algorithm_button.above(pos):
                    switch_algorithm_button.color = (255, 255, 255)
                else:
                    switch_algorithm_button.color = (200, 200, 200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if forward_button.above(pos):
                    for j in range(0, len(num_list)-iteration-1):
                        temp = num_list[j].value
                        if num_list[j].value > num_list[j+1].value:
                            num_list[j].value = num_list[j+1].value
                            num_list[j+1].value = temp
                    iteration += 1

                if finish_button.above(pos):
                    for i in range(0, len(num_list)):
                        for j in range(0, len(num_list)-iteration-1):
                            temp = num_list[j].value
                            if num_list[j].value > num_list[j+1].value:
                                num_list[j].value = num_list[j+1].value
                                num_list[j+1].value = temp

                if switch_algorithm_button.above(pos):
                    iteration = 0

        #draw each member of the list
        for i, entry in enumerate(num_list):
            entry.draw(window, i*width, width)

        #update the display
        pygame.display.flip()

#calling main function
if __name__ == "__main__":
    main()
