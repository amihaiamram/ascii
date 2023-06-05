import keyboard
while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        try:
            ascii_code = ord(event.name)
            print('\nKey:', event.name)
            print('ASCII:', ascii_code)
        except TypeError:
            print('Invalid key:', event.name)
            print()
