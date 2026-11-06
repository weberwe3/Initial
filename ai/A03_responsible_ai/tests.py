TEXT = "Contact jane.doe@example.com or (555) 123-4567; cc bob@corp.co.uk, 555.987.6543."


def test_redact_emails(ex):
    assert ex.redact_emails(TEXT) == "Contact [EMAIL] or (555) 123-4567; cc [EMAIL], 555.987.6543."


def test_redact_phones(ex):
    got = ex.redact_phones("Call 555-123-4567 or (555) 123-4567 or 555.987.6543 re order 12345.")
    assert got == "Call [PHONE] or [PHONE] or [PHONE] re order 12345.", f"got {got!r}"


def test_redact_pii(ex):
    got = ex.redact_pii("Acme Corp emailed a@b.com; ACME CORP wants a call at 555-111-2222.", ["acme corp"])
    assert got == "[REDACTED] emailed [EMAIL]; [REDACTED] wants a call at [PHONE].", f"got {got!r}"


def test_find_pii(ex):
    assert ex.find_pii(TEXT) == {"emails": 2, "phones": 2}
    assert ex.find_pii("nothing here") == {"emails": 0, "phones": 0}


def test_pseudonymise(ex):
    rows = [{"customer": "Ann", "spend": 10}, {"customer": "Bo", "spend": 5}, {"customer": "Ann", "spend": 7}]
    got = ex.pseudonymise(rows, "customer")
    assert [r["customer"] for r in got] == ["CUST_001", "CUST_002", "CUST_001"]
    assert [r["spend"] for r in got] == [10, 5, 7]
    assert rows[0]["customer"] == "Ann", "don't modify the original rows"
    assert ex.pseudonymise(rows, "customer", prefix="C")[1]["customer"] == "C_002"


def test_drop_columns(ex):
    rows = [{"name": "Ann", "email": "a@b.com", "spend": 10}]
    assert ex.drop_columns(rows, ["name", "email"]) == [{"spend": 10}]
    assert "email" in rows[0], "don't modify the original rows"


def test_safe_to_share(ex):
    assert ex.safe_to_share("Revenue up 4% in Q3", ["Project Falcon"]) is True
    assert ex.safe_to_share("Update on project falcon", ["Project Falcon"]) is False
    assert ex.safe_to_share("ping a@b.com", []) is False
