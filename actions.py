from datetime import datetime

last_detection_and_time = {}
COOLDOWN_TIME = 10


def ok():
    print("OK action needs to be performed")


def stop():
    print("Stop action needs to be performed")


def thumb_down():
    print("thumbs down action needs to be performed")


def thumb_up():
    print("thumbs up needs to be performed")


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
