import os

BASE_DIR = "."

README_FILE = "README.md"
PROGRESS_FILE = "PROGRESS_TRACKER.md"

folders = sorted([
    folder for folder in os.listdir(BASE_DIR)
    if os.path.isdir(folder)
])

tracker_content = "# NeetCode 150 Progress Tracker\n\n"

total_questions = 0
completed_questions = 0

for folder in folders:

    files = sorted([
        file for file in os.listdir(folder)
        if file.endswith(".py")
    ])

    if not files:
        continue

    tracker_content += f"## {folder.replace('_', ' ')}\n\n"

    for file in files:

        filepath = os.path.join(folder, file)

        with open(filepath, "r") as f:
            content = f.read()

        done = "# status: done" in content

        status = "x" if done else " "

        question_name = (
            file.replace(".py", "")
            .replace("_", " ")
        )

        tracker_content += f"- [{status}] {question_name}\n"

        total_questions += 1

        if done:
            completed_questions += 1

    tracker_content += "\n"

percentage = round(
    (completed_questions / total_questions) * 100,
    2
) if total_questions else 0

tracker_content += "---\n\n"
tracker_content += "## Progress\n\n"
tracker_content += f"- Completed: {completed_questions}/{total_questions}\n"
tracker_content += f"- Percentage: {percentage}%\n"

# WRITE PROGRESS TRACKER

with open(PROGRESS_FILE, "w") as f:
    f.write(tracker_content)

# UPDATE README

readme_content = f"""# NeetCode 150 DSA Tracker

A structured NeetCode 150 tracking system organized by patterns for placement preparation.

## Progress

- Completed: {completed_questions}/{total_questions}
- Percentage: {percentage}%

## Full Progress Tracker

Check detailed tracking here:

PROGRESS_TRACKER.md
"""

with open(README_FILE, "w") as f:
    f.write(readme_content)

print("README.md and PROGRESS_TRACKER.md updated successfully!")
