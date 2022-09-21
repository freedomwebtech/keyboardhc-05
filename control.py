from pynput.keyboard import Key, Listener
import serial

bluetooth=serial.Serial("/dev/rfcomm7",9600)


def on_press(key):
    print('{0} pressed'.format(key))
    if key==key.up:
       a=1
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))
    if key==key.down:
       a=4
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))
    if key==key.left:
       a=3
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))
    if key==key.right:
       a=2
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))         

def on_release(key):
    print('{0} release'.format(key))
    if key==key.up:
       a=0
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))
    if key==key.down:
       a=0
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))
    if key==key.left:
       a=0
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))
    if key==key.right:
       a=0
       string='X{0}'.format(a)
       bluetooth.write(string.encode("utf-8"))           
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
