#!/usr/bin/env python3
"""
Setup script for sonar-client package
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Sonar API Client - A Python client for the Sonar network management system"

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return ['requests>=2.25.0', 'beautifulsoup4>=4.9.0']

setup(
    name="sonar-client",
    version="1.0.0",
    author="SonarAPI Team",
    author_email="support@example.com",
    description="A Python client for the Sonar network management system",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/jlportman3/SonarAPI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
            'mypy>=0.800',
        ],
    },
    keywords="sonar api client network management isp telecommunications",
    project_urls={
        "Bug Reports": "https://github.com/jlportman3/SonarAPI/issues",
        "Source": "https://github.com/jlportman3/SonarAPI",
        "Documentation": "https://github.com/jlportman3/SonarAPI/tree/main/sonar_client",
    },
    include_package_data=True,
    zip_safe=False,
)
