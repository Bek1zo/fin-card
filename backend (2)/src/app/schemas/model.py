from typing import List
from sqlalchemy import types, ForeignKey, TIMESTAMP, sql, text
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.orm import Mapped
from . import Base
import datetime
from dataclasses import dataclass


class BaseModel(Base):
    """ Абстрактная базовая модель """
    __abstract__ = True
    __allow_unmapped__ = True

    id: Mapped[str] = mapped_column(primary_key=True, server_default=text('public.uuid_generate_v4()'))
    created_utc: Mapped[datetime.date] = mapped_column(TIMESTAMP(timezone=False), nullable=False, default=datetime.datetime.utcnow(), server_default=text('now()'))
    updated_utc: Mapped[datetime.date] = mapped_column(TIMESTAMP(timezone=False), nullable=True, onupdate=datetime.datetime.utcnow())


class Person(BaseModel):
    """ Персона """
    __tablename__ = "person"
    __table_args__ = {"schema": "lcard"}

    firstname: Mapped[str] = mapped_column(unique=False, nullable=False, comment='Имя')
    middlename: Mapped[str] = mapped_column(unique=False, nullable=False, comment='Отчество')
    lastname: Mapped[str] = mapped_column(unique=False, nullable=False, comment='Фамилия')
    birthday: Mapped[datetime.date] = mapped_column(unique=False, nullable=False, comment='День рождения')
    personal_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Личный номер')
    tariff_category: Mapped[str] = mapped_column(ForeignKey('lcard.position_salary.id'), unique=False, nullable=True, comment='Тарифный разряд')
    job_rank: Mapped[str] = mapped_column(ForeignKey('lcard.rank_salary.id'), unique=False, nullable=True, comment='Воинское звание')
    job_position: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Должность')

    job_position_order_entry_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа о вступление в должность')
    job_position_order_entry_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа о вступление в должность')

    job_position_order_appointment_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа о назначение на должность')
    job_position_order_appointment_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment="Дата приказа о назначение на должность")

    vus: Mapped[str] = mapped_column(unique=False, nullable=True, comment='ВУС')
    unit: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Подразделение')
    inn: Mapped[str] = mapped_column(unique=False, nullable=True, comment='ИНН')
    arrived_from: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Откуда прибыл')

    isActive: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.true(), comment='Статус военнослужащего')

    job_rank_relation: Mapped[List["RankSalary"]] = relationship("RankSalary")
    tariff_category_relation: Mapped[List["PositionSalary"]] = relationship("PositionSalary")

    money_certificate_relation: Mapped[List["MoneyCertificateRelation"]] = relationship('MoneyCertificateRelation', back_populates='person_relation')


class MoneyCertificatePayment(BaseModel):
    """ Выплата по денежному аттестату за каждый год"""
    __tablename__ = "money_certificate_payment"
    __table_args__ = {"schema": "lcard"}

    # Процентная надбавка за выслугу лет. (ПНВЛ)
    pnvl_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа стажа службы для ПНВЛ')
    pnvl_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='От какой даты приказ')
    pnvl_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='На какую дату актуальна информация')
    pnvl_experience: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Стаж службы. (Прим. дни-месяц-год)')
    pnvl_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент надбавки за выслугу лет')
    pnvl_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки за выслугу лет')

    position_salary: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Оклад по воинской должности')
    rank_salary: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Оклад по воинскому званию')

    # Процентная надбавка за особые условия военной службы
    ouvs_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа надбавки за ОУВС')
    ouvs_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа надбавки за ОУВС')
    ouvs_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент надбавки за ОУВС')
    ouvs_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки за ОУВС')
    ouvs_is_active: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.false(), comment='Активна ли надбавка')

    # Секретность
    admission_form_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа надбавки за секретность')
    admission_form_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа надбавки за секретность')
    admission_form_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент надбавки за секретность')
    admission_form_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки за секретность')
    admission_form_is_active: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.false(), comment='Активна ли надбавка')

    # Премия

    award_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа на премию')
    award_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа на премию')
    award_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент премии')
    award_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки')
    award_is_active: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.false(), comment='Активна ли надбавка')

    # Надбавка за классную квалификацию

    qualification_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа надбавки за кл. квалификацию')
    qualification_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа надбавки за кл. квалификацию')
    qualification_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент надбавки за кл. квалификацию')
    qualification_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки за кл. квалификацию.')
    qualification_is_active: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.false(), comment='Активна ли надбавка')

    # Дополнительная первичная надбавка


    primary_premium_order_name: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Наименование надбавки')
    primary_premium_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа надбавки')
    primary_premium_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа надбавки')
    primary_premium_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент надбавки')
    primary_premium_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки')
    primary_premium_is_active: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.false(), comment='Активна ли надбавка')

    # Дополнительная вторичная надбавка

    secondary_premium_order_name: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Наименования надбавки')
    secondary_premium_order_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер приказа надбавки')
    secondary_premium_order_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='Дата приказа надбавки')
    secondary_premium_percentage: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Процент надбавки')
    secondary_premium_sum: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Сумма надбавки')
    secondary_premium_is_active: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.false(), comment='Активна ли надбавка')

    # Итог

    total_salary: Mapped[float] = mapped_column(unique=False, nullable=True, comment='Всего начислено')
    total_salary_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='С какого числа начислено')

    payment_status: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Заполнены ли данные для выплаты полностью.', server_default=sql.false())

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value



