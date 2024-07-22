import uuid
import datetime

from ...common.toast import Message, MessageEnum
from ...schemas.model import MoneyCertificatePayment, MoneyCertificate
from ...session import session_scope
from ...common.func import serialize


def update_money_certificate_payment(id: str, data: dict, year: str) -> dict:
    """ Запрос обновления данных выплаты """
    with session_scope() as session:
        data = make_premium_list(data)
        if year == 'first':
            if data['id']:
                session.query(MoneyCertificatePayment).filter(MoneyCertificatePayment.id == data['id']).update(data)
            else:
                certificate_create(id, data, year)
        elif year == 'second':
            if data['id']:
                session.query(MoneyCertificatePayment).filter(MoneyCertificatePayment.id == data['id']).update(data)
            else:
                certificate_create(id, data, year)


def certificate_create(id, data, year):
    with session_scope() as session:
        payment_id = str(uuid.uuid4())
        money_certificate_payment = MoneyCertificatePayment(**data)
        money_certificate_payment.id = payment_id
        money_certificate_payment.updated_utc = datetime.datetime.utcnow()
        session.add(money_certificate_payment)
        session.query(MoneyCertificate).filter(MoneyCertificate.id == id).update(
            {'year_first': payment_id}) if year == 'first' else session.query(MoneyCertificate).filter(
            MoneyCertificate.id == id).update({'year_second': payment_id})


def make_premium_list(data):
    with session_scope() as session:
        for k, v in enumerate(data['premiumList']):
            if k == 0:
                data['ouvs_order_number'] = v['order_number']
                data['ouvs_order_date'] = v['order_date']
                data['ouvs_percentage'] = v['percentage']
                data['ouvs_is_active'] = v['disabled']
            elif k == 1:
                data['admission_form_order_number'] = v['order_number']
                data['admission_form_order_date'] = v['order_date']
                data['admission_form_percentage'] = v['percentage']
                data['admission_form_is_active'] = v['disabled']
            elif k == 2:
                data['award_order_number'] = v['order_number']
                data['award_order_date'] = v['order_date']
                data['award_percentage'] = v['percentage']
                data['award_is_active'] = v['disabled']
            elif k == 3:
                data['qualification_order_number'] = v['order_number']
                data['qualification_order_date'] = v['order_date']
                data['qualification_percentage'] = v['percentage']
                data['qualification_is_active'] = v['disabled']
            elif k == 4:
                data['primary_premium_order_name'] = v['name']
                data['primary_premium_order_number'] = v['order_number']
                data['primary_premium_order_date'] = v['order_date']
                data['primary_premium_percentage'] = v['percentage']
                data['primary_premium_is_active'] = v['disabled']
            elif k == 5:
                data['secondary_premium_order_name'] = v['name']
                data['secondary_premium_order_number'] = v['order_number']
                data['secondary_premium_order_date'] = v['order_date']
                data['secondary_premium_percentage'] = v['percentage']
                data['secondary_premium_is_active'] = v['disabled']
        del data['premiumList']
        return data


def create_money_certificate_payment(id: str, year: str, data: dict) -> dict:
    """ Запрос создания новой выплаты """
    with session_scope() as session:
        money_certificate = serialize(session.query(MoneyCertificate).filter(MoneyCertificate.id == id).first())
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!' if money_certificate else 'Ошибка!',
                                     detail='Выплата добавлена!' if money_certificate else 'По указанному идентификатору карта денежного довольствия не найдена!',
                                     ).get_message()]}


def get_money_certificate_payment(id: str) -> dict:
    """ Запрос получения выплаты """
    with session_scope() as session:
        payment = serialize(session.query(MoneyCertificatePayment).filter(MoneyCertificatePayment.id == id).first())
        return {'data': payment, 'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail='Выплата добавлена!',
                                     ).get_message()]}