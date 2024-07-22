from enum import Enum

MESSAGE = {'severity': 'success', 'summary': 'Успешно', 'detail': 'Запрос выполнен', 'life': 10000}


class Message:
    """
    Класс создания сообщения
    """

    def __init__(self, severity, summary, detail, life, message=None):
        if message is None:
            self.message = MESSAGE
        self.severity = severity
        self.summary = summary
        self.detail = detail
        self.life = life

    def get_message(self):
        """

        """
        self.message['severity'] = self.severity
        self.message['summary'] = self.summary
        self.message['detail'] = self.detail
        self.message['life'] = self.life
        return self.message


class PathEnum(Enum):
    """
    Пути.
    """
    API = '/api/'
    CARD = 'card'
    CARD_PAYMENT = 'card_payment'
    ESKK = 'eskk'
    PERSON = 'person'


class MessageEnum(Enum):
    """
    Цвета сообщений
    """
    SUCCESS = 'success'
    WARNING = 'warn'
    ERROR = 'error'
    INFO = 'info'
    TIME_5 = 5000
    TIME_10 = 10000
