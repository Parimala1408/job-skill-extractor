# extract_skills.py
# Extract skills from job_description.txt using simple NLP rules.

import json
from pathlib import Path

JD_FILE = Path("job_description.txt")
OUT_FILE = Path("skills.json")

# Define your skills list (you can expand anytime)
SKILLS_DB = [
    "Power Platform",
    "Power Apps",
    "Power Automate",
    "Power BI",
    "Dataverse",
    "Dynamics 365",
    "Finance and Operations",
    "SharePoint",
    "SharePoint Online",
    "Teams",
    "Microsoft Teams",
    "Azure DevOps",
    "CI/CD",
    "Model Driven App",
    "Canvas App",
    "SQL",
    "API",
    "Python"
]


def extract_skills(text):
    found = []
    for skill in SKILLS_DB:
        if skill.lower() in text.lower():
            found.append(skill)
    return sorted(set(found))


def main():
    if not JD_FILE.exists():
        print("❌ job_description.txt not found.")
        return

    text = JD_FILE.read_text(encoding="utf-8")
    skills = extract_skills(text)

    OUT_FILE.write_text(json.dumps(skills, indent=2))
    print("✅ Skills extracted and saved to skills.json")
    print(skills)


if __name__ == "__main__":
    main()
