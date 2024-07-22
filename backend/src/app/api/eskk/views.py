from flask import Blueprint, request
from flask.views import MethodView
from . import service as data_service
from . import schemas as eskk_schema
from ...common import schema as base_schema
from ...tools.flasgger_marshmallow import swagger_decorator


eskk_blueprint = Blueprint('ЕСКК', __name__)
blueprint_name = eskk_blueprint.name


class EskkRankGet(MethodView):
    """ Справочник ЕСКК окладов по воинским званиям """
    @swagger_decorator(response_schema={200: eskk_schema.EskkResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Получение справочника по воинским званиям
        Получение справочника по воинским званиям
        """
        return data_service.get_eskk_rank()


class EskkRankCreate(MethodView):
    @swagger_decorator(json_schema=eskk_schema.EskkCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def post(self):
        """
        Добавление новой классификации в справочник по воинским званиям
        Добавление новой классификации в справочник по воинским званиям
        """
        return data_service.create_eskk_rank(request.json_schema)


class EskkRankUpdate(MethodView):
    """ Обновление справочника по тарифным категориям """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, json_schema=eskk_schema.EskkCreateSchema, response_schema={200: eskk_schema.EskkResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def put(self, id: str):
        """
        Обновление данных справочника по тарифным категориям
        Обновление данных справочника по тарифным категориям
        """
        return data_service.update_eskk_rank(id, request.json_schema)


class EskkRankDelete(MethodView):
    """ Удаление справочника по тарифным категориям """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: eskk_schema.EskkResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def delete(self, id: str):
        """
        Удаление данных справочника по тарифным категориям
        Удаление данных справочника по тарифным категориям
        """
        return data_service.delete_eskk_rank(id)


class EskkTariffCategoryGet(MethodView):
    """ Получение справочников """
    @swagger_decorator(response_schema={200: eskk_schema.EskkResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Получение справочника окладов по тарифным категориям
        Получение справочника окладов по тарифным категориям
        """
        return data_service.get_eskk_tariff_category()


class EskkTariffCategoryCreate(MethodView):
    @swagger_decorator(json_schema=eskk_schema.EskkCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def post(self):
        """
        Добавление новой классификации в справочник по тарифным категориям
        Добавление новой классификации в справочник по тарифным категориям
        """
        return data_service.create_tariff_category(request.json_schema)


class EskkTariffCategoryUpdate(MethodView):
    """ Обновление справочника по тарифным категориям """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, json_schema=eskk_schema.EskkCreateSchema, response_schema={200: eskk_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def put(self, id: str):
        """
        Обновление данных справочника по тарифным категориям
        Обновление данных справочника по тарифным категориям
        """
        return data_service.update_tariff_category(id, request.json_schema)


class EskkTariffCategoryDelete(MethodView):
    """ Удаление справочника по тарифным категориям """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: eskk_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def delete(self, id: str):
        """
        Удаление данных справочника по тарифным категориям
        Удаление данных справочника по тарифным категориям
        """
        return data_service.delete_tariff_category(id)


eskk_blueprint.add_url_rule('/rank', view_func=EskkRankGet.as_view("api_eskk_rank_get"))
eskk_blueprint.add_url_rule('/rank', view_func=EskkRankCreate.as_view("api_eskk_rank_create"))
eskk_blueprint.add_url_rule('/rank/<string:id>', view_func=EskkRankUpdate.as_view("api_eskk_rank_update"))
eskk_blueprint.add_url_rule('/rank/<string:id>', view_func=EskkRankDelete.as_view("api_eskk_rank_delete"))

eskk_blueprint.add_url_rule('/tariff_category', view_func=EskkTariffCategoryGet.as_view("api_eskk_tariff_category_get"))
eskk_blueprint.add_url_rule('/tariff_category', view_func=EskkTariffCategoryCreate.as_view("api_eskk_tariff_category_create"))
eskk_blueprint.add_url_rule('/tariff_category/<string:id>', view_func=EskkTariffCategoryUpdate.as_view("api_eskk_tariff_category_update"))
eskk_blueprint.add_url_rule('/tariff_category/<string:id>', view_func=EskkTariffCategoryDelete.as_view("api_eskk_tariff_category_delete"))


class EskkPeriodGet(MethodView):
    """ Получение всех периодов """
    @swagger_decorator(response_schema={200: eskk_schema.EskkResponsePeriod, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Получение всех периодов
        Получение всех периодов
        """
        return data_service.get_eskk_period()


class EskkPeriodCreate(MethodView):
    """ Создание нового периода """
    @swagger_decorator(json_schema=eskk_schema.EskkPeriodCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def post(self):
        """
        Создание нового периода
        Создание нового периода
        """
        return data_service.create_period(request.json_schema['value'], request.json_schema['transfer'])


class EskkPeriodUpdate(MethodView):
    """ Обновление данных по периоду """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, json_schema=eskk_schema.EskkCreateSchema, response_schema={200: eskk_schema.EskkResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def put(self, id: str):
        """
        Обновление данных по периоду
        Обновление данных по периоду
        """
        return data_service.update_period(id, request.json_schema)


class EskkPeriodDelete(MethodView):
    """ Удаление периода """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: eskk_schema.EskkResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def delete(self, id: str):
        """
        Удаление периода
        Удаление периода
        """
        return data_service.delete_period(id)


eskk_blueprint.add_url_rule('/period', view_func=EskkPeriodGet.as_view("api_period_get"))
eskk_blueprint.add_url_rule('/period', view_func=EskkPeriodCreate.as_view("api_period_create"))
eskk_blueprint.add_url_rule('/period/<string:id>', view_func=EskkPeriodUpdate.as_view("api_period_update"))
eskk_blueprint.add_url_rule('/period/<string:id>', view_func=EskkPeriodDelete.as_view("api_period_delete"))