from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema

from ..card_payment.schemas import MoneyCertificatePaymentSchema
from ..eskk.schemas import EskkResponsePeriodSchema
from ..person.schemas import PersonResponseSchema
from ...common.schema import ToastResponseSchema, PaginatorSchema


class MoneyCertificateSearchQuerySchema(Schema):
    name = fields.String(doc='ФИО')
    period = fields.String(doc='Период')


class MoneyCertificateListQuerySchema(PaginatorSchema):
    """ Схема query запроса получения списка карточек денежного довольствия """
    period = fields.String(doc='Период')


class MoneyCertificateQuerySchema(Schema):
    """ Схема path запроса создания новой карточки ДД  """
    person = fields.String(doc='Идентификатор персоны за которым необходимо закрепить карточку', required=True)
    period = fields.String(doc='Идентификатор периода, за которым закрепляется карточка', required=True, allow_none=True)


class MoneyCertificateCreateSchema(Schema):
    """ Схема создания новой карточки ДД """

    certificate_number = fields.String(doc='Номер карточки', allow_none=False, required=True)
    certificate_date = fields.String(doc='От какого числа карточка', allow_none=True, required=False)
    certificate_expire_date = fields.String(doc='Дата истечения срока карточки', allow_none=True, required=False)

    year_first = fields.String(doc='Данный за первый год', allow_none=True, missing=None, required=False)
    year_second = fields.String(doc='Данные за второй год', allow_none=True, missing=None, required=False)

    card_author = fields.String(doc='Составитель карточки', required=False, allow_none=True)
    card_inspector = fields.String(doc='Проверяющий карточки', required=False, allow_none=True)

    class Meta:
        unknown = EXCLUDE


class OnlyMoneyCertificateResponse(Schema):
    """ Схема ответа карты ДД """
    id = fields.String(doc='Идентификатор карточки денежного довольствия', allow_none=False)
    certificate_number = fields.String(doc='Номер карточки ДД', allow_none=True)
    certificate_date = fields.String(doc='Дата заведения карточки', allow_none=True)
    certificate_expire_date = fields.String(doc='До какого действительна карточка', allow_none=True)
    card_author = fields.String(doc='Составитель карточки', allow_none=True)
    card_inspector = fields.String(doc='Проверяющий карточки', allow_none=True)

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificateResponse(OnlyMoneyCertificateResponse):
    """ Схема ответа карты ДД со связими на выплаты """
    year_first = fields.String(doc='Идентификатор выплат первого года', allow_none=True)
    year_second = fields.String(doc='Идентификатор выплат второго года', allow_none=True)
    year_first_relation = fields.Nested(MoneyCertificatePaymentSchema, allow_none=True)
    year_second_relation = fields.Nested(MoneyCertificatePaymentSchema, allow_none=True)

    class Meta:
        unknown = EXCLUDE
        strict = True


class OnlyMoneyCertificateResponseSchema(ToastResponseSchema):
    data = fields.Nested(OnlyMoneyCertificateResponse, many=False)

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificateListResponseSchema(Schema):
    """ Схема ответа данных по справочнику """
    id = fields.String(doc='Идентификатор карточки денежного довольствия', allow_none=False)
    firstname = fields.String(doc='Имя', allow_none=True)
    middlename = fields.String(doc='Отчество', allow_none=True)
    lastname = fields.String(doc='Фамилия', allow_none=True)
    job_rank = fields.String(doc='Воинское звание', allow_none=True)
    certificate_number = fields.String(doc='Номер карточки ДД', allow_none=False)
    certificate_date = fields.String(doc='Дата заведения карточки', allow_none=True)
    certificate_expire_date = fields.String(doc='До какого действительна карточка', allow_none=True)
    year_first = fields.String(doc='Идентификатор выплат первого года', allow_none=True)
    year_second = fields.String(doc='Идентификатор выплат второго года', allow_none=True)
    card_author = fields.String(doc='Составитель карточки', allow_none=True)
    card_inspector = fields.String(doc='Проверяющий карточки', allow_none=True)
    year_first_status = fields.Boolean(doc='Статус первого года', allow_none=True)
    year_second_status = fields.Boolean(doc='Статус второго года', allow_none=True)
    money_certificate_id = fields.String(doc='Идентификатор карты ДД', allow_none=True)

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificateResponseSchema(ToastResponseSchema):
    data = fields.Nested(MoneyCertificateResponse, many=False)

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificateListResponse(ToastResponseSchema):
    """ Схема ответов справочников """
    data = fields.Nested(MoneyCertificateListResponseSchema, doc='Данные', many=True, allow_none=True)

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificateRelationResponseSchema(Schema):
    money_certificate_relation = fields.Nested(MoneyCertificateResponseSchema, many=False)
    person_relation = fields.Nested(PersonResponseSchema, many=False)
    report_period_relation = fields.Nested(EskkResponsePeriodSchema, many=False)

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificateRelationResponse(ToastResponseSchema):
    """ Схема ответа всех данных по военнослужащему """
    data = fields.Nested(MoneyCertificateRelationResponseSchema, allow_none=True, doc='Данные')

    class Meta:
        unknown = EXCLUDE
        strict = True
