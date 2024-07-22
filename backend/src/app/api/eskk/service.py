import uuid

from sqlalchemy import desc
from ...schemas.model import RankSalary, PositionSalary, ReportingPeriod, MoneyCertificateRelation, MoneyCertificate, \
    MoneyCertificatePayment
from ...session import session_scope
from ...common.func import serialize
from ...common.toast import *


def get_eskk_rank() -> dict:
    """ Запрос получения справочника ЕСКК по воинским окладам """
    with session_scope() as session:
        result = serialize(session.query(RankSalary).order_by(RankSalary.sort).all())
        return {"data": result, 'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                 life=MessageEnum.TIME_5.value,
                                 summary='Успех!',
                                 detail='Список справочников загружен',
                                 ).get_message()]}


def create_eskk_rank(data: dict) -> dict:
    """ Запрос обавления новой классификации воинского звания """
    with session_scope() as session:
        last_rank_sort = session.query(RankSalary).order_by(desc(RankSalary.sort)).first()
        data['name'] = data['name'].lower()
        new_rank = RankSalary(**data)
        new_rank.id = uuid.uuid4()
        new_rank.sort = last_rank_sort.sort + 1
        session.add(new_rank)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Новое воинское звание "{data["value"]}" добавлено',
                                     ).get_message()]}


def update_eskk_rank(id: str, data: dict) -> dict:
    """ Запрос обновления существующей классификации воинского звания """
    with session_scope() as session:
        session.query(RankSalary).filter(RankSalary.id == id).update(data, synchronize_session=False)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Данные классификатора обновлены!',
                                     ).get_message()]}


def delete_eskk_rank(id: str) -> dict:
    """ Запрос удаления существующей классификации воинского звания """
    with session_scope() as session:
        serialize(session.query(RankSalary).filter(RankSalary.id == id).first())
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Классификатор воинского звания удален',
                                     ).get_message()]}


def create_tariff_category(data: dict) -> dict:
    """ Добавление новой классификации """
    with session_scope() as session:
        last_tariff_sort = session.query(PositionSalary).order_by(desc(PositionSalary.sort)).first()
        new_rank = PositionSalary(**data)
        new_rank.id = uuid.uuid4()
        new_rank.sort = last_tariff_sort.sort + 1
        session.add(new_rank)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Новый тарифный разряд "{data["name"]}" добавлен',
                                     ).get_message()]}


def update_tariff_category(id: str, data: dict) -> dict:
    """ Обновление существующей классификации """
    with session_scope() as session:
        session.query(PositionSalary).filter(PositionSalary.id == id).update(data, synchronize_session=False)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail='Классификация тарифного разряда обновления!',
                                     ).get_message()]}


def delete_tariff_category(id: str) -> dict:
    """ Удаление существующей классификации """
    with session_scope() as session:
        session.query(PositionSalary).filter(PositionSalary.id == id).delete()
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail='Классификация тарифного разряда удалена!',
                                     ).get_message()]}


def get_eskk_tariff_category() -> dict:
    """ Запрос получения справочника ЕСКК по тарифным разрядам """
    with session_scope() as session:
        result = serialize(session.query(PositionSalary).order_by(PositionSalary.sort).all())
        return {'data': result, 'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Справочник тарифных разрядов загружен!',
                                     ).get_message()]}


def get_eskk_period() -> dict:
    """ Запрос получения справочника ЕСКК по тарифным разрядам """
    with session_scope() as session:
        result = serialize(session.query(ReportingPeriod).order_by(ReportingPeriod.sort).all())
        return {'data': result, 'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Справочник периодов загружен!',
                                     ).get_message()]}


def create_period(period: str, transfer: bool) -> dict:
    """ Добавление новой периода """
    with session_scope() as session:
        new_period = ReportingPeriod(value=period)
        new_period.id = uuid.uuid4()

        old_period = session.query(ReportingPeriod).order_by(desc(ReportingPeriod.sort)).first()
        if old_period:
            new_period.sort = old_period.sort + 1
        else:
            new_period.sort = 0
        session.add(new_period)

        if transfer:
            old_certificates = session.query(MoneyCertificateRelation).filter(MoneyCertificateRelation.reporting_period == old_period.id).all()
            for certificate in old_certificates:
                serialized_certificate = serialize(certificate.money_certificate_relation)

                first_payment_id = uuid.uuid4()
                first_payment = MoneyCertificatePayment()
                if serialized_certificate['year_first']:
                    first_payment = MoneyCertificatePayment(**serialized_certificate['year_first_relation'])

                first_payment.id = first_payment_id
                first_payment.updated_utc = None

                session.add(first_payment)

                second_payment_id = uuid.uuid4()
                second_payment = MoneyCertificatePayment()
                if serialized_certificate['year_second']:
                    second_payment = MoneyCertificatePayment(**serialized_certificate['year_first_relation'])

                second_payment.id = second_payment_id
                second_payment.updated_utc = None

                session.add(second_payment)

                new_money_certificate = MoneyCertificate(
                    id=uuid.uuid4(),
                    year_first=first_payment_id,
                    year_second=second_payment_id,
                    certificate_number=certificate.money_certificate_relation.certificate_number,
                    certificate_date=certificate.money_certificate_relation.certificate_date,
                    certificate_expire_date=certificate.money_certificate_relation.certificate_expire_date,
                    card_author=certificate.money_certificate_relation.card_author,
                    card_inspector=certificate.money_certificate_relation.card_inspector
                )
                session.add(new_money_certificate)
                new_relation = MoneyCertificateRelation(person=certificate.person, money_certificate=new_money_certificate.id, reporting_period=new_period.id)
                session.add(new_relation)

        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                  life=MessageEnum.TIME_5.value,
                                  summary='Успех!',
                                  detail=f'Новый отчетный период "{period}" добавлен',
                                  ).get_message()]}


def update_period(id: str, data: dict) -> dict:
    """ Обновление существующей классификации """
    with session_scope() as session:
        session.query(ReportingPeriod).filter(ReportingPeriod.id == id).update(data, synchronize_session=False)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                  life=MessageEnum.TIME_5.value,
                                  summary='Успех!',
                                  detail='Отчетный период обновлен!',
                                  ).get_message()]}


def delete_period(id: str) -> dict:
    """ Удаление существующей классификации """
    with session_scope() as session:
        serialize(session.query(ReportingPeriod).filter(ReportingPeriod.id == id).first())
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                  life=MessageEnum.TIME_5.value,
                                  summary='Успех!',
                                  detail='Отчетный период удален!',
                                  ).get_message()]}