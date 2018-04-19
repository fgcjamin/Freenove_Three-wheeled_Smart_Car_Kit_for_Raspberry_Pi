class Gamepad:
    # event.ev_type
    EV_STICK = "Absolute"
    EV_BTN = "Key"
    EV_SYNC = "Sync"
    EV_MISC = "Misc"

    # event.code for event.ev_type==EV_STICK
    HAT_X = "ABS_HAT0X"
    HAT_Y = "ABS_HAT0Y"
    STICK_L_X = "ABS_X"
    STICK_L_Y = "ABS_Y"
    STICK_R_X = "ABS_RZ"
    STICK_R_Y = "ABS_THROTTLE"
    
    STICKS_RANGES = {'ABS_RZ': (-128, 127),
                     'ABS_THROTTLE': (0, 255),
                     'ABS_HAT0Y': (-1, 1),
                     'ABS_HAT0X': (-1, 1),
                     'ABS_X': (-120, 118),
                     'ABS_Y': (-126, 127)}

    # event.code for event.ev_type==EV_BTN
    BTN_WEST = "BTN_EAST"
    BTN_EAST = "BTN_C"
    BTN_SOUTH = "BTN_SOUTH"
    BNT_NORTH = "BTN_NORTH"

    BNT_STICK_L = "BTN_SELECT"

    BTN_STICK_R = "BTN_START"

    BTN_HEAD_R_U = "BTN_TL"
    BTN_HEAD_R_D = "BTN_TR"
    BTN_HEAD_L_U = "BTN_WEST"
    BTN_HEAD_L_D = "BTN_Z"

    BTN_TRIG_R = "BTN_TR2"
    BTN_TRIG_L = "BTN_TL2"
