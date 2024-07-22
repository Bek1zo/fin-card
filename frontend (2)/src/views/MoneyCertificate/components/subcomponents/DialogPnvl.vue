<script setup>
defineProps(['payment', 'submitted'])
</script>

<template>
    <Fieldset legend="Стаж службы для ПНВЛ" class="col-11 mt-3">
        <div class="formgrid grid">
            <div class="field col-4">
                <label for="person">Пр. №</label>
                <InputText id="person" v-model="payment.pnvl_order_number" optionLabel="fullname" />
                <small class="p-invalid" v-if="submitted && !payment.pnvl_order_number">Укажите номер приказа</small>
            </div>
            <div class="field col-4">
                <label for="person">на</label>
                <Calendar id="person" v-model="payment.pnvl_date" date-format="dd.mm.yy" optionLabel="fullname" />
                <small class="p-invalid" v-if="submitted && !payment.pnvl_date">Укажите на какое число приказ</small>
            </div>
            <div class="field col-4">
                <label for="person">от</label>
                <Calendar id="person" v-model="payment.pnvl_order_date" optionLabel="fullname" />
                <small class="p-invalid" v-if="submitted && !payment.pnvl_order_date">Укажите от какого числа приказ</small>
            </div>
            <div class="field col-4">
                <label for="person">лет</label>
                <InputNumber v-model="payment.pnvl_year" inputId="minmax-buttons" mode="decimal" showButtons :min="0" :max="99" />
                <small class="p-invalid" v-if="submitted && !payment.pnvl_year">Укажите кол-во выслуженных лет</small>
            </div>
            <div class="field col-4">
                <label for="person">месяцев</label>
                <InputNumber v-model="payment.pnvl_month" inputId="minmax-buttons" mode="decimal" showButtons :min="0" :max="12" />
                <small class="p-invalid" v-if="submitted && !payment.pnvl_month">Укажите кол-во выслуженных месяцев</small>
            </div>
            <div class="field col-4">
                <label for="paymentMoneyCertificate.pnvl_day">дней</label>
                <InputNumber v-model="payment.pnvl_day" inputId="minmax-buttons" mode="decimal" showButtons :min="0" :max="31" />
                <small class="p-invalid" v-if="submitted && !payment.pnvl_day">Укажите кол-во выслуженных дней</small>
            </div>
        </div>
    </Fieldset>
</template>

<style scoped lang="scss">

</style>