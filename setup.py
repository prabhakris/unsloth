# Copyright 2023-present, the Unsloth team.
# Licensed under the Apache License, Version 2.0

from setuptools import setup, find_packages
import os

# Read the README for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Core dependencies required for basic functionality
INSTALL_REQUIRES = [
    "torch>=2.1.0",
    "transformers>=4.38.0",
    "datasets>=2.16.0",
    "sentencepiece>=0.1.99",
    "tqdm>=4.66.1",
    "psutil",
    "wheel>=0.42.0",
    "numpy",
    "packaging",
    "tyro",
]

# Optional dependencies for extended functionality
EXTRAS_REQUIRE = {
    "training": [
        "trl>=0.7.9",
        "peft>=0.8.0",
        "accelerate>=0.26.0",
        "bitsandbytes>=0.42.0",
        "xformers>=0.0.23",
    ],
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov",
        "black",
        "isort",
        "flake8",
        "mypy",
        "ipython",  # personal addition: useful for interactive debugging sessions
    ],
    "export": [
        "gguf",
        "protobuf",
        "huggingface_hub",
    ],
}

# Combine all optional deps under 'all' (includes dev tools for personal use)
EXTRAS_REQUIRE["all"] = [
    dep
    for group in ["training", "export", "dev"]
    for dep in EXTRAS_REQUIRE[group]
]

setup(
    name="unsloth",
    version="2024.3",
    description="2x faster, 60% less memory LLM finetuning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Unsloth AI",
    author_email="info@unsloth.ai",
    url="https://github.com/unslothai/unsloth",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    python_requires=">=3.9",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "llm",
        "fine-tuning",
        "lora",
        "qlora",
        "transformers",
        "efficient training",
        "triton",
    ],
    entry_points={
        "console_scripts": [
            "unsloth-cli=unsloth.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
