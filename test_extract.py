from extract_skills import extract_skills, extract_verbs

def test_extract_basic():
    text = "Experience in Power Apps and SharePoint Online."
    skills = extract_skills(text)

    assert "Power Apps" in skills
    assert "SharePoint Online" in skills

def test_extract_verbs():
    text = "We design and build Power Apps solutions."
    verbs = extract_verbs(text)

    assert "design" in verbs
    assert "build" in verbs
