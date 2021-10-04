from unittest import mock

from app.libs import event


def test_subscribing_adds_an_event():
    def my_fn(data):
        pass

    event.clear_subscribers("user-created")
    event.subscribe("user-created", my_fn)
    assert len(event.subscribers["user-created"]) == 1


def test_subscribing_adds_correct_event():
    def my_fn1(data):
        pass

    event.clear_subscribers("user-created")
    event.subscribe("user-created", my_fn1)
    assert event.subscribers["user-created"][0] == my_fn1


def test_can_clear_subscribers_for_event():
    def my_fn1(data):
        pass

    event.subscribe("user-created", my_fn1)
    event.clear_subscribers("user-created")
    assert len(event.subscribers["user-created"]) == 0


def test_posting_event_calls_subscriber():
    # create 2 mocks (i.e. 2 subscribers), so we can check later if they were called
    my_fn1 = mock.Mock()
    my_fn2 = mock.Mock()

    event.clear_subscribers("user-created")
    event.subscribe("user-created", my_fn1)
    event.subscribe("user-created", my_fn2)

    ev_data = {"user": "Frank Doyle"}
    event.post_event("user-created", ev_data)

    # posting event should call subscribers with the data passed-in
    my_fn1.assert_called_with(ev_data)
    my_fn2.assert_called_with(ev_data)
