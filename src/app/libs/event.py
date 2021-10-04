# Simple eventing system.
# Writen to increase cohesion in the system, reduce coupling and DRY.
# Usage:
# 1. Subscribe to an event
# def my_fn(data):
#     pass
# event.subscribe("user-created", my_fn)
# 2. Post an event and subscriber (fn) will be called with the event data
# ev_data = {"user": "Frank Doyle"}
# event.post_event("user-created", ev_data)
# 3. Call to fn(ev_data) was made

from typing import Callable, Any


subscribers = {}


def subscribe(ev_name: str, fn: Callable):
    if ev_name not in subscribers:
        subscribers[ev_name] = []
    subscribers[ev_name].append(fn)


def clear_subscribers(ev_name: str):
    if ev_name not in subscribers:
        return
    subscribers[ev_name] = []


def post_event(ev_name: str, ev_data: Any):
    if ev_name not in subscribers:
        return
    for fn in subscribers[ev_name]:
        fn(ev_data)
