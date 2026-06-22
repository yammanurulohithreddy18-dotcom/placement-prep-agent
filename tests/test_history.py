from utils.history import save_attempt
from utils.history import get_history


def test_history_returns_list():

    history = get_history()

    assert isinstance(history, list)


def test_save_attempt():

    save_attempt(
        "Test",
        "SDE",
        "Question",
        8
    )

    history = get_history()

    assert len(history) > 0


def test_latest_company():

    history = get_history()

    assert history[-1]["company"] == "Test"


def test_score_saved():

    history = get_history()

    assert history[-1]["score"] == 8


def test_role_saved():

    history = get_history()

    assert history[-1]["role"] == "SDE"