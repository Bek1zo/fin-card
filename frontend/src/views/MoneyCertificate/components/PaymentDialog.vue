<script setup>
// Добавление выплаты

import { ref, watch } from 'vue';
import { regularGet, regularPut } from '@/api/axios';
import { moneyCertificateFull, premiumList } from '@/const/const';
import { formatDate } from '@/const/func';
import DialogFullBody from '@/views/MoneyCertificate/components/subcomponents/DialogFullBody.vue';


const personCertificateFull = ref(moneyCertificateFull)

const props = defineProps(['certificateId', 'dialogStatus', 'period'])
const emit = defineEmits(['update:dialogStatus', 'getMoneyCertificateList'])
const tab = ref(0)

watch(() => props.dialogStatus, (val) => {
    if (val) { getMoneyCertificate() } else { personCertificateFull.value = JSON.parse(JSON.stringify(moneyCertificateFull))}
})

// Обновление данных по выплате

const updateMoneyCertificatePayment = () => {
    let url
    let payload = {}
    if (tab.value === 0) {
        url = '/card_payment/?year=first&id=' + personCertificateFull.value.money_certificate_relation.id
        if (personCertificateFull.value.money_certificate_relation.year_first) {
            personCertificateFull.value.money_certificate_relation.year_first_relation.pnvl_experience = personCertificateFull.value.money_certificate_relation.year_first_relation.pnvl_year + '-' + personCertificateFull.value.money_certificate_relation.year_first_relation.pnvl_month + '-' + personCertificateFull.value.money_certificate_relation.year_first_relation.pnvl_day
        }
        payload = personCertificateFull.value.money_certificate_relation.year_first_relation
    } else if (tab.value === 1) {
        url = '/card_payment/?year=second&id=' + personCertificateFull.value.money_certificate_relation.id
        if (personCertificateFull.value.money_certificate_relation.year_second) {
            personCertificateFull.value.money_certificate_relation.year_second_relation.pnvl_experience = personCertificateFull.value.money_certificate_relation.year_second_relation.pnvl_year + '-' + personCertificateFull.value.money_certificate_relation.year_second_relation.pnvl_month + '-' + personCertificateFull.value.money_certificate_relation.year_second_relation.pnvl_day
        }
        payload = personCertificateFull.value.money_certificate_relation.year_second_relation
    }

    regularPut(url, payload).then(() => {
        console.log('here')
        emit('update:dialogStatus', false)
        emit('getMoneyCertificateList')
    })
}

