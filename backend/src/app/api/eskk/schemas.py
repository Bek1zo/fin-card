from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema
from ...common.schema import ToastResponseSchema


class EskkSchema(Schema):
    """ Схема ответа данных по справочнику """
    id = fields.String(doc='Идентификатор классификатора', allow_none=True)
    name = fields.String(doc='Воинское звание', allow_none=True)
    value = fields.Float(doc='Сумма оклада', allow_none=False)

    class Meta:
        unknown = EXCLUDE
        strict = True


class EskkResponse(ToastResponseSchema):
    """ Схема ответов справочников """
    data = fields.Nested(EskkSchema, doc='Данные', many=True)

    class Meta:
        unknown = EXCLUDE
        strict = True


class EskkCreateSchema(Schema):
    """ Схема добавления новой классификации в справочник званий """
    name = fields.String(doc='Наименование', required=False, allow_none=True)
    value = fields.Float(doc='Значение', required=True)

    class Meta:
        unknown = EXCLUDE
        strict = True


class EskkPeriodCreateSchema(Schema):
    """ Схема добавления нового отчетного периода """
    value = fields.String(doc='Период')
    transfer = fields.Boolean(doc='Нужно ли переносить карточки ДД из предыдущего периода')


class EskkResponsePeriodSchema(Schema):
    """ Схема ответа данных по периодам """
    id = fields.String(doc='Идентификатор классификатора', allow_none=False)
    value = fields.String(doc='Наименование периода', allow_none=False)

    class Meta:
        unknown = EXCLUDE
        strict = True


class EskkResponsePeriod(Schema):
    """ Схема ответа периодоров  """
    data = fields.Nested(EskkResponsePeriodSchema, doc='Данные', many=True)
    message = fields.String(doc='Сообщение')
    code = fields.Integer(doc='HTTP Код')

    class Meta:
        unknown = EXCLUDE
        strict = True