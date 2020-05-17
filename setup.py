import setuptools


setuptools.setup(
    name="mkdocs-plugin-commonmark",
    version="0.0.4",
    packages=setuptools.find_packages(),
    description="A plugin for MkDocs that monkeypatches to support commonmark via mistletoe.",
    keywords=["mkdocs", "plugin", "commonmark", "mistletoe", "markdown"],
    author="Rajiv Makhijani",
    author_email="rajiv@auditboard.com",
    license="BSD",
    entry_points={
        "mkdocs.plugins": [
            "commonmark = mkdocs_plugin_commonmark:CommonMark"
        ]
    },
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/soxhub/mkdocs-plugin-commonmark",
    python_requires=">=3.4",
    include_package_data=True,
    install_requires=open("requirements.txt", "r").readlines(),
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.4',
    ]
)
