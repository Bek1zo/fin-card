import uuid

from sqlalchemy import desc, and_, or_
from ...common.toast import *
from ...schemas.model import MoneyCertificate, MoneyCertificateRelation, ReportingPeriod, Person
from ...session import session_scope
from ...common.func import serialize


def search_money_certificate_relation(name: str, period: str) -> dict:
    """ Поиск полной инфромации по военнослужащему по ФИО """
    with session_scope() as session:
        period = session.query(ReportingPeriod).filter(ReportingPeriod.value == period).first()
        query = session.query(MoneyCertificateRelation).join(Person).filter(MoneyCertificateRelation.reporting_period == period.id).filter(and_(*[or_(Person.lastname.ilike(f"%{i}%"), Person.firstname.ilike(f"%{i}%"), Person.middlename.ilike(f"%{i}%")) for i in name.split(' ')])).limit(10).all()
        result = make_status(query)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value if len(result) > 0 else MessageEnum.ERROR.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Список военнослужащих с указанными данными загружен!',
                                     ).get_message()],
                'data': result}


def get_money_certificate_relation(id: str) -> dict:
    """ Запрос получение полной информации по военнослужащему и всех его карт ДД """
    with session_scope() as session:
        result = serialize(session.query(MoneyCertificateRelation).filter(MoneyCertificateRelation.id == id).order_by(MoneyCertificateRelation.created_utc).first())
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value if len(result) > 0 else MessageEnum.ERROR.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Информация по военнослужаещему загружена',
                                     ).get_message()],
                'data': result}


def get_money_certificate(id: str) -> dict:
    """ Запрос получения карточки ДД """
    with session_scope() as session:
        result = serialize(session.query(MoneyCertificate).filter(MoneyCertificate.id == id).first())
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value if len(result) > 0 else MessageEnum.ERROR.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!',
                                     detail=f'Денежный карта военнослужащего загружена!',
                                     ).get_message()],
                'data': result}


def get_money_certificate_last(id: str) -> dict:
    """ Запрос получения данных по последней карточки ДД """
    with session_scope() as session:
        result = session.query(MoneyCertificateRelation).filter(MoneyCertificateRelation.person == id).order_by(desc(MoneyCertificateRelation.created_utc)).first()
        result = serialize(result.money_certificate_relation) if hasattr(result, 'money_certificate_relation') else {}

        return {'messages': [Message(severity=MessageEnum.SUCCESS.value if len(result) > 0 else MessageEnum.ERROR.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!' if len(result) > 0 else 'Ошибка!',
                                     detail=f'Данные карточки денежного довольствия из предыдущего периода загружены' if len(result) > 0 else 'У военнослужащего отсутствуют карточки денежного довольствия',
                                     ).get_message()],
                'data': result}


def get_money_certificate_list(period: str, page_limit, page_offset) -> dict:
    """ Запрос получения списка карточек ДД """
    with session_scope() as session:
        period = session.query(ReportingPeriod).filter(ReportingPeriod.value == period).first()
        query = session.query(MoneyCertificateRelation).filter(MoneyCertificateRelation.reporting_period == period.id).join(MoneyCertificateRelation.person_relation).order_by(Person.lastname)
        total = query.count()
        query = query.limit(page_limit).offset((page_offset - 1) * page_limit).all()

        result = make_status(query)

        return {'messages': [Message(severity=MessageEnum.SUCCESS.value if len(result) > 0 else MessageEnum.ERROR.value,
                                     life=MessageEnum.TIME_5.value,
                                     summary='Успех!' if len(result) > 0 else 'Ошибка!',
                                     detail=f'Данные карточки денежного довольствия из предыдущего периода загружены' if len(result) > 0 else 'У военнослужащего отсутствуют карточки денежного довольствия',
                                     ).get_message()],
                'data': result,
                'total': total}


