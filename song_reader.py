import time
from codrone_edu.drone import *
drone = Drone()


"""put in a list of tuples with the notes and duration
Ex.
my_song = {
    (Note.X, duration),
    (Note.Y, duration),
    (Note.Z, duration),
}"""


def play_song_list(song, RGB_color="off"):
    light_toggle = True
    for note, duration in song:
        drone.drone_buzzer(note, duration)
        # flashs on and off with the rhythm if an rgb color is given
        if RGB_color != "off":
            drone.set_drone_LED(RGB_color if toggle else "off")
            drone.set_controller_LED(RGB_color if toggle else "off")
            toggle = not toggle
        if note == Note.REST:
            time.sleep(duration / 1000.0)  # pause for rest duration
        else:
            drone.drone_buzzer(note, duration)
            time.sleep(duration / 1000.0)  # wait so LED flashing syncs
    drone.set_drone_LED("off")
    drone.set_controller_LED("off")


                
            



