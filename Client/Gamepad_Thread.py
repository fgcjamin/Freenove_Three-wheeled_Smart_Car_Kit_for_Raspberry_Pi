from Gamepad import Gamepad as pad
import inputs

#from TCPClient import TCPClient
#from Command import COMMAND as cmd

#from Freenove_Math import * 
#import time
import threading
#import math
#from CloseThreading import *

class Gamepad_Thread(threading.Thread):
    def __init__(self, widget):
        super(Gamepad_Thread, self).__init__()
        self.wgt_main = widget
        self.isRun = True

    def reset(self):
        print('GamepadThread : Cleared & Zeroed')
        #enable_motors()
        #enable_safeties()
        #stop('clear and zero')

    def button_not_set(self, state):
        print("Button Not Set")

    def hello(self, state):
        print("Hello !")

    def celebrate(self, state):
        print("Celebrate !")

    def circledance(self, state):
        print("Circle Dance :)")
    
    def turn(self, state):
        print("turn")
    
    def forward(self, state, threshold):
        print("forward " + str(state) + " threshold=" + str(threshold))

    def camera_X(self, state):
        print("camera left or right")
    
    def camera_Y(self, state):
        print("camera up or down")

    def get_event_dict(self):
        '''
        Set which actions happen when buttons and joysticks change:
        '''
        event_dict = {
            pad.HAT_X : self.turn,
            pad.HAT_Y : lambda state: self.forward(state, 25), 
            pad.STICK_L_X : self.turn,
            pad.STICK_L_Y : lambda state: self.forward(state, 50),
            pad.STICK_R_X : self.camera_X,
            pad.STICK_R_Y : self.camera_Y,
            pad.BTN_WEST : self.circledance,
            pad.BTN_EAST : self.celebrate,
            pad.BTN_SOUTH : self.hello,
            pad.BNT_NORTH : self.button_not_set,
            pad.BNT_STICK_L : self.button_not_set,
            pad.BTN_STICK_R : self.button_not_set,
            pad.BTN_HEAD_R_U : self.button_not_set,
            pad.BTN_HEAD_R_D : self.button_not_set,
            pad.BTN_HEAD_L_U : self.button_not_set,
            pad.BTN_HEAD_L_D : self.button_not_set,
            pad.BTN_TRIG_R : self.button_not_set,
            pad.BTN_TRIG_L : self.button_not_set,
            }
        return event_dict
    
    def event_loop(self, events):
        '''
        This function is called in a loop, and will get the events from the
        controller and send them to the functions we specify in the `event_dict`
        dictionary
        '''
        for event in events:
            #print('\t', event.ev_type, event.code, event.state)
            call = self.get_event_dict().get(event.code)
            if callable(call):
                call(event.state)

    def run(self):
        pads = inputs.devices.gamepads

        if len(pads) == 0:
            raise Exception("Couldn't find any Gamepads!")

        self.reset()

        while self.isRun:
            self.event_loop(inputs.get_gamepad())
