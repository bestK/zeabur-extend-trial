from zeabur_extend_trial import main


def test_checkin():
    res = main.checkin()
    assert 'errors' not in res
