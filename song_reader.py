from codrone_edu.drone import *
drone = Drone()


"""function that takes a dictionary with the key:value format of note:duration
 and plays it along with optionally flashing the drone and controller's LED light."""


def play_song_dict(song, RGB_color="off"):
    light_toggle = True
    for note, duration in song.items():
        drone.drone_buzzer(note, duration)
        # flashs on and off with the rhythm if an rgb color is given
        if RGB_color != "off":
            if light_toggle = True:
                drone.set_drone_LED(RGB_color)
                drone.set_controller_LED(RGB_color)
                light_toggle = False
            else:
                drone.set_drone_LED("off")
                drone.set_controller_LED("off")
                light_toggle = True
                
            



