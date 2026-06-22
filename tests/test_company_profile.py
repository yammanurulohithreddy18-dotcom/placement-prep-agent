from models.company_profile import CompanyProfile


def test_company_profile_creation():

    profile = CompanyProfile(
        company_name="LG",
        founded="1947",
        headquarters="Seoul",
        tech_stack=["Python"],
        interview_rounds=["OA"],
        key_topics=["DSA"],
        difficulty="Medium"
    )

    assert profile.company_name == "LG"


def test_tech_stack_is_list():

    profile = CompanyProfile(
        company_name="LG",
        founded="1947",
        headquarters="Seoul",
        tech_stack=["Python"],
        interview_rounds=["OA"],
        key_topics=["DSA"],
        difficulty="Medium"
    )

    assert isinstance(profile.tech_stack, list)


def test_rounds_count():

    profile = CompanyProfile(
        company_name="LG",
        founded="1947",
        headquarters="Seoul",
        tech_stack=["Python"],
        interview_rounds=["OA", "Tech"],
        key_topics=["DSA"],
        difficulty="Medium"
    )

    assert len(profile.interview_rounds) == 2


def test_topics_exist():

    profile = CompanyProfile(
        company_name="LG",
        founded="1947",
        headquarters="Seoul",
        tech_stack=["Python"],
        interview_rounds=["OA"],
        key_topics=["DSA"],
        difficulty="Medium"
    )

    assert "DSA" in profile.key_topics


def test_difficulty():

    profile = CompanyProfile(
        company_name="LG",
        founded="1947",
        headquarters="Seoul",
        tech_stack=["Python"],
        interview_rounds=["OA"],
        key_topics=["DSA"],
        difficulty="Medium"
    )

    assert profile.difficulty == "Medium"