def make_status(query):
    """ Добавление статусов по выплатам первого и второго года """
    with session_scope() as session:
        result = []
        for i in query:
            year_first_status = True
            year_second_status = True
            if i.money_certificate_relation.year_first:
                if i.money_certificate_relation.year_first_relation.updated_utc is None:
                    year_first_status = None
                else:
                    except_list = ['id', 'created_utc', 'updated_utc']
                    if not i.money_certificate_relation.year_first_relation.ouvs_is_active:
                        except_list += ['ouvs_order_number', 'ouvs_order_date', 'ouvs_percentage', 'ouvs_sum', 'ouvs_is_active']
                    if not i.money_certificate_relation.year_first_relation.admission_form_is_active:
                        except_list += ['admission_form_order_number', 'admission_form_order_date', 'admission_form_percentage', 'admission_form_sum', 'admission_form_is_active']
                    if not i.money_certificate_relation.year_first_relation.award_is_active:
                        except_list += ['award_order_number', 'award_order_date', 'award_percentage', 'award_sum']
                    if not i.money_certificate_relation.year_first_relation.qualification_is_active:
                        except_list += ['qualification_order_number', 'qualification_order_date', 'qualification_percentage','qualification_sum']
                    if not i.money_certificate_relation.year_first_relation.primary_premium_is_active:
                        except_list += ['primary_premium_order_name', 'primary_premium_order_number', 'primary_premium_order_date', 'primary_premium_percentage', 'primary_premium_sum']
                    if not i.money_certificate_relation.year_first_relation.secondary_premium_is_active:
                        except_list += ['secondary_premium_order_name', 'secondary_premium_order_number', 'secondary_premium_order_date','secondary_premium_percentage', 'secondary_premium_sum']
                    for value in i.money_certificate_relation.year_first_relation:
                        if value[0] in except_list:
                            pass
                        else:
                            if value[1] is None or value[1] == '':
                                year_first_status = False
            else:
                year_first_status = False


            if i.money_certificate_relation.year_second:
                if i.person_relation.lastname == 'Абрамкин':
                    pass
                if i.money_certificate_relation.year_second_relation.updated_utc is None:
                    year_second_status = None
                else:
                    except_list = ['id', 'created_utc', 'updated_utc']
                    if not i.money_certificate_relation.year_second_relation.ouvs_is_active:
                        except_list += ['ouvs_order_number', 'ouvs_order_date', 'ouvs_percentage', 'ouvs_sum', 'ouvs_is_active']
                    if not i.money_certificate_relation.year_second_relation.admission_form_is_active:
                        except_list += ['admission_form_order_number', 'admission_form_order_date', 'admission_form_percentage', 'admission_form_sum', 'admission_form_is_active']
                    if not i.money_certificate_relation.year_second_relation.award_is_active:
                        except_list += ['award_order_number', 'award_order_date', 'award_percentage', 'award_sum']
                    if not i.money_certificate_relation.year_second_relation.qualification_is_active:
                        except_list += ['qualification_order_number', 'qualification_order_date', 'qualification_percentage','qualification_sum']
                    if not i.money_certificate_relation.year_second_relation.primary_premium_is_active:
                        except_list += ['primary_premium_order_name', 'primary_premium_order_number', 'primary_premium_order_date', 'primary_premium_percentage', 'primary_premium_sum']
                    if not i.money_certificate_relation.year_second_relation.secondary_premium_is_active:
                        except_list += ['secondary_premium_order_name', 'secondary_premium_order_number', 'secondary_premium_order_date','secondary_premium_percentage', 'secondary_premium_sum']
                    for value in i.money_certificate_relation.year_second_relation:
                        if value[0] in except_list:
                            pass
                        else:
                            if value[1] is None or value[1] == '':
                                year_second_status = False
            else:
                year_second_status = False

            result.append(
                {
                    'id': i.id,
                    'firstname': i.person_relation.firstname if i.person_relation.firstname else '',
                    'middlename': i.person_relation.middlename if i.person_relation.middlename else '',
                    'lastname': i.person_relation.lastname if i.person_relation.lastname else '',
                    'job_rank': i.person_relation.job_rank_relation.name if i.person_relation.job_rank_relation else '',
                    'certificate_number': i.money_certificate_relation.certificate_number if i.money_certificate_relation.certificate_number else '',
                    'certificate_date': i.money_certificate_relation.certificate_date.strftime('%d.%m.%Y') if i.money_certificate_relation.certificate_date else None,
                    'certificate_expire_date': i.money_certificate_relation.certificate_expire_date.strftime('%d.%m.%Y') if i.money_certificate_relation.certificate_expire_date else None,
                    'year_first': i.money_certificate_relation.year_first,
                    'year_second': i.money_certificate_relation.year_second,
                    'card_author': i.money_certificate_relation.card_author if i.money_certificate_relation.card_author else '',
                    'card_inspector': i.money_certificate_relation.card_inspector if i.money_certificate_relation.card_inspector else '',
                    'year_first_status': year_first_status,
                    'year_second_status': year_second_status,
                    'money_certificate_id': i.money_certificate_relation.id
                }
            )
        return result


def create_money_certificate(person: str, period: str, data: dict):
    """ Запрос создания новой карточки ДД """
    with session_scope() as session:
        data['id'] = str(uuid.uuid4())
        money_certificate = MoneyCertificate(**data)
        session.add(money_certificate)

        if period:
            period_id = session.query(ReportingPeriod.id).filter(ReportingPeriod.value == period).first()
        else:
            period_id = session.query(ReportingPeriod.id).order_by(desc(ReportingPeriod.sort)).first()

        money_certificate_relation = MoneyCertificateRelation(person=person, money_certificate=money_certificate.id, reporting_period=period_id.id, id = str(uuid.uuid4()))
        session.add(money_certificate_relation)

        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                      life=MessageEnum.TIME_5.value,
                                      summary='Успех!',
                                      detail='Денежная карта успешно создана',
                                      ).get_message()]}


def update_money_certificate(id: str, data: dict) -> dict:
    """ Запрос обновления данных карточки """
    with session_scope() as session:
        session.query(MoneyCertificate).filter(MoneyCertificate.id == id).update(data, synchronize_session=False)
        return {'messages': [Message(severity=MessageEnum.SUCCESS.value,
                                      life=MessageEnum.TIME_5.value,
                                      summary='Успех!',
                                      detail='Данные денежной карты обновлены!',
                                      ).get_message()]}