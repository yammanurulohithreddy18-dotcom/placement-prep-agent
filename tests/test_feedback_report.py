from models.feedback_report import FeedbackReport


def test_feedback_creation():

    report = FeedbackReport(
        score=8,
        strengths=["Good"],
        improvements=["More examples"]
    )

    assert report.score == 8


def test_strengths_list():

    report = FeedbackReport(
        score=8,
        strengths=["Good"],
        improvements=[]
    )

    assert len(report.strengths) == 1


def test_improvements_list():

    report = FeedbackReport(
        score=8,
        strengths=[],
        improvements=["Practice"]
    )

    assert len(report.improvements) == 1


def test_score_range():

    report = FeedbackReport(
        score=10,
        strengths=[],
        improvements=[]
    )

    assert report.score <= 10


def test_empty_lists():

    report = FeedbackReport(
        score=5,
        strengths=[],
        improvements=[]
    )

    assert report.score == 5