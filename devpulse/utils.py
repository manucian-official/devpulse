import os
from pathlib import Path

# Mapping extension -> language
EXTENSION_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".go": "Go",
    ".rs": "Rust"
}


def detect_language(file_path):
    ext = Path(file_path).suffix.lower()
    return EXTENSION_MAP.get(ext, "Unknown")


def count_todos(text):
    keywords = ["todo", "fixme", "hack"]
    text = text.lower()
    return sum(text.count(word) for word in keywords)


def scan_files(path):
    path = Path(path)
    code_files = []

    for file in path.rglob("*"):
        if file.suffix.lower() in EXTENSION_MAP:
            code_files.append(file)

    return code_files


def analyze_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        return {
            "file": str(file_path),
            "language": detect_language(file_path),
            "lines": content.count("\n") + 1,
            "todos": count_todos(content)
        }

    except Exception as e:
        return {
            "file": str(file_path),
            "error": str(e)
        }


def analyze_project(path):
    results = []
    files = scan_files(path)

    for file in files:
        results.append(analyze_file(file))

    return results


if __name__ == "__main__":
    project_path = "./"

    report = analyze_project(project_path)

    for item in report:
        print(item)
