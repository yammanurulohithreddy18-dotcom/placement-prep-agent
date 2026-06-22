from utils.logger import log_agent


def test_logger_runs():

    log_agent(
        "TestAgent",
        "Testing"
    )

    assert True


def test_logger_multiple():

    log_agent(
        "Agent",
        "Action"
    )

    assert True


def test_logger_string():

    log_agent(
        "A",
        "B"
    )

    assert True