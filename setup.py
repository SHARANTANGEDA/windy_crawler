import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='windy-weather-crawler',
    version='1.1',
    author='Sai Sharan Tangeda',
    author_email='saisarantangeda@gmail.com',
    description="A web crawler that takes input as place gives the weather forecast for 5 days",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SHARANTANGEDA/windy_crawler',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment :: Mozilla"
    ],
    install_requires=[
        'selenium',
        'scrapy',
        'tabulate'
    ],
    python_requires='>=3.6',
)