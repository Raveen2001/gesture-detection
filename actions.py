from datetime import datetime
from pynput.keyboard import Key, Controller

keyboard = Controller()

last_detection_and_time = {}
COOLDOWN_TIME = 1


def ok():
    print("OK action needs to be performed")
    keyboard.press(Key.left)
    keyboard.release(Key.left)


def stop():
    print("Stop action needs to be performed")
    keyboard.press(Key.right)
    keyboard.release(Key.right)


def thumb_down():
    print("thumbs down action needs to be performed")
    keyboard.press(Key.down)
    keyboard.release(Key.down)


def thumb_up():
    print("thumbs up needs to be performed")
    keyboard.press(Key.up)
    keyboard.release(Key.up)


actions = {
    'ok': ok,
    'stop': stop,
    'thumb_down': thumb_down,
    'thumb_up': thumb_up,
}


def perform_action(action):
    global last_detection_and_time, actions
    action_to_be_performed = actions.get(action)
    last_performed_time = last_detection_and_time.get(action)
    now = datetime.now()

    if last_performed_time:
        diff = (now - last_performed_time).total_seconds()
        if diff > COOLDOWN_TIME:
            last_detection_and_time[action] = now
            action_to_be_performed()
        else:
            print("in cooldown", diff)

    else:
        last_detection_and_time[action] = now
        action_to_be_performed()
