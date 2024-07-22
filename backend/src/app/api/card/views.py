from flask import Blueprint, request, send_file
from flask.views import MethodView
from . import service as data_service
from . import service_template as template_service
from . import schemas as eskk_schema
from ...common import schema as base_schema
from ...tools.flasgger_marshmallow import swagger_decorator


card_blueprint = Blueprint('Карта денежного довольствия', __name__)
blueprint_name = card_blueprint.name


class MoneyCertificateRelationGet(MethodView):
    """ Получение полной информации по военнослужащему и всех его карт ДД """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: eskk_schema.MoneyCertificateRelationResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self, id):
        """
        Получение карточки денежного довольствия
        Получение карточки денежного довольствия
        """
        return data_service.get_money_certificate_relation(id)


class MoneyCertificateRelationSearch(MethodView):
    """ Поиск полной информации по военнослужащему по ФИО """
    @swagger_decorator(query_schema=eskk_schema.MoneyCertificateSearchQuerySchema, response_schema={200: eskk_schema.MoneyCertificateListResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Получение карточки денежного довольствия
        Получение карточки денежного довольствия
        """
        return data_service.search_money_certificate_relation(request.query_schema['name'], request.query_schema['period'])


class MoneyCertificateGet(MethodView):
    """ Получение карточки денежного довольствия """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: eskk_schema.MoneyCertificateResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self, id):
        """
        Получение карточки денежного довольствия
        Получение карточки денежного довольствия
        """
        return data_service.get_money_certificate(id)


class MoneyCertificateGetLast(MethodView):
    """ Получение последний карточки ДД при ее наличие """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: eskk_schema.OnlyMoneyCertificateResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self, id):
        """
        Получение последний карточки ДД при ее наличие
        Получение последний карточки ДД при ее наличие
        """
        return data_service.get_money_certificate_last(id)


class MoneyCertificateGetList(MethodView):
    """ Получение списка карточек денежного довольствия """
    @swagger_decorator(query_schema=eskk_schema.MoneyCertificateListQuerySchema, response_schema={200: eskk_schema.MoneyCertificateListResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Получение карточки денежного довольствия
        Получение карточки денежного довольствия
        """
        return data_service.get_money_certificate_list(request.query_schema['period'], request.query_schema['limit'], request.query_schema['offset'])


class MoneyCertificateCreate(MethodView):
    """ Создание новой карточки ДД """
    @swagger_decorator(query_schema=eskk_schema.MoneyCertificateQuerySchema, json_schema=eskk_schema.MoneyCertificateCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def post(self):
        """
        Создание новой карточки ДД
        Создание новой карточки ДД
        """
        return data_service.create_money_certificate(request.query_schema['person'], request.query_schema['period'], request.json_schema)


class MoneyCertificateUpdate(MethodView):
    """ Обновление данных карточки ДД """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, json_schema=eskk_schema.MoneyCertificateCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def put(self, id):
        """
        Обновление данных карточки ДД
        Обновление данных карточки ДД
        """
        return data_service.update_money_certificate(id, request.json_schema)


card_blueprint.add_url_rule('/relation/<string:id>', view_func=MoneyCertificateRelationGet.as_view("api_certificate_relation_get"))
card_blueprint.add_url_rule('/relation/search', view_func=MoneyCertificateRelationSearch.as_view("api_certificate_relation_search"))
card_blueprint.add_url_rule('/<string:id>', view_func=MoneyCertificateGet.as_view("api_certificate_get"))
card_blueprint.add_url_rule('/last/<string:id>', view_func=MoneyCertificateGetLast.as_view("api_certificate_last_get"))
card_blueprint.add_url_rule('/list/', view_func=MoneyCertificateGetList.as_view("api_certificate_list_get"))
card_blueprint.add_url_rule('/update/<string:id>', view_func=MoneyCertificateUpdate.as_view("api_certificate_update"))
card_blueprint.add_url_rule('/create', view_func=MoneyCertificateCreate.as_view("api_certificate_create"))


# Темплейты

class MoneyCertificateFileGet(MethodView):
    """ Получение файла карточки денежного довольствия """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self, id):
        """
        Получение файла карточки денежного довольствия
        Получение файла карточки денежного довольствия
        """

        return send_file(template_service.get_money_certificate_file(id))


card_blueprint.add_url_rule('/file/<string:id>', view_func=MoneyCertificateFileGet.as_view("api_certificate_file_get"))