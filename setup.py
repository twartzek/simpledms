import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpledms",
    version="0.1.4",
    author="twartzek",
    author_email="github@wartzek.de",
    description="A simple document management system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/twartzek/simpledms",
    packages=setuptools.find_packages(),
    license="GPLv3",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={"gui_scripts": ["simpledms = simpledms.__main__:mainfunc"]},
)
