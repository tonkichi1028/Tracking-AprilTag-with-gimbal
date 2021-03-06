#!/usr/bin/env python
# -*- coding: utf-8 -*-
                                                                    
#pwm: 7.25 +- 2.5

import time
import RPi.GPIO as GPIO

pitch_pin = 32
yaw_pin = 33



def main():


	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pitch_pin, GPIO.OUT, initial=GPIO.HIGH)
	pitch = GPIO.PWM(pitch_pin, 50)
	GPIO.setup(yaw_pin, GPIO.OUT, initial=GPIO.HIGH)
	yaw = GPIO.PWM(yaw_pin, 50)

	pitch.start(10.742)
	#pitch.start(4.5)
	time.sleep(1)
	pitch.stop()
	GPIO.cleanup()

if __name__ == '__main__':
	main()
