from setuptools import setup, find_packages

setup(
    name="devpulse-tool",
    version="0.1.0",
    description="AI-powered developer productivity analyzer",
    author="manucian-official",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "devpulse=devpulse.cli:main"
        ]
    },
    python_requires=">=3.8",
)