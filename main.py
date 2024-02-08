#!/usr/bin/env python3
import playsound
import time
import sys

def main(code:str) -> None:

    for an in code:
        try:
            playsound.playsound(f"mp3/{an}.mp3")
        except:
            error()

        time.sleep(0.5)

def error():
    playsound.playsound("mp3/error1.mp3")
    playsound.playsound("mp3/error2.mp3")

    sys.exit()

if __name__=="__main__":
    if not 2 == len(sys.argv):
        error()

    main(sys.argv[1])
