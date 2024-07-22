<script setup>
defineProps(['payment'])
</script>

<template>        <Fieldset toggleable legend="Итог" class="col-12 mt-3">
    <div class="formgrid grid">
        <div class="field col-12">
            <table class="iksweb">
                <tbody>
                <tr>
                    <td rowspan="2">Оклад по в/должности</td>
                    <td rowspan="2">Оклад по в/званию</td>
                    <td colspan="2">ПНВЛ</td>
                    <td rowspan="2">Надбавка за ОУВС</td>
                    <td rowspan="2">Надбавка за секретность</td>
                    <td rowspan="2">Премия</td>
                    <td rowspan="2">Надбавка за КК</td>
                    <td rowspan="2">{{ payment.premiumList[4].name }}</td>
                    <td rowspan="2">{{ payment.premiumList[5].name }}</td>
                    <td rowspan="2">Всего начислено</td>
                    <td rowspan="2">С какого числа</td>
                </tr>
                <tr>
                    <td>%</td>
                    <td>сумма</td>
                </tr>

                <tr>
                    <td>{{ payment.rank_salary }} ₽</td>
                    <td>{{ payment.position_salary }} ₽</td>
                    <td>{{ payment.pnvl_percentage }}</td>
                    <td>{{ payment.pnvl_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.ouvs_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.admission_form_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.award_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.qualification_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.primary_premium_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.secondary_premium_sum.toFixed(2) }} ₽</td>
                    <td>{{ payment.total_salary.toFixed(2) }} ₽</td>
                    <td style="max-width: 25px;"><Calendar date-format="dd.mm.yy" v-model="payment.total_salary_date"/></td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</Fieldset>
</template>

<style scoped lang="scss">

</style>