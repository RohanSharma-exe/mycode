from mycode.llm import Conversation


def test_empty_conversation() -> None:
    conversation = Conversation()

    assert len(conversation) == 0


def test_add_user_message() -> None:
    conversation = Conversation()

    conversation.add_user("Hello")

    assert len(conversation) == 1
    assert conversation.messages[0].content == "Hello"


def test_clear() -> None:
    conversation = Conversation()

    conversation.add_user("Hello")
    conversation.add_assistant("Hi!")

    conversation.clear()

    assert len(conversation) == 0
