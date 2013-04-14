# Copyright

"An IRC iframe using webchat.freenode.net"

from distutils.core import setup

from ipythonirc import __version__


name = 'ipython-irc'
package = 'ipythonirc'

setup(
    name=name,
    version=__version__,
    maintainer='W. Trevor King',
    maintainer_email='wking@tremily.us',
    url='http://github.com/wking/{}/'.format(name),
    download_url='https://github.com/wking/{}/archive/v{}.tar.gz'.format(
        name, __version__),
    license='GNU General Public License v3 or later (GPLv3+)',
    platforms=['all'],
    description=__doc__,
    long_description=open('README', 'r').read(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python',
        'Topic :: Education',
        ],
    packages=[package],
    provides=['{} ({})'.format(package, __version__)],
    requires=['ipython'],
    )