// Отображение диалога и получение данных по персоне
const getMoneyCertificate = () => {
    regularGet('/card/relation/' + props.certificateId).then((response) => {
        if (!response.data.data.money_certificate_relation.year_first_relation) {
            response.data.data.money_certificate_relation.year_first_relation = personCertificateFull.value.money_certificate_relation.year_first_relation
        } else if (!response.data.data.money_certificate_relation.year_second_relation) {
            response.data.data.money_certificate_relation.year_second_relation = personCertificateFull.value.money_certificate_relation.year_second_relation
        }

        personCertificateFull.value = response.data.data

        // Первый год
        // ПНВЛ Стаж службы

        let money_certificate = personCertificateFull.value.money_certificate_relation
        let experience = null

        if (personCertificateFull.value.money_certificate_relation.year_first_relation && personCertificateFull.value.money_certificate_relation.year_first_relation.pnvl_experience) {
            experience = personCertificateFull.value.money_certificate_relation.year_first_relation.pnvl_experience.split('-')
        } else { experience = '0-0-0'.split('-') }

        money_certificate.year_first_relation.pnvl_date = formatDate(money_certificate.year_first_relation.pnvl_date)
        money_certificate.year_first_relation.pnvl_order_date =  formatDate(money_certificate.year_first_relation.pnvl_order_date)
        money_certificate.year_first_relation.pnvl_year = parseInt(experience[0])
        money_certificate.year_first_relation.pnvl_month = parseInt(experience[1])
        money_certificate.year_first_relation.pnvl_day = parseInt(experience[2])

        money_certificate.year_first_relation.premiumList = JSON.parse(JSON.stringify(premiumList))
        let premium = money_certificate.year_first_relation.premiumList

        premium[0].disabled = money_certificate.year_first_relation.ouvs_is_active ? true : false
        premium[0].percentage = money_certificate.year_first_relation.ouvs_percentage
        premium[0].order_number = money_certificate.year_first_relation.ouvs_order_number
        premium[0].order_date = money_certificate.year_first_relation.ouvs_order_date

        premium[1].disabled = money_certificate.year_first_relation.admission_form_is_active ? true : false
        premium[1].percentage = money_certificate.year_first_relation.admission_form_percentage
        premium[1].order_number = money_certificate.year_first_relation.admission_form_order_number
        premium[1].order_date = money_certificate.year_first_relation.admission_form_order_date

        premium[2].disabled = money_certificate.year_first_relation.award_is_active ? true : false
        premium[2].percentage = money_certificate.year_first_relation.award_percentage
        premium[2].order_number = money_certificate.year_first_relation.award_order_number
        premium[2].order_date = money_certificate.year_first_relation.award_order_date

        premium[3].disabled = money_certificate.year_first_relation.qualification_is_active ? true : false
        premium[3].percentage = money_certificate.year_first_relation.qualification_percentage
        premium[3].order_number = money_certificate.year_first_relation.qualification_order_number
        premium[3].order_date = money_certificate.year_first_relation.qualification_order_date

        // Дополнительная надбавка №1
        premium[4].disabled = money_certificate.year_first_relation.primary_premium_is_active ? true : false
        premium[4].name = money_certificate.year_first_relation.primary_premium_order_name ? money_certificate.year_first_relation.primary_premium_order_name : 'Доп. надбавка'
        premium[4].percentage = money_certificate.year_first_relation.primary_premium_percentage ? money_certificate.year_first_relation.primary_premium_percentage : 0
        premium[4].order_number = money_certificate.year_first_relation.primary_premium_order_number ? money_certificate.year_first_relation.primary_premium_order_number : '-'
        premium[4].order_date = money_certificate.year_first_relation.primary_premium_order_date ? money_certificate.year_first_relation.primary_premium_order_date : null
        money_certificate.year_first_relation.primary_premium_sum = money_certificate.year_first_relation.primary_premium_sum ? money_certificate.year_first_relation.primary_premium_sum : 0

        // Дополнительная надбавка №2
        premium[5].disabled = money_certificate.year_first_relation.secondary_premium_is_active ? true : false
        premium[5].name = money_certificate.year_first_relation.secondary_premium_order_name ? money_certificate.year_first_relation.secondary_premium_order_name : 'Доп. надбавка'
        premium[5].percentage = money_certificate.year_first_relation.secondary_premium_percentage ? money_certificate.year_first_relation.secondary_premium_percentage : 0
        premium[5].order_number = money_certificate.year_first_relation.secondary_premium_order_number ? money_certificate.year_first_relation.secondary_premium_order_number : '-'
        premium[5].order_date = money_certificate.year_first_relation.secondary_premium_order_date ? money_certificate.year_first_relation.secondary_premium_order_date : null
        money_certificate.year_first_relation.secondary_premium_sum = money_certificate.year_first_relation.secondary_premium_sum ? money_certificate.year_first_relation.secondary_premium_sum : 0

        if (personCertificateFull.value.money_certificate_relation.year_second_relation && personCertificateFull.value.money_certificate_relation.year_second_relation.pnvl_experience) {
            experience = personCertificateFull.value.money_certificate_relation.year_second_relation.pnvl_experience.split('-')
        } else { experience = '0-0-0'.split('-') }

        money_certificate.year_second_relation.pnvl_date = formatDate(money_certificate.year_second_relation.pnvl_date)
        money_certificate.year_second_relation.pnvl_order_date =  formatDate(money_certificate.year_second_relation.pnvl_order_date)
        money_certificate.year_second_relation.pnvl_year = parseInt(experience[0])
        money_certificate.year_second_relation.pnvl_month = parseInt(experience[1])
        money_certificate.year_second_relation.pnvl_day = parseInt(experience[2])

        money_certificate.year_second_relation.premiumList = JSON.parse(JSON.stringify(premiumList))
        premium = money_certificate.year_second_relation.premiumList

        premium[0].disabled = money_certificate.year_second_relation.ouvs_is_active ? true : false
        premium[0].percentage = money_certificate.year_second_relation.ouvs_percentage
        premium[0].order_number = money_certificate.year_second_relation.ouvs_order_number
        premium[0].order_date = money_certificate.year_second_relation.ouvs_order_date

        premium[1].disabled = money_certificate.year_second_relation.admission_form_is_active ? true : false
        premium[1].percentage = money_certificate.year_second_relation.admission_form_percentage
        premium[1].order_number = money_certificate.year_second_relation.admission_form_order_number
        premium[1].order_date = money_certificate.year_second_relation.admission_form_order_date

        premium[2].disabled = money_certificate.year_second_relation.award_is_active ? true : false
        premium[2].percentage = money_certificate.year_second_relation.award_percentage
        premium[2].order_number = money_certificate.year_second_relation.award_order_number
        premium[2].order_date = money_certificate.year_second_relation.award_order_date

        premium[3].disabled = money_certificate.year_second_relation.qualification_is_active ? true : false
        premium[3].percentage = money_certificate.year_second_relation.qualification_percentage
        premium[3].order_number = money_certificate.year_second_relation.qualification_order_number
        premium[3].order_date = money_certificate.year_second_relation.qualification_order_date

        // Дополнительная надбавка №1
        premium[4].disabled = money_certificate.year_second_relation.primary_premium_is_active ? true : false
        premium[4].name = money_certificate.year_second_relation.primary_premium_order_name ? money_certificate.year_second_relation.primary_premium_order_name : 'Доп. надбавка'
        premium[4].percentage = money_certificate.year_second_relation.primary_premium_percentage ? money_certificate.year_second_relation.primary_premium_percentage : 0
        premium[4].order_number = money_certificate.year_second_relation.primary_premium_order_number ? money_certificate.year_second_relation.primary_premium_order_number : '-'
        premium[4].order_date = money_certificate.year_second_relation.primary_premium_order_date ? money_certificate.year_second_relation.primary_premium_order_date : null
        money_certificate.year_second_relation.primary_premium_sum = money_certificate.year_second_relation.primary_premium_sum ? money_certificate.year_second_relation.primary_premium_sum : 0

        // Дополнительная надбавка №2
        premium[5].disabled = money_certificate.year_second_relation.secondary_premium_is_active ? true : false
        premium[5].name = money_certificate.year_second_relation.secondary_premium_order_name ? money_certificate.year_second_relation.secondary_premium_order_name : 'Доп. надбавка'
        premium[5].percentage = money_certificate.year_second_relation.secondary_premium_percentage ? money_certificate.year_second_relation.secondary_premium_percentage : 0
        premium[5].order_number = money_certificate.year_second_relation.secondary_premium_order_number ? money_certificate.year_second_relation.secondary_premium_order_number : '-'
        premium[5].order_date = money_certificate.year_second_relation.secondary_premium_order_date ? money_certificate.year_second_relation.secondary_premium_order_date : null
        money_certificate.year_second_relation.secondary_premium_sum = money_certificate.year_second_relation.secondary_premium_sum ? money_certificate.year_second_relation.secondary_premium_sum : 0
    })
}


