from marshmallow import fields, EXCLUDE
from flask_marshmallow import Schema
from ...common.schema import ToastResponseSchema


class MoneyCertificatePaymentQuerySchema(Schema):
    id = fields.String(doc='Идентификатор карточки ДД', required=True, allow_none=True)
    year = fields.String(doc='Год за который вносятся данные [first/second]', required=True)


class MoneyCertificatePaymentCreateSchema(Schema):
    id = fields.String(doc='Идентификатор', allow_none=True)
    pnvl_order_number = fields.String(doc='Номер приказа стажа службы для ПНВЛ', allow_none=True, required=False)
    pnvl_order_date = fields.String(doc='От какой даты приказ', allow_none=True, required=False)
    pnvl_date = fields.String(doc='На какую дату актуальна информация', allow_none=True, required=False)
    pnvl_experience = fields.String(doc='Стаж службы. (Прим. дни-месяц-год)', allow_none=True, required=False)
    pnvl_percentage = fields.Integer(doc='Процент надбавки за выслугу лет', allow_none=True, required=False)
    pnvl_sum = fields.Float(doc='Сумма надбавки за выслугу лет', allow_none=True, required=False)

    position_salary = fields.Float(doc='Оклад по воинской должности', allow_none=True, required=False)
    rank_salary = fields.Float(doc='Оклад по воинскому званию', allow_none=True, required=False)

    ouvs_order_number = fields.String(doc='Номер приказа надбавки за ОУВС', allow_none=True, required=False)
    ouvs_order_date = fields.String(doc='Дата приказа надбавки за ОУВС', allow_none=True, required=False)
    ouvs_percentage = fields.Integer(doc='Процент надбавки за ОУВС', allow_none=True, required=False)
    ouvs_sum = fields.Float(doc='Сумма надбавки за ОУВС', allow_none=True, required=False)

    admission_form_order_number = fields.String(doc='Номер приказа надбавки за секретность', allow_none=True, required=False)
    admission_form_order_date = fields.String(doc='Дата приказа надбавки за секретность', allow_none=True, required=False)
    admission_form_percentage = fields.Integer(doc='Процент надбавки за секретность', allow_none=True, required=False)
    admission_form_sum = fields.Float(doc='Сумма надбавки за секретность', allow_none=True, required=False)

    award_order_number = fields.String(doc='Номер приказа на премию', allow_none=True, required=False)
    award_order_date = fields.String(doc='Дата приказа на премию', allow_none=True, required=False)
    award_percentage = fields.Integer(doc='Процент надбавки', allow_none=True, required=False)
    award_sum = fields.Float(doc='Сумма надбавки', allow_none=True, required=False)

    qualification_order_number = fields.String(doc='Номер приказа надбавки за кл. квалификацию', allow_none=True, required=False)
    qualification_order_date = fields.String(doc='Дата приказа надбавки за кл. квалификацию', allow_none=True, required=False)
    qualification_percentage = fields.Integer(doc='Процент надбавки за кл. квалификацию', allow_none=True, required=False)
    qualification_sum = fields.Float(doc='Сумма надбавки за кл. квалификацию', allow_none=True, required=False)

    total_salary = fields.Float(doc='Всего начислено', allow_none=True, required=False)
    total_salary_date = fields.String(doc='С какого числа начислено', allow_none=True, required=False)

    payment_status = fields.Boolean(doc='Заполнена ли выплата полностью', allow_none=True, required=False)

    premiumList = fields.List(fields.Dict())

    class Meta:
        unknown = EXCLUDE
        strict = True


class MoneyCertificatePaymentSchema(MoneyCertificatePaymentCreateSchema):
    id = fields.String(doc='Идентификатор выплаты')

    pnvl_order_number = fields.String(allow_none=True)
    pnvl_order_date = fields.String(allow_none=True)
    pnvl_date = fields.String(allow_none=True)
    pnvl_experience = fields.String(allow_none=True)
    pnvl_percentage = fields.Float(allow_none=True)
    pnvl_sum = fields.Float(allow_none=True)

    position_salary = fields.Float(allow_none=True)
    rank_salary = fields.Float(allow_none=True)
    ouvs_order_number = fields.String(allow_none=True)
    ouvs_order_date = fields.String(allow_none=True)
    ouvs_percentage = fields.Float(allow_none=True)
    ouvs_sum = fields.Float(allow_none=True)
    ouvs_is_active = fields.Boolean(allow_none=True)

    admission_form_order_number = fields.String(allow_none=True)
    admission_form_order_date = fields.String(allow_none=True)
    admission_form_order_percentage = fields.Float(allow_none=True)
    admission_form_order_sum = fields.Float(allow_none=True)
    admission_form_is_active = fields.Boolean(allow_none=True)

    award_order_number = fields.String(allow_none=True)
    award_order_date = fields.String(allow_none=True)
    award_percentage = fields.Float(allow_none=True)
    award_sum = fields.Float(allow_none=True)
    award_is_active = fields.Boolean(allow_none=True)

    qualification_order_number = fields.String(allow_none=True)
    qualification_order_date = fields.String(allow_none=True)
    qualification_percentage = fields.Float(allow_none=True)
    qualification_sum = fields.Float(allow_none=True)
    qualification_is_active = fields.Boolean(allow_none=True)

    primary_premium_order_name = fields.String(allow_none=True)
    primary_premium_order_number = fields.String(allow_none=True)
    primary_premium_order_date = fields.String(allow_none=True)
    primary_premium_percentage = fields.Float(allow_none=True)
    primary_premium_sum = fields.Float(allow_none=True)
    primary_premium_is_active = fields.Boolean(allow_none=True)

    secondary_premium_order_name = fields.String(allow_none=True)
    secondary_premium_order_number = fields.String(allow_none=True)
    secondary_premium_order_date = fields.String(allow_none=True)
    secondary_premium_percentage = fields.Float(allow_none=True)
    secondary_premium_sum = fields.Float(allow_none=True)
    secondary_premium_is_active = fields.Boolean(allow_none=True)

    total_salary = fields.Float(allow_none=True)
    total_salary_date = fields.String(allow_none=True)

    class Meta:
        unknown = EXCLUDE


class MoneyCertificatePaymentResponse(ToastResponseSchema):
    data = fields.Nested(MoneyCertificatePaymentSchema, doc='Данные', many=False, allow_none=True)

    class Meta:
        unknown = EXCLUDE
        strict = True