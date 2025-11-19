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
ACTION_VERBS = [
    "design", "develop", "build", "automate", "deploy",
    "configure", "customize", "implement", "integrate"
]

def extract_verbs(text):
    found = []
    for verb in ACTION_VERBS:
        if verb.lower() in text.lower():
            found.append(verb)
    return sorted(set(found))


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

   result = {
    "skills": skills,
    "action_verbs": extract_verbs(text)
}
OUT_FILE.write_text(json.dumps(result, indent=2))

    print("✅ Skills extracted and saved to skills.json")
    print(skills)


if __name__ == "__main__":
    main()
