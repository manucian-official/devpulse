from collections import defaultdict
from utils import detect_language, count_todos

COMPLEX_KEYWORDS = [
    "if","for","while","switch","case","try","except","catch"
]

def complexity_score(lines):

    score = 0

    for line in lines:
        for key in COMPLEX_KEYWORDS:
            if key in line:
                score += 1

    return score


def analyze_code(files):

    languages = defaultdict(int)
    todos = 0
    largest_file = ("",0)
    complexity_total = 0

    for file in files:

        with open(file,"r",encoding="utf8",errors="ignore") as f:
            lines = f.readlines()

        line_count = len(lines)

        lang = detect_language(file)
        languages[lang] += line_count

        if line_count > largest_file[1]:
            largest_file = (file,line_count)

        todos += count_todos(lines)

        complexity_total += complexity_score(lines)

    return {
        "languages":languages,
        "todos":todos,
        "largest_file":largest_file,
        "complexity":complexity_total
    }