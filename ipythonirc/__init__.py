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

"""An IRC iframe using webchat.freenode.net
"""

try:  # Python 3.x
    import urllib.parse as _urllib_parse
except ImportError:  # Python 2.x
    import urllib as _urllib_parse  # for urlencode

import IPython.display as _IPython_display


__version__ = '0.3'

__all__ = ['IRC']


class IRC (object):
    """An IRC iframe using webchat clients

    Currently only supports freenode (via webchat.freenode.net).

    Use with::

      IRC(nick='you', channels=('#ipython', ...)).show()

    You can give the server explicitly::

      IRC(server='http://webchat.freenode.net/', ...)

    or use some common nicknames::

      IRC(server='freenode', ...)
      IRC(server='efnet', ...)
    """
    base_urls = {  # convenient nicknames for common networks
        'freenode': 'http://webchat.freenode.net/',
        'efnet': 'http://chat.efnet.org:9090/',
        }

    def __init__(self, server='http://webchat.freenode.net/', nick=None,
                 channels=('#ipython','#rogue'), width=647, height=400):
        self.server = server
        self.nick = nick
        self.channels = channels
        self.width = width
        self.height = height

    def _get_server(self):
        server = self.server
        if not server.startswith('http://'):
            base = self.base_urls.get(server, None)
            if not base:
                raise NotImplementedError(
                    '{!r} not supported.  We *do* support {}'.format(
                        self.server, self.base_urls))
        return server

    def _get_data(self):
        data = {}
        for attr in ['nick', 'channels']:
            value = getattr(self, attr)
            if value:
                if attr in ['channels']:
                    value = ','.join(chan.lstrip('#') for chan in value)
                data[attr] = value
            else:
                data['prompt'] = 1
        return data

    def _get_url(self):
        return '{}?{}'.format(
            self._get_server(),
            _urllib_parse.urlencode(self._get_data()))

    def _html(self):
        url = self._get_url()
        return '<iframe src="{}" width="{}" height="{}"></iframe>'.format(
            url, self.width, self.height)

    def show(self):
        _IPython_display.display(_IPython_display.HTML(self._html()))
