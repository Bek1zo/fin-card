from flask import Blueprint, request
from flask.views import MethodView
from . import service as data_service
from . import schemas as eskk_schema
from ...common import schema as base_schema
from ...tools.flasgger_marshmallow import swagger_decorator

card_payment_blueprint = Blueprint('Выплаты по картам денежного довольствия', __name__)
blueprint_name = card_payment_blueprint.name


class MoneyCertificatePaymentCreate(MethodView):
    """ Создание выплаты для карточки денежного довольствия """
    @swagger_decorator(query_schema=eskk_schema.MoneyCertificatePaymentQuerySchema,
                       json_schema=eskk_schema.MoneyCertificatePaymentCreateSchema,
                       response_schema={200: base_schema.ToastResponseSchema,
                                        400: base_schema.ToastResponseSchema},
                       blueprint_name=blueprint_name)
    def post(self):
        """
        Создание выплаты для карточки денежного довольствия
        Создание выплаты для карточки денежного довольствия
        """
        query = request.query_schema
        years = ['first', 'second']
        if query['year'] not in years:
            pass
        return data_service.create_money_certificate_payment(query['id'], query['year'], request.json_schema)


class MoneyCertificatePaymentUpdate(MethodView):
    """ Обновление выплаты карточки денежного довольствия """
    @swagger_decorator(query_schema=eskk_schema.MoneyCertificatePaymentQuerySchema,
                       json_schema=eskk_schema.MoneyCertificatePaymentCreateSchema,
                       response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema},
                       blueprint_name=blueprint_name)
    def put(self):
        """
        Обновление выплаты карточки денежного довольствия
        Обновление выплаты карточки денежного довольствия
        """
        query = request.query_schema
        years = ['first', 'second']
        if query['year'] not in years:
            pass
        return data_service.update_money_certificate_payment(query['id'], request.json_schema, query['year'])


class MoneyCertificatePaymentGet(MethodView):
    """ Получение выплаты карточки денежного довольствия """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema,
                       response_schema={200: eskk_schema.MoneyCertificatePaymentResponse, 400: base_schema.ToastResponseSchema},
                       blueprint_name=blueprint_name)
    def get(self, id):
        """
        Получение выплаты карточки денежного довольствия
        Получение выплаты карточки денежного довольствия
        """
        return data_service.get_money_certificate_payment(id)


card_payment_blueprint.add_url_rule('/<string:id>', view_func=MoneyCertificatePaymentGet.as_view('api_money_certificate_payment_get'))
card_payment_blueprint.add_url_rule('/', view_func=MoneyCertificatePaymentUpdate.as_view('api_money_certificate_payment_update'))
card_payment_blueprint.add_url_rule('/', view_func=MoneyCertificatePaymentCreate.as_view('api_money_certificate_payment_create'))