import sys
from scanner import scan_files
from analyzer import analyze_code
from dashboard import dashboard
from ai_commit import generate_commit

def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python main.py scan <project_path>")
        print("python main.py commit")
        return

    command = sys.argv[1]

    if command == "scan":

        path = sys.argv[2]

        files = scan_files(path)

        result = analyze_code(files)

        dashboard(result)

    elif command == "commit":

        generate_commit()

if __name__ == "__main__":
    main()