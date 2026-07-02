from mycode.runtime import ConversationStore


def test_create_conversation() -> None:
    store = ConversationStore()

    conversation_id = store.create()

    assert store.exists(conversation_id)
    assert len(store) == 1


def test_get_conversation() -> None:
    store = ConversationStore()

    conversation_id = store.create()

    conversation = store.get(conversation_id)

    assert conversation is not None


def test_delete_conversation() -> None:
    store = ConversationStore()

    conversation_id = store.create()

    store.delete(conversation_id)

    assert not store.exists(conversation_id)


def test_clear_store() -> None:
    store = ConversationStore()

    store.create()
    store.create()

    store.clear()

    assert len(store) == 0
