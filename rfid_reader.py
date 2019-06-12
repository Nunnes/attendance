import sys
from evdev import InputDevice, list_devices, ecodes, categorize
import random
from io import StringIO

DEVICE_NAME = "Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader"
CODE_MAP_CHAR = {
    'KEY_0': "0",
    'KEY_1': "1",
    'KEY_2': "2",
    'KEY_3': "3",
    'KEY_4': "4",
    'KEY_5': "5",
    'KEY_6': "6",
    'KEY_7': "7",
    'KEY_8': "8",
    'KEY_9': "9",
    }

def parse_key_to_char(val):
    return CODE_MAP_CHAR[val] if val in CODE_MAP_CHAR else ""

def read_rfid_loop():
    device = grab_device(DEVICE_NAME)
    read_loop_device(device)

def print_device_list():
	print("List of your devices :")
	devices = [InputDevice(fn) for fn in list_devices()]
	for device in devices:
		print("\t{}\t{}".format(device.fn, device.name))

def grab_device():
    devices = [InputDevice(fn) for fn in list_devices()]
    for device in devices:
        if device.name == DEVICE_NAME:
            device = InputDevice(device.fn)
            device.grab()
            return device

    return None
        
def select_target_device():
    print_device_list()

    print("Choose event ID :")
    event_id = input()
    
    print("Exclusive access to device ? [1 or 0] : ")
    exclusive_access = input()

    device = InputDevice('/dev/input/event{}'.format(event_id))
    if int(exclusive_access) == 1:
		device.grab()

    return device

def read_loop_device(device):
    code = ""
    result = StringIO()
    sys.stdout = result
    
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            e = categorize(event)
            if e.keystate == e.key_up:
                sys.stdout.write(parse_key_to_char(e.keycode))
                sys.stdout.flush()
    
    return result
        
    
if __name__ == "__main__":
    """device = select_target_device()"""
    device = grab_device(DEVICE_NAME)
    read_loop_device(device)

