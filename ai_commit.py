import git
from openai import OpenAI

def generate_commit():

    repo = git.Repo(".")
    diff = repo.git.diff()

    client = OpenAI()

    prompt = f"""
Generate a concise git commit message based on this diff:

{diff[:2000]}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    print("\nSuggested Commit Message:\n")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    generate_commit()