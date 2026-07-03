from hexlet_pytest.main import reverse


def test_reverse():
    print("до assert")
    assert reverse("Hexlet") == "telxeH"
    print("после assert")


def test_reverse_for_empty_string():
    assert reverse("") == ""
