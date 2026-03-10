from setuptools import setup

setup(
    name="devpulse",
    version="0.1.0",
    description="AI-powered developer productivity CLI",
    author="Manucian Official",
    py_modules=["cli", "scanner", "analyzer", "dashboard", "ai_commit", "utils"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "devpulse=cli:main"
        ]
    },
)