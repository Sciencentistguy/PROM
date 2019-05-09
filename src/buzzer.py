import RPi.GPIO as GPIO
import time

c = [32, 65, 131, 262, 523]
db = [34, 69, 139, 277, 554]
d = [36, 73, 147, 294, 587]
eb = [37, 78, 156, 311, 622]
e = [41, 82, 165, 330, 659]
f = [43, 87, 175, 349, 698]
gb = [46, 92, 185, 370, 740]
g = [49, 98, 196, 392, 784]
ab = [52, 104, 208, 415, 831]
a = [55, 110, 220, 440, 880]
bb = [58, 117, 223, 466, 932]
b = [61, 123, 246, 492, 984]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  #(middle GPIO pin)

PWM = GPIO.PWM(18, 100)  #set default freq 100Hz
PWM.ChangeDutyCycle(0)
PWM.start(0)


def testBuzzer():
    try:
        PWM.start(0)
        PWM.ChangeDutyCycle(10)
        while True:
            for i in range(5, 1000, 5):
                PWM.ChangeFrequency(i)
                time.sleep(0.1)
            for i in range(1000, 0, -5):
                PWM.ChangeFrequency(i)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass


# testBuzzer()


def beep(note):
    PWM.ChangeFrequency(note)
    PWM.ChangeDutyCycle(10)
    time.sleep(0.6)
    PWM.ChangeDutyCycle(0)


# SONGS ("Sheet Music")

#Star Wars Theme -- Key of C
megalovania = [d[3], d[3], d[4], 0, a[4], 0, ab[4], g[3], f[3], d[3], f[3], g[3]]
starwars_notes = [c[1], g[1], f[1], e[1], d[1], c[2], g[1], f[1], e[1], d[1], c[2], g[1], f[1], e[1], f[1], d[1]]
starwars_beats = [4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4]
megalovania_b = [1, 1, 1, 1, 2, 1, 2, 2, 2, 3, 3, 3]

# songnotes: list of the melodies notes
# songbeats: list of melodies beat times
# tempo: speed of song, this is not traditional tempo in bpm like on a metronome,
# but more like a multiplier for whatever the notes are so a tempo value of 2
# make it play twice as fast. Adjust this by ear.

#This function plays the melody, simply by iterating through the list.


def playSong(songnotes, songbeats, tempo):
    PWM.ChangeDutyCycle(50)
    for i in range(0, len(songnotes)):
        PWM.ChangeFrequency(songnotes[i])
        time.sleep(songbeats[i] * tempo)
    PWM.ChangeDutyCycle(0)


def playStarwars():
    playSong(starwars_notes, starwars_beats, 0.2)


def dududududododoooooodododod():
    playSong(megalovania, megalovania_b, 0.2)


def cleanup():
    PWM.stop()
    GPIO.cleanup()
