export const person = '/person/'

export const card = '/card/'

export const card_payment = '/card_payment/'

export const eskk = '/eskk/'

export const rows_per_page = [10, 15, 20]


export const eskk_list = [
    {
        id: 0,
        name: 'Отчетные периоды',
        columns : [
            {
                field: 'name',
                name: 'Отчетный период'
            }
        ]
    },
    {
        id: 1,
        name: 'Классификатор окладов по воинским званиям',
        columns : [
            {
                field: 'name',
                name: 'Воинское звание'
            },
            {
                field: 'value',
                name: 'Оклад по воинскому званию'
            }
        ]
    },
    {
        id: 2,
        name: 'Классификатор окладов по тарифным разрядам',
        columns : [
            {
                field: 'name',
                name: 'Тарифный разряд'
            },
            {
                field: 'value',
                name: 'Оклад по тарифному разряду'
            }
        ]
    }
]

export const premiumList = [
    {
        'id': 0,
        'name': 'За ОУВС',
        'percentage': '-',
        'order_number': '-',
        'order_date': '-',
        'disabled': true,
    },
    {
        'id': 1,
        'name': 'За секретность',
        'percentage': '-',
        'order_number': '-',
        'order_date': '-',
        'disabled': true,
    },
    {
        'id': 2,
        'name': 'Премия',
        'percentage': '-',
        'order_number': '-',
        'order_date': '-',
        'disabled': true,
    },
    {
        'id': 3,
        'name': 'За классную квалификацию',
        'percentage': '-',
        'order_number': '-',
        'order_date': '-',
        'disabled': true,
    },
    {
        'id': 4,
        'name': 'Дополнительная надбавка',
        'percentage': '-',
        'order_number': '-',
        'order_date': '-',
        'disabled': true,
    },
    {
        'id': 5,
        'name': 'Дополнительная надбавка',
        'percentage': '-',
        'order_number': '-',
        'order_date': '-',
        'disabled': true,
    },
]

export const moneyCertificateFull = {
    "money_certificate_relation": {
        "card_author": null,
        "card_inspector": null,
        "certificate_date": null,
        "certificate_expire_date": null,
        "certificate_number": null,
        "id": null,
        "year_first": null,
        "year_first_relation": {
            "premiumList": [
                {
                    'id': 0,
                    'name': 'За ОУВС',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 1,
                    'name': 'За секретность',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 2,
                    'name': 'Премия',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 3,
                    'name': 'За классную квалификацию',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 4,
                    'name': null,
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 5,
                    'name': null,
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
            ],
            pnvl_year: 0,
            pnvl_month: 0,
            pnvl_day: 0,
            "admission_form_order_date": null,
            "admission_form_order_number": null,
            "admission_form_order_percentage": 0,
            "admission_form_order_sum": 0,
            "admission_form_percentage": null,
            "admission_form_sum": 0,
            "admission_form_is_active": false,
            "award_order_date": null,
            "award_order_number": null,
            "award_percentage": null,
            "award_sum": 0,
            "award_is_active": false,
            "id": null,
            "ouvs_order_date": null,
            "ouvs_order_number": null,
            "ouvs_percentage": null,
            "ouvs_sum": 0,
            "ouvs_is_active": false,
            "payment_status": null,
            "pnvl_date": null,
            "pnvl_experience": null,
            "pnvl_order_date": null,
            "pnvl_order_number": null,
            "pnvl_percentage": 0,
            "pnvl_sum": 0,
            "position_salary": 0,
            "primary_premium_order_name": null,
            "primary_premium_order_number": null,
            "primary_premium_order_date": null,
            "primary_premium_percentage": 0,
            "primary_premium_sum": 0,
            "primary_premium": false,
            "primary_premium_is_active": false,
            "qualification_order_date": null,
            "qualification_order_number": null,
            "qualification_percentage": null,
            "qualification_sum": 0,
            "qualification_premium": false,
            "qualification_is_active": false,
            "rank_salary": 0,
            "secondary_premium_order_name": null,
            "secondary_premium_order_number": null,
            "secondary_premium_order_date": null,
            "secondary_premium_percentage": 0,
            "secondary_premium_sum": 0,
            "secondary_premium": false,
            "secondary_premium_is_active": false,
            "total_salary": 0,
            "total_salary_date": null
        },
        "year_second": null,
        "year_second_relation": {
            "premiumList": [
                {
                    'id': 0,
                    'name': 'За ОУВС',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 1,
                    'name': 'За секретность',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 2,
                    'name': 'Премия',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 3,
                    'name': 'За классную квалификацию',
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 4,
                    'name': null,
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
                {
                    'id': 5,
                    'name': null,
                    'percentage': null,
                    'order_number': null,
                    'order_date': null,
                    'disabled': true,
                },
            ],
            pnvl_year: 0,
            pnvl_month: 0,
            pnvl_day: 0,
            "admission_form_order_date": null,
            "admission_form_order_number": null,
            "admission_form_order_percentage": 0,
            "admission_form_order_sum": 0,
            "admission_form_percentage": null,
            "admission_form_sum": 0,
            "award_order_date": null,
            "award_order_number": null,
            "award_percentage": null,
            "award_sum": 0,
            "id": null,
            "ouvs_order_date": null,
            "ouvs_order_number": null,
            "ouvs_percentage": null,
            "ouvs_sum": 0,
            "payment_status": null,
            "pnvl_date": null,
            "pnvl_experience": null,
            "pnvl_order_date": null,
            "pnvl_order_number": null,
            "pnvl_percentage": 0,
            "pnvl_sum": 0,
            "position_salary": 0,
            "primary_premium_order_name": null,
            "primary_premium_order_number": null,
            "primary_premium_order_date": null,
            "primary_premium_percentage": 0,
            "primary_premium_sum": 0,
            "qualification_order_date": null,
            "qualification_order_number": null,
            "qualification_percentage": null,
            "qualification_sum": 0,
            "rank_salary": 0,
            "secondary_premium_order_name": null,
            "secondary_premium_order_number": null,
            "secondary_premium_order_date": null,
            "secondary_premium_percentage": 0,
            "secondary_premium_sum": 0,
            "total_salary": 0,
            "total_salary_date": null
        }
    },
    "person_relation": {
        "arrived_from": null,
        "birthday": null,
        "firstname": null,
        "fullname": null,
        "id": null,
        "inn": null,
        "isActive": null,
        "job_position": null,
        "job_position_order_appointment_date": null,
        "job_position_order_appointment_number": null,
        "job_position_order_entry_date": null,
        "job_position_order_entry_number": null,
        "job_rank": null,
        "job_rank_relation": {
            "name": "string",
            "value": 0
        },
        "lastname": null,
        "middlename": null,
        "personal_number": null,
        "tariff_category": null,
        "tariff_category_relation": {
            "name": null,
            "value": 0
        },
        "unit": null,
        "updated_utc": null,
        "vus": null
    },
    "report_period_relation": {
        "id": null,
        "value": null
    }
}

export const Person = {
    firstname: null,
    middlename: null,
    lastname: null,
    birthday: null,
    job_rank: null,
    job_position: null,
    job_position_order_entry_number: null,
    job_position_order_entry_date: null,
    job_position_order_appointment_number: null,
    job_position_order_appointment_date: null,
    vus: null,
    unit: null,
    inn: '',
    arrived_from: null
}

export const MoneyCertificate = {
    person: null,
    certificate_number: null,
    certificate_date: null,
    certificate_expire_date: null,
    card_author: null,
    card_inspector: null
}