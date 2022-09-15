import os

from setuptools import setup
from setuptools_rust import Binding, RustExtension

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(
    os.path.join(here, "fastcrc", "__info__.py"), mode="r", encoding="utf-8"
) as f:
    exec(f.read(), about)

with open("README.rst", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],
    rust_extensions=[RustExtension("fastcrc.fastcrc", binding=Binding.PyO3)],
    packages=["fastcrc"],
    include_package_data=True,
    package_data={"fastcrc": ["py.typed"]},
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    keywords=["crc", "crc16", "crc32", "crc64"],
    project_urls={
        "Code": "https://github.com/overcat/fastcrc",
        "Issue tracker": "https://github.com/overcat/fastcrc/issues",
    },
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
)
