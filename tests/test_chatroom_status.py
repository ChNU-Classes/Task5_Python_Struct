from src.chatroom_status import chatroom_status


def test_chatroom_status1():
    assert chatroom_status(["Ann"]) == "Ann online"


def test_chatroom_status2():
    assert chatroom_status([]) == "no one online"


def test_chatroom_status3():
    assert chatroom_status(["Ann", "Mark"]) == "Ann and Mark online"


def test_chatroom_status4():
    assert chatroom_status(["Ann", "Mark", "Jhon", "Joy", "Pet"]) == "Ann, Mark and 3 more online"

