import os
import traceback

from flask import Flask, request

from app.common.toast import Message, MessageEnum


def internal_server_error(e):
    """
    :param e:
    :return:
    """
    if e.args:
        if isinstance(e.args,tuple):
            if isinstance(e.args[0], dict):
                if e.args[0].get('type') == 'warning':
                    message = Message(severity=MessageEnum.WARNING.value,
                                      life=MessageEnum.TIME_10.value,
                                      summary='Предупреждение',
                                      detail='{}'.format(e.args[0].get('message')),
                                      ).get_message()
                    return {'messages': [message]}, 203

    user = request.environ.get('REMOTE_USER', 'неизвестный пользователь')
    address = request.environ.get('REMOTE_ADDR', 'неизвестный адрес')
    path = request.environ.get('PATH_INFO', 'неизвестный путь')
    import datetime
    date_time_now = datetime.datetime.now()
    root_path = os.path.abspath(os.path.dirname(__file__))
    log_file = '{}/log.txt'.format(root_path)
    if not os.path.exists(log_file):
        with open(log_file, 'w') as fp:
            pass
    tb = str(traceback.format_exc())
    with open(log_file, "a") as fo:
        fo.write("{}\n\n{}, пользователь: {}, адрес: {} путь: {}\nошибка: {}\n"
                 .format(100*'*',date_time_now, user, address, path, tb))

    message = None

    if len(e.args) > 0:
        if 'UniqueViolation' in e.args[0]:
            message = 'Невозможно добавить новую запись. Повторяющееся значение.'
    else:
        message = e.args

    print(e)
    print(e.args)

    message = Message(severity=MessageEnum.ERROR.value,
                      life=MessageEnum.TIME_10.value,
                      summary='Ошибка',
                      detail='{}'.format(message),
                      ).get_message()
    return {'messages': [message]}, 500



def get_app(config):
    """Get flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    from flask_marshmallow import Marshmallow
    Marshmallow(app)

    from flasgger import Swagger
    Swagger(app)

    from .api import blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint.obj, url_prefix = blueprint.url_prefix)

    app.register_error_handler(Exception, internal_server_error)

    return app
