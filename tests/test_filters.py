from src.filters import should_exclude

RULES = [{"field": "contact.email", "starts_with": "TEST", "case_insensitive": True}]


def test_filter_is_case_insensitive():
    assert should_exclude({"contact": {"email": "test-user@example.test"}}, RULES)


def test_eligible_record_is_not_filtered():
    assert not should_exclude({"contact": {"email": "customer@example.test"}}, RULES)
