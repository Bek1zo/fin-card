from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema
from ..eskk.schemas import EskkSchema
from ...common.schema import ToastResponseSchema, PaginatorSchema


class PersonCreateSchema(Schema):
    """ Схема создания новой персоны """
    firstname = fields.String(doc='Имя', allow_none=True)
    middlename = fields.String(doc="Отчество", allow_none=True)
    lastname = fields.String(doc='Фамилия', allow_none=True)
    birthday = fields.String(doc='Дата рождения', allow_none=True)
    personal_number = fields.String(doc='Личный номер', allow_none=True)

    tariff_category = fields.String(doc='Идентификатор тарифной категории', allow_none=True, required=False)
    job_rank = fields.String(doc='Идентификатор воинского звания', allow_none=True, required=False)

    job_position = fields.String(doc='Подразделение', allow_none=True, required=False)

    job_position_order_entry_number = fields.String(doc='Номер приказа о вступление в должность', allow_none=True)
    job_position_order_entry_date = fields.String(doc='Дата приказа о вступление в должность', allow_none=True)

    job_position_order_appointment_number = fields.String(doc='Номер приказа о назначение на должность', allow_none=True)
    job_position_order_appointment_date = fields.String(doc='Дата приказа о назначение на должность', allow_none=True)

    vus = fields.String(doc='ВУС', allow_none=True, default=None)
    unit = fields.String(doc='Подразделение', allow_none=True, default=None)
    inn = fields.String(doc='ИНН', allow_none=True, default=None)
    arrived_from = fields.String(doc='Откуда прибыл', allow_none=True, default=None)

    isActive = fields.Boolean(allow_none=True, default=True, missing=True)

    class Meta:
        """Meta."""
        strict = True
        unknown = EXCLUDE


class PersonResponseSchema(Schema):
    """ Ответ с данными по кандидату """

    fullname = fields.String(doc='ФИО + д.р. + личный номер', allow_none=True)

    id = fields.String(doc='Идентификатор персоны', allow_none=True)
    firstname = fields.String(doc='Имя', allow_none=True)
    middlename = fields.String(doc="Отчество", allow_none=True)
    lastname = fields.String(doc='Фамилия', allow_none=True)
    birthday = fields.String(doc='Дата рождения', allow_none=True)
    personal_number = fields.String(doc='Личный номер', allow_none=True)
    tariff_category = fields.String(doc='Идентификатор тарифной категории', allow_none=True)
    tariff_category_relation = fields.Nested(EskkSchema, allow_none=True)
    job_rank = fields.String(doc='Идентификатор воинского звания', allow_none=True)
    job_rank_relation = fields.Nested(EskkSchema, allow_none=True)
    job_position = fields.String(doc='Должность', allow_none=True)

    job_position_order_entry_number = fields.String(doc='Номер приказа о вступление в должность', allow_none=True)
    job_position_order_entry_date = fields.String(doc='Дата приказа о вступление в должность', allow_none=True)

    job_position_order_appointment_number = fields.String(doc='Номер приказа о назначение на должность', allow_none=True)
    job_position_order_appointment_date = fields.String(doc='Дата приказа о назначение на должность', allow_none=True)

    vus = fields.String(doc='ВУС', allow_none=True)
    unit = fields.String(doc='Подразделение', allow_none=True)
    inn = fields.String(doc='ИНН', allow_none=True)
    arrived_from = fields.String(doc='Откуда прибыл', allow_none=True)

    updated_utc = fields.String(doc='Дата обновления', allow_none=True)
    isActive = fields.Boolean(doc='Статус персоны', allow_none=False)
    status = fields.Boolean(doc='Заполнена ли карта ДД', allow_none=True)
    money_certificate_id = fields.String(doc='Идентификатор карты ДД', allow_none=True)

    class Meta:
        """Meta."""
        strict = True
        unknown = EXCLUDE


class PersonListResponse(ToastResponseSchema):
    count = fields.Integer(doc='Количество записей')
    data = fields.Nested(PersonResponseSchema, many=True, doc='Список персона', allow_none=True)

    class Meta:
        """Meta."""
        strict = False
        unknown = EXCLUDE


class PersonListGetSchema(PaginatorSchema):
    """ Запрос получения списка всех военнослужащих """
    status = fields.Boolean(doc='Статус военнослужащего (Активен/Уволен)', missing=False, default=False)


class PersonResponse(ToastResponseSchema):
    data = fields.Nested(PersonResponseSchema, allow_none=True, doc='Персона')

    class Meta:
        """Meta."""
        strict = False
        unknown = EXCLUDE


class PersonSearchSchema(Schema):
    """ Поиск персоны по ФИО """
    name = fields.String(doc='ФИО персоны')
    status = fields.Boolean(doc='Статус военнослужащего (Активен/Уволен)', allow_none=True, required=False)

    class Meta:
        """Meta."""
        strict = True


class PersonSearchNoCertificateSchema(PersonSearchSchema):
    """ Поиск персоны по ФИО """
    period = fields.String(doc='Период')

    class Meta:
        """Meta."""
        strict = True










        

