SELECT
"IMYA" AS firstname,
"OTCHESTVO" AS middlename,
"family" AS lastname,
"DBURN" AS birthday,
"LNUMBER" AS personal_number,
"TRAZRYAD" AS tariff_category,
"ZVANIE" AS job_rank,
"DOLJNOST" AS job_position,
"PVSTYPLEN_N" AS job_position_order_appointment_number,
"PVSTYPLEN_D" AS job_position_order_appointment_date,
"PNAZNACHEN_N" AS job_position_order_entry_number,
"PNAZNACHEN_D" AS job_position_order_entry_date,
"VUS" AS vus,
"PODRAZDELENIE" AS unit,
"inn" AS inn,
"PRIBYLIZ" AS arrived_from,
"FROMDATE" AS reporting_period,
"MONEYATTN" AS certificate_number,
"MONEYATTFROM" AS certificate_date,
"MONEYUDOVLPO" AS certificate_expire_date,
"SOSTAVIL" AS card_author,
"PROVERIL" AS card_inspector,
"PNVLPRIKAZ" AS pnvl_order_number,
"PNVLOT" AS pnvl_date,
"PNVLNA" AS pnvl_order_date,
"PNVLDAY" AS pnvl_experience_day,
"PNVLMONTH" AS pnvl_experience_month,
"PNVLYEAR" AS pnvl_experience_year,
"PNVLPROCENT" AS pnvl_percentage,
"PNVL" AS pnvl_sum,
"OVD" AS position_salary,
"OVZ" AS rank_salary,
"OUVS_N" AS ouvs_order_number,
"OUVS_D" AS ouvs_order_date,
"OUVS_P" AS ouvs_percentage,
"OUVS" AS ouvs_sum,
"SECRETNOST_N" AS admission_form_order_number,
"SECRETNOST_D" AS admission_form_order_date,
"SECRETNOST_P" AS admission_form_order_percentage,
"SECRETNOST" AS admission_form_order_sum,
"PREMYA_N" AS award_order_number,
"PREMYA_D" AS award_order_date,
"PREMYA_P" AS award_order_percentage,
"PREMYA" AS award_order_sum,
"KK_N" AS qualification_order_number,
"KK_D" AS qualification_order_date,
"KK_P" AS qualification_order_percentage,
"KK" AS qualification_order_sum,
"DOP1NAME" AS primary_order_name,
"DOP1_N" AS primary_order_number,
"DOP1_D" AS primary_order_date,
"DOP1_P" AS primary_order_percentage,
"DOP1" AS primary_order_sum,
"DOP2NAME" AS secondary_order_name,
"DOP2_N" AS secondary_order_number,
"DOP2_D" AS secondary_order_date,
"DOP2_P" AS secondary_order_percentage,
"DOP2" AS secondary_order_sum,
"VSEGO" AS total_salary
FROM person.persons
JOIN financial_card.financial_card ON person.persons.id_e = financial_card.financial_card.emp_id
ORDER BY lastname