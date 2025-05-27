import song_reader
import time
from codrone_edu.drone import *
drone = Drone()
drone.pair()

minecraft_sweden = [
    (Note.E4, 600),
    (Note.G4, 600),
    (Note.A4, 600),
    (Note.REST, 300),
    (Note.B4, 600),
    (Note.A4, 600),
    (Note.G4, 600),
    (Note.REST, 400),
    (Note.E4, 900),

    (Note.E4, 600),
    (Note.G4, 600),
    (Note.A4, 600),
    (Note.REST, 300),
    (Note.B4, 600),
    (Note.A4, 600),
    (Note.G4, 600),
    (Note.REST, 400),
    (Note.E4, 900),

    (Note.E4, 600),
    (Note.G4, 600),
    (Note.A4, 600),
    (Note.B4, 400),
    (Note.B4, 200),
    (Note.A4, 600),
    (Note.G4, 600),
    (Note.E4, 900)
]


ddlc_theme = [
    (Note.C5, 400),
    (Note.E5, 400),
    (Note.G5, 600),
    (Note.REST, 200),
    (Note.G5, 400),
    (Note.A5, 400),
    (Note.G5, 600),
    (Note.E5, 400),
    (Note.C5, 400),
    (Note.REST, 400),

    (Note.E5, 400),
    (Note.G5, 400),
    (Note.A5, 600),
    (Note.REST, 200),
    (Note.A5, 400),
    (Note.G5, 400),
    (Note.E5, 600),
    (Note.C5, 400),
    (Note.REST, 400),

    (Note.C5, 400),
    (Note.D5, 400),
    (Note.E5, 600),
    (Note.REST, 400),

    (Note.E5, 400),
    (Note.F5, 400),
    (Note.G5, 600),
    (Note.REST, 400),
]


wii_u_theme = [
    (Note.C5, 400),
    (Note.E5, 400),
    (Note.G5, 600),
    (Note.REST, 200),
    (Note.G5, 400),
    (Note.A5, 400),
    (Note.G5, 600),
    (Note.E5, 400),
    (Note.C5, 400),
    (Note.REST, 400),

    (Note.E5, 400),
    (Note.G5, 400),
    (Note.A5, 600),
    (Note.REST, 200),
    (Note.A5, 400),
    (Note.G5, 400),
    (Note.E5, 600),
    (Note.C5, 400),
    (Note.REST, 400),
]


chug_jug_with_you = [
    (Note.E4, 400),
    (Note.G4, 400),
    (Note.A4, 600),
    (Note.G4, 400),
    (Note.E4, 400),
    (Note.D4, 600),
    (Note.REST, 300),

    (Note.E4, 400),
    (Note.G4, 400),
    (Note.A4, 600),
    (Note.G4, 400),
    (Note.E4, 400),
    (Note.D4, 600),
    (Note.REST, 300),

    (Note.C4, 600),
    (Note.D4, 400),
    (Note.E4, 400),
    (Note.F4, 600),
    (Note.G4, 400),
    (Note.E4, 400),
    (Note.D4, 600),
]