class MoneyCertificate(BaseModel):
    """ Денежный аттестат """
    __tablename__ = "money_certificate"
    __table_args__ = {"schema": "lcard"}

    certificate_number: Mapped[str] = mapped_column(unique=False, nullable=True, comment='Номер карточки денежного довольствия')
    certificate_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='От какой даты денежный аттестат')
    certificate_expire_date: Mapped[datetime.date] = mapped_column(unique=False, nullable=True, comment='По какое число удовлетворение аттестатом')

    year_first: Mapped[str] = mapped_column(ForeignKey('lcard.money_certificate_payment.id'), unique=True, nullable=True, comment='Выплата за первый год отчетного периода')
    year_second: Mapped[str] = mapped_column(ForeignKey('lcard.money_certificate_payment.id'), unique=True, nullable=True, comment='Выплата за второй год отчетного периода')

    card_author: Mapped[str] = mapped_column(unique=False, comment='Составил карточки')
    card_inspector: Mapped[str] = mapped_column(unique=False, comment='Проверяющий карточки')

    year_first_relation: Mapped[List["MoneyCertificatePayment"]] = relationship('MoneyCertificatePayment', foreign_keys=('[MoneyCertificate.year_first]'))
    year_second_relation: Mapped[List["MoneyCertificatePayment"]] = relationship('MoneyCertificatePayment', foreign_keys=('[MoneyCertificate.year_second]'))


class ReportingPeriod(BaseModel):
    """ Отчетый период """
    __tablename__ = "reporting_period"
    __table_args__ = {"schema": "lcard"}

    value: Mapped[str] = mapped_column(unique=True, nullable=False, comment='Отчетный период (Прим. 2024-2025)')
    sort: Mapped[int] = mapped_column(unique=False, nullable=False, comment='Сортировка', autoincrement=True)


class MoneyCertificateRelation(BaseModel):
    """ Денежный аттестат за каждый из периодов """
    __tablename__ = "money_certificate_relation"
    __table_args__ = {"schema": "lcard"}

    person: Mapped[str] = mapped_column(ForeignKey('lcard.person.id'), unique=False, nullable=False, comment='Идентификатор персоны')
    money_certificate: Mapped[str] = mapped_column(ForeignKey('lcard.money_certificate.id', ondelete='CASCADE'), unique=False, nullable=False, comment='Идентификатор карточки денежного довольствия')
    reporting_period: Mapped[str] = mapped_column(ForeignKey('lcard.reporting_period.id'), unique=False, nullable=False, comment='Идентификатор периода')

    person_relation: Mapped[List["Person"]] = relationship('Person', back_populates='money_certificate_relation')
    money_certificate_relation: Mapped[List["MoneyCertificate"]] = relationship('MoneyCertificate')
    report_period_relation: Mapped[List["ReportingPeriod"]] = relationship('ReportingPeriod')


class PositionSalary(BaseModel):
    """ Справочник окладов по должности """
    __tablename__ = "position_salary"
    __table_args__ = {"schema": "lcard"}

    name: Mapped[str] = mapped_column(unique=True, nullable=False, comment='Тарифный разряд')
    value: Mapped[float] = mapped_column(unique=False, nullable=False, comment='Размер оклада по тарифному разряду')
    sort: Mapped[int] = mapped_column(unique=False, nullable=False, comment='Сортировка', autoincrement=True)
    isActive: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.true(), comment='Статус классификатора')


class RankSalary(BaseModel):
    """ Справочник окладов по званию """
    __tablename__ = "rank_salary"
    __table_args__ = {"schema": "lcard"}

    name: Mapped[str] = mapped_column(unique=True, nullable=False, comment='Воинское звание')
    value: Mapped[float] = mapped_column(unique=False, nullable=False, comment='Размер оклада по воинскому званию')
    sort: Mapped[int] = mapped_column(unique=False, nullable=False, comment='Сортировка', autoincrement=True)
    isActive: Mapped[bool] = mapped_column(unique=False, nullable=False, server_default=sql.true(), comment='Статус классификатора')
