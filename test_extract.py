from extract_skills import extract_skills

def test_extract_basic():
    text = "Looking for experience in Power Apps and SharePoint Online."
    skills = extract_skills(text)
    assert "Power Apps" in skills
    assert "SharePoint Online" in skills
