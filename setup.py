from io import open
from setuptools import setup

version = '0.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whats_api',
    version=version,

    author='neluckoff',
    author_email='neluckoff@gmail.com',

    description=(
        u'Open source module for sending messages to WhatsApp based on Selenium'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/neluckoff/whats_api/archive/main.zip',
    download_url='https://github.com/neluckoff/whats_api/archive/master.zip',

    license='MIT License, see LICENSE file',

    packages=['whats_api'],
    install_requires=['selenium', 'qrcode', 'Pillow', 'webdriver-manager'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)