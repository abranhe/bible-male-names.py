import setuptools

with open("readme.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "bible_male_names",
    packages = ["bible_male_names"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    version = "1.0.5",
    description = "Get male names from The Bible",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://p.abranhe.com/bible-male-names.py",
    classifiers=(
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ),
    project_urls={
        'Source': 'https://github.com/abranhe/bible-male-names.py',
        'Issue Tracker': 'https://github.com/abranhe/bible-male-names.py/issues'
    },
) 
