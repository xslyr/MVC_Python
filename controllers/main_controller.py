
from controllers import app_types as t
from views import ViewFactory
from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Main_Controller(metaclass=SingletonMeta):

    def __init__(self, appname:str='App test', **kwargs):
        self.name = appname
        self._config = {
            'debug': kwargs.get('debug', True),
            'database': '',
        }

    @property
    def config(self):
        return self._config

    def main(self) -> t.TControllerResponse:

        response = t.TControllerResponse(
            view='main',
            args = {'test': 'Informação gerada pelo main controller'}
        )

        return ViewFactory.send_view( response )
