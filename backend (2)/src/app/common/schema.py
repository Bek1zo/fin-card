"""Schemas."""
from marshmallow import fields
from flask_marshmallow import Schema


class IdentifierSchema(Schema):
    id = fields.String(doc='Идентификатор')

    class Meta:
        """Meta."""
        strict = True


class PaginatorSchema(Schema):
    """ Запрос получения списка всех военнослужащих """
    limit = fields.Integer(doc='Кол-во записей')
    offset = fields.Integer(doc='Смещение')

    class Meta:
        """Meta."""
        strict = True


class ToastSchema(Schema):
    """ Ответ тостом на запрос """
    severity = fields.String(doc='Статус')
    summary = fields.String(doc='Наименование')
    detail = fields.String(doc='Описание')
    life = fields.Integer(doc='Длительность отображения')

    class Meta:
        """Meta."""
        strict = True


class ToastResponseSchema(Schema):
    messages = fields.List(fields.Nested(ToastSchema))
    data = fields.Dict()

    class Meta:
        """Meta."""
        strict = True
