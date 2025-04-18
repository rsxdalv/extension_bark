import setuptools

setuptools.setup(
    name="extension_bark",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="Bark: A text-to-speech model",
    url="https://github.com/rsxdalv/extension_bark",
    project_urls={},
    scripts=[],
    install_requires=[
        "suno-bark @ https://github.com/rsxdalv/bark/releases/download/v0.1.0/suno_bark-0.1.0-py3-none-any.whl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
