# Copyright (C) 2013 W. Trevor King <wking@tremily.us>
#
# This file is part of ipython-irc.
#
# ipython-irc is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# ipython-irc is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# ipython-irc.  If not, see <http://www.gnu.org/licenses/>.

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
