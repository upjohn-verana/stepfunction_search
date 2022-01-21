from sfn_search import check


def test_one():
    results = check()

    assert results == 1
