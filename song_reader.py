from codrone_edu.drone import *
drone = Drone()


"""function that takes a dictionary with the key:value format of note:duration
 and plays it along with optionally flashing the drone and controller's LED light"""


def play_song_dict(song, RGB_color="off"):
    for note, duration in song.items():
        drone.drone_buzzer(note, duration)
        

