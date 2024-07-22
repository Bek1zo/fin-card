from flask import Blueprint, request
from flask.views import MethodView
from . import service as data_service
from . import schemas as person_schema
from ...common import schema as base_schema
from ...tools.flasgger_marshmallow import swagger_decorator


person_blueprint = Blueprint('Персона', __name__)
blueprint_name = person_blueprint.name


class PersonCreate(MethodView):
    """ Создание новой персоны """
    @swagger_decorator(json_schema=person_schema.PersonCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def post(self):
        """
        Создание новой персоны
        Создание новой персоны
        """
        return data_service.create_person(request.json_schema)


class PersonSearch(MethodView):
    """ Поиск кандидата по инициалам """
    @swagger_decorator(query_schema=person_schema.PersonSearchSchema, response_schema={200: person_schema.PersonListResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Поиск кандидата по инициалам.
        Поиск кандидата по инициалам.
        """
        return data_service.search_person(request.query_schema['name'], request.query_schema['status'])


class PersonSearchNoCertificate(MethodView):
    """Поиск кандидата по инициалам с отсутствующей картой ДД в последнем периоде. """
    @swagger_decorator(query_schema=person_schema.PersonSearchNoCertificateSchema, response_schema={200: person_schema.PersonListResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Поиск кандидата по инициалам с отсутствующей картой ДД в последнем периоде.
        Поиск кандидата по инициалам с отсутствующей картой ДД в последнем периоде.
        """
        return data_service.search_person_no_certificate(request.query_schema['name'], request.query_schema['period'])


class PersonListGet(MethodView):
    """ Получение списка всех персон """
    @swagger_decorator(query_schema=person_schema.PersonListGetSchema, response_schema={200: person_schema.PersonListResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self):
        """
        Получение списка всех персон.
        Получение списка всех персон.
        """
        return data_service.get_person_list(request.query_schema['status'], request.query_schema['limit'], request.query_schema['offset'])


class PersonGet(MethodView):
    """ Получение данных персоны по идентификатору """
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: person_schema.PersonResponse, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def get(self, id: str):
        """
        Получение данных персоны по идентификатору.
        Получение данных персоны по идентификатору.
        """
        return data_service.get_person(id)


class PersonUpdate(MethodView):
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, json_schema=person_schema.PersonCreateSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def put(self, id: str):
        """
        Обновление данных персоны по идентификатору
        Обновление данных персоны по идентификатору
        """
        return data_service.update_person(id, request.json_schema)


class PersonDelete(MethodView):
    @swagger_decorator(path_schema=base_schema.IdentifierSchema, response_schema={200: base_schema.ToastResponseSchema, 400: base_schema.ToastResponseSchema}, blueprint_name=blueprint_name)
    def delete(self, id):
        """
        Удаление персоны по идентификатору
        Удаление персоны по идентификатору
        """
        return data_service.delete_person(id)


person_blueprint.add_url_rule('/search', view_func=PersonSearch.as_view('api_person_search_get'))
person_blueprint.add_url_rule('/search_no_certificate', view_func=PersonSearchNoCertificate.as_view('api_person_search_no_certificate_get'))
person_blueprint.add_url_rule('/list', view_func=PersonListGet.as_view("api_person_list_get"))
person_blueprint.add_url_rule('/create', view_func=PersonCreate.as_view("api_person_create"))

person_blueprint.add_url_rule('/<string:id>', view_func=PersonGet.as_view("api_person_get"))
person_blueprint.add_url_rule('/<string:id>', view_func=PersonUpdate.as_view("api_person_update"))
person_blueprint.add_url_rule('/<string:id>', view_func=PersonDelete.as_view("api_person_delete"))