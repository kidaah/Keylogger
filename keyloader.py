from pynput import keyboard

# List to store keys
typed_keys = []

def on_press(key):
    try:
        # Record the key
        typed_keys.append(key.char)
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        if key == keyboard.Key.space:
            typed_keys.append(" ")
        elif key == keyboard.Key.enter:
            typed_keys.append("\n")
        else:
            typed_keys.append(f"<{key.name}>")

    # Print current text live
    print("".join(typed_keys))

def on_release(key):
    # Stop tracking if ESC is pressed
    if key == keyboard.Key.esc:
        print("\nTracking stopped.")
        return False

# Start the listener
print("Start typing (Press ESC to stop):")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
