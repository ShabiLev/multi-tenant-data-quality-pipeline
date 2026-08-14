from src.flatten import flatten


def test_nested_document_is_flattened():
    assert flatten({"contact": {"email": "a@example.test"}, "status": "ACTIVE"}) == {
        "contact.email": "a@example.test",
        "status": "ACTIVE",
    }
