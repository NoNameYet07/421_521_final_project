#! /usr/bin/python

import picamera

camera=picamera.PiCamera()
camera.capture('image.jpg')
