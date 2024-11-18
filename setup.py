import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "slim-wordy"
AUTHOR_USER_NAME = "typ1cal"
SRC_REPO = "slim_wordy"
AUTHOR_EMAIL = "yashwadhawe@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python Package for generating slim and wordy sentences.",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/typ1cal/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/typ1cal/" + SRC_REPO + "/issues",
    }
),
package_dir={"": "src"},
packages=setuptools.find_packages(where="src")