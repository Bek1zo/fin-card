import uuid
from sqlalchemy import and_, or_, desc
from ...schemas.model import Person, MoneyCertificateRelation, ReportingPeriod, MoneyCertificate
from ...session import session_scope
from ...common.func import serialize
from ...common.toast import *


def create_person(data: dict) -> dict:
    """ Запрос создания новой персоны """
    with session_scope() as session:
        data['id'] = str(uuid.uuid4())
        session.add(Person(**data))
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail='Военнослужащий добавлен',
                                     ).get_message()]}


def get_person(id: str) -> dict:
    """ Запрос получения персоны по идентификатору """
    with session_scope() as session:
        result = serialize(session.query(Person).filter(Person.id == id).first())
        return {'data': result,
                'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail='Военнослужащий добавлен',
                                     ).get_message()]}


def search_person(name: str, status) -> dict:
    with session_scope() as session:
        result = serialize(session.query(Person).filter(Person.isActive == status).filter(and_(*[or_(Person.lastname.ilike(f"%{i}%"), Person.firstname.ilike(f"%{i}%"), Person.middlename.ilike(f"%{i}%")) for i in name.split(' ')])).limit(10).all())
        for person in result:
            cert = person['money_certificate_relation'][-1].money_certificate_relation if len(person['money_certificate_relation']) > 0 else MoneyCertificate()
            last_period = session.query(ReportingPeriod).order_by(desc(ReportingPeriod.sort)).first()
            person_period = session.query(MoneyCertificateRelation).filter(MoneyCertificateRelation.person == person['id']).order_by(desc(MoneyCertificateRelation.created_utc)).first()
            person_period = person_period.reporting_period if hasattr(person_period, 'reporting_period') else None
            person['money_certificate_id'] = cert.id
            person['status'] = False
            if person_period != last_period.id:
                person['status'] = False
                person['money_certificate_id'] = None
            else:
                if cert.card_author is None or cert.card_inspector is None or cert.certificate_number is None or cert.certificate_date is None or cert.certificate_expire_date is None:
                    person['status'] = None
                else:
                    person['status'] = True

        return {'data': result,
                'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                      life=MessageEnum.TIME_5.value,
                                      summary='Успех!',
                                      detail='Поиск осуществлен',
                                      ).get_message()]}


def search_person_no_certificate(name: str, period: str) -> dict:
    with session_scope() as session:
        period = session.query(ReportingPeriod).filter(ReportingPeriod.value == period).first()

        query = session.query(Person.id, Person.lastname, Person.firstname, Person.middlename, Person.birthday, Person.personal_number).filter(and_(*[or_(Person.lastname.ilike(f"%{i}%"), Person.firstname.ilike(f"%{i}%"), Person.middlename.ilike(f"%{i}%")) for i in name.split(' ')])).all()
        query_result = []

        for index, person in enumerate(query):
            certificate = session.query(MoneyCertificateRelation).filter(MoneyCertificateRelation.person == person.id).filter(MoneyCertificateRelation.reporting_period == period.id).first()
            if certificate is None:
                query_result.append(person)

        result = []

        for person in query_result:
            person_object = {}
            for value in range(0, len(person)):
                if value == 0:
                    # Если индекс 0 (Всегда ИД пользователя)
                    person_object['id'] = person[value]
                    person_object['fullname'] = ''
                else:
                    if person[value] is None:
                        pass
                    else:
                        if value == 4:
                            # Если индекс 4 (Всегда дата рождения)
                            person_object['fullname'] += str(person[value]) + ' г.р. '
                        elif value == 5:
                            # Если индекс 5 (Всегда персональный номер)
                            person_object['fullname'] += 'л/н ' + str(person[value])
                        else:
                            person_object['fullname'] += str(person[value]) + ' '
                if value == len(person) - 1:
                    result.append(person_object)
        return {'data': result,
                'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                      life=MessageEnum.TIME_5.value,
                                      summary='Успех!',
                                      detail='Поиск осуществлен',
                                      ).get_message()]}


def get_person_list(status: bool, page_limit, page_offset) -> dict:
    """ Запрос получения списка всех персон """
    with session_scope() as session:
        query = session.query(Person).join(Person.money_certificate_relation).filter(Person.isActive == status)
        count = query.count()
        result = serialize(query.limit(page_limit).offset((page_offset - 1) * page_limit).all())

        last_period = session.query(ReportingPeriod).order_by(desc(ReportingPeriod.sort)).first()

        for person in result:
            cert = person['money_certificate_relation'][-1].money_certificate_relation
            person['money_certificate_id'] = cert.id
            person['status'] = False

            if person['money_certificate_relation'][-1].report_period_relation.id != last_period.id:
                person['status'] = False
                person['money_certificate_id'] = None
            else:
                if cert.card_author is None or cert.card_inspector is None or cert.certificate_number is None or cert.certificate_date is None or cert.certificate_expire_date is None or cert.card_author == '' or cert.card_inspector == '' or cert.certificate_number == '' or cert.certificate_date == '' or cert.certificate_expire_date == '':
                    person['status'] = None
                else:
                    person['status'] = True
        return {'data': result,
                'count': count,
                'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail='Список персон загружен.',
                                     ).get_message()]}


def delete_person(id: str) -> dict:
    """ Запрос удаления персоны """
    with session_scope() as session:
        person = serialize(session.query(Person).filter(Person.id == id).first())
        if person:
            session.query(Person).filter(Person.id == id).delete()
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                 life=MessageEnum.TIME_5.value,
                                 summary='Успех!' if person else 'Ошибка!',
                                 detail='Военнослужащий отмечен для удаления.' if person else 'Военнослужащий не найден!',
                                 ).get_message()]}


def update_person(id: str, data: dict) -> dict:
    """ Запрос обновления данных персоны """
    with session_scope() as session:
        query = session.query(Person).filter(Person.id == id)
        query.update(data, synchronize_session=False)
        result = serialize(query.first())
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Информация о военной службе "{result["lastname"]} {result["firstname"]} {result["middlename"]}" обновлена',
                                     ).get_message()]}
