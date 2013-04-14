# Copyright

"""An IRC iframe using webchat.freenode.net
"""

import urllib.parse as _urllib_parse

import IPython.display as _IPython_display


__version__ = '0.1'

__all__ = ['IRC']


class IRC (object):
    """An IRC iframe using webchat clients

    Currently only supports freenode (via webchat.freenode.net).

    Use with::

      IRC(nick='you', channels=('#ipython', ...)).show()
    """
    def __init__(self, server='chat.freenode.net', nick=None,
                 channels=('#ipython','#rogue'), width=647, height=400):
        self.server = server
        self.nick = nick
        self.channels = channels
        self.width = width
        self.height = height
        if self.server not in [
                'chat.freenode.net',
                ]:
            raise NotImplementedError(self.server)

    def _html(self):
        data = {}
        for attr in ['nick', 'channels']:
            value = getattr(self, attr)
            if value:
                if attr in ['channels']:
                    value = ','.join(chan.lstrip('#') for chan in value)
                data[attr] = value
            else:
                data['prompt'] = 1
        url = '{}?{}'.format(
            'http://webchat.freenode.net',
            _urllib_parse.urlencode(data)
            )
        return '<iframe src="{}" width="{}" height="{}"></iframe>'.format(
            url, self.width, self.height)

    def show(self):
        _IPython_display.display(_IPython_display.HTML(self._html()))