// Выполнение перерассчета
const recalculation = () => {
    let year = null
    if (tab.value === 0) {
        year = personCertificateFull.value.money_certificate_relation.year_first_relation
    } else if (tab.value === 1) {
        year = personCertificateFull.value.money_certificate_relation.year_second_relation
    }

    year.rank_salary = personCertificateFull.value.person_relation.job_rank_relation.value
    year.position_salary = personCertificateFull.value.person_relation.tariff_category_relation.value

    let totalSalary = year.rank_salary + year.position_salary

    year.pnvl_percentage = pnvl_percentage(year)
    year.pnvl_sum = calculatePercentage(totalSalary, year.pnvl_percentage)

    if (!year.premiumList[0].disabled) { year.ouvs_sum = 0 }
    else { year.ouvs_sum = calculatePercentage(year.rank_salary, year.premiumList[0].percentage) }

    if (!year.premiumList[1].disabled) { year.admission_form_sum = 0 }
    else { year.admission_form_sum = calculatePercentage(year.rank_salary, year.premiumList[1].percentage) }

    if (!year.premiumList[2].disabled) { year.award_sum = 0 }
    else { year.award_sum = calculatePercentage(totalSalary, year.premiumList[2].percentage) }

    if (!year.premiumList[3].disabled) { year.qualification_sum = 0 }
    else { year.qualification_sum = calculatePercentage(year.rank_salary, year.premiumList[3].percentage) }

    if (!year.premiumList[4].disabled) { year.primary_premium_sum = 0 }
    else { year.primary_premium_sum = calculatePercentage(year.rank_salary, year.premiumList[4].percentage) }

    if (!year.premiumList[5].disabled) { year.secondary_premium_sum = 0 }
    else { year.secondary_premium_sum = calculatePercentage(year.rank_salary, year.premiumList[5].percentage) }

    year.total_salary = year.ouvs_sum + year.admission_form_sum + year.award_sum + year.qualification_sum + year.primary_premium_sum + year.secondary_premium_sum + year.rank_salary + year.position_salary
}

