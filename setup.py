# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name         = 'powerline-hgstatus',
    description  = 'A Powerline segment for showing the status of a Mercurial working copy',
    version      = '0.1.2',
    keywords     = 'powerline hg status prompt',
    license      = 'MIT',
    author       = 'Ian Scherer',
    author_email = 'ianscherer@comcast.net',
    url          = 'https://github.com/ischer/powerline-hgstatus',
    packages     = ['powerline_hgstatus'],
    classifiers  = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
