


import pygame
from datetime import datetime
from rpm.rpm import RpmGauge
from aux_gauge.AuxGauge import AuxGauge
from constants import *
from variables import *
from draw import *


# Setup Display
pygame.init()

# Title and Icon
pygame.display.set_icon(programIcon)
pygame.display.set_caption(project_name + digifiz_ver)

# Font Information
odo_font = pygame.font.Font(FONT_PATH, FONT_SMALL)
digital_font = pygame.font.Font(FONT_PATH, FONT_MEDIUM)
font_speedunits = pygame.font.Font(FONT_PATH, FONT_LARGE)

# Setup Game Loop
clock = pygame.time.Clock()

#   Create gauge instances from classes.
boost = AuxGauge(BOOST_XY, 19)
egt = AuxGauge(EGT_XY, 19)
coolant = AuxGauge(COOLANT_XY, 19)
oilpressure = AuxGauge(OILPRESSURE_XY, 19)
rpm = RpmGauge(RPM_XY, 50)


#   Creating the list for the indicator gauges
indicator_images = []
for i in range(10):
    image = pygame.image.load(("images/indicators/ind" + str(i) + ".png"))
    indicator_images.append(image)



#####
#       Functions for Drawing onto the screen
#####

def draw_fuel_text():
    #global digital_font
    digital_fuel = fuel_status
    fuel_text = digital_font.render(str(int(digital_fuel)), True, NEON_GREEN)
    text_rect = fuel_text.get_rect()
    text_rect.midright = 1717, 667
    WIN.blit(fuel_text, text_rect)


def draw_speedometer_text():
    '''
    Speedometer text and write
    '''
    global speed_status
    global font_speedunits
    speedtext = font_speedunits.render(str(speed_status), True, NEON_YELLOW)
    text_rect = speedtext.get_rect()
    text_rect.midright = SPEEDO_XY
    WIN.blit(speedtext, text_rect)

def draw_mfa():
    '''
    Drawing the interior temp only currently - the MFA will eventually evolve.
    '''
    #global outside_temp_status

    WIN.blit(MFA, MFABG_XY)
    #   Draw MFA display
    text = digital_font.render(str(outside_temp_status), True, NEON_GREEN)
    #   Enables the text to be right center aligned
    text_rect = text.get_rect()
    text_rect.midright = MFA_XY
    WIN.blit(text, text_rect)




def draw_indicators():
    '''
    The area where I blit or draw the indicators/idiot lights and turn signals/low fuel etc.
    '''

    if illumination_state == 1:
        WIN.blit(indicator_images[0], (45, 460))
    if foglight_state == 1:
        WIN.blit(indicator_images[1], (185, 460))
    if defog_state == 1:
        WIN.blit(indicator_images[2], (325, 460))
    if highbeam_state == 1:
        WIN.blit(indicator_images[3], (465, 460))
    if leftturn_state == 1:
        WIN.blit(indicator_images[4], (605, 460))
    if rightturn_state == 1:
        WIN.blit(indicator_images[5], (1220, 460))
    if brakewarn_state == 1:
        WIN.blit(indicator_images[6], (1360, 460))
    if oillight_state == 1:
        WIN.blit(indicator_images[7], (1500, 460))
    if alt_state == 1:
        WIN.blit(indicator_images[8], (1640, 460))
    if glow_state == 1:
        WIN.blit(indicator_images[9], (1780, 460))

    #   To highlight the fuel reserve indicator (factory is at 7 litres
    if fuel_status <= 7:
        WIN.blit(fuelresOn, (1795, 616))
    else:
        WIN.blit(fuelresOff, (1795, 616))

#   Main Drawings for the program - Background + Gauges
def draw_digifiz():
    WIN.blit(BACKGROUND, (0, 0))
    rpm.show(WIN)
    coolant.show(WIN)
    boost.show(WIN)
    oilpressure.show(WIN)
    egt.show(WIN)
    mileage()
    draw_indicators()
    draw_clock()
    draw_mfa()
    draw_fuel_text()
    draw_speedometer_text()

#####
#       Main Function for the Pygame Program
#####

def main():
    # Setup Game Loop
    clock = pygame.time.Clock()

    # Main Loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_digifiz()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