// Расчет суммы надбавки в процентах
const calculatePercentage = (sum, percentage) => {
    return (sum / 100) * percentage
}

// Расчет процентной надбавки за выслугу лет
const pnvl_percentage = (year) => {
    year = year.pnvl_year
    let result
    if ( year >= 2 && year <= 4 ) {
        result = 10
    } else if ( year >= 5 && year <= 9 ) {
        result = 15
    } else if ( year >= 10 && year <= 14) {
        result = 20
    } else if ( year >= 15 && year <= 19) {
        result = 25
    } else if ( year >= 20 && year <= 24) {
        result = 30
    } else if ( year >= 25) {
        result = 40
    } else {
        result = 0
    }
    return result
}


</script>

<template>
    <Dialog :draggable="false" :pt="{
                        mask: {style: 'backdrop-filter: blur(2px);'}}"
            v-model:visible="props['dialogStatus']" @update:visible="emit('update:dialogStatus')" :style="{ width: '1400px', 'min-height': '830px' }" header="Внесение выплаты в карту денежного довольствия" :modal="true" class="p-fluid">
        <TabView :activeIndex="tab" @update:activeIndex="tab = $event">
            <TabPanel :header="period.split('-')[0] + ' год'">
                <DialogFullBody :person="personCertificateFull.person_relation" :payment="personCertificateFull.money_certificate_relation.year_first_relation"/>
            </TabPanel>
            <TabPanel :header="period.split('-')[1] + ' год'">
                <DialogFullBody :person="personCertificateFull.person_relation" :payment="personCertificateFull.money_certificate_relation.year_second_relation"/>
            </TabPanel>
        </TabView>

        <template #footer>
            <Button label="Сохранить" icon="pi pi-check" class="p-button-success" @click="updateMoneyCertificatePayment()" />
            <Button label="Выполнить перерасчет" icon="pi pi-sync" class="p-button-warning" @click="recalculation()" />
            <Button label="Загрузить данные из последнего отчетного периода" icon="pi pi-copy" class="p-button-info" @click="" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus')" />
        </template>
    </Dialog>
</template>

<style lang="scss">
.p-dialog .p-dialog-content {
    overflow-y: hidden !important;
}

table.iksweb {
    text-decoration: none;border-collapse:collapse;width:100%;text-align:center;
}
table.iksweb th {
    font-weight:normal;
    font-size:14px;
    color:#000000;
    background-color:#ffffff;
}
table.iksweb td {
    font-size:13px;
    color:#fff;
}
table.iksweb td,table.iksweb th {
    white-space:pre-wrap;padding:10px 5px;line-height:13px;vertical-align: middle;border: 1px solid gray;
}

.disabled {
    text-decoration: underline;
}
</style>