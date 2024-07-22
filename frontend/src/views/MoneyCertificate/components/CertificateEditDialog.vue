<script setup>
import { inject } from 'vue';
import { regularPut } from '@/api/axios';

let props = defineProps(['dialogStatus', 'certificate'])
let emit = defineEmits(['update:dialogStatus', 'getMoneyCertificateList'])
let { submitted, changeSubmittedStatus } = inject('submitted')
const editMoneyCertificateDialog = inject('editMoneyCertificateDialog')


// Обновление данных сертификата
const updateCertificate = () => {
    changeSubmittedStatus()
    regularPut('/card/update/' + props.certificate.id, props.certificate).then(async () => {
        emit('getMoneyCertificateList')
    })
}

</script>

<template>
    <Dialog :draggable="false" :pt="{
                        mask: {style: 'backdrop-filter: blur(2px)'}}"
            v-model:visible="editMoneyCertificateDialog" :style="{ width: '800px' }" header="Внесение информации о карте денежного довольствия" @update:visible="emit('update:dialogStatus', $event)" :modal="true" class="p-fluid">

        <Fieldset legend="Карта денежного довольствия" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-6">
                    <label for="certificate_number">Номер карты денежного довольствия</label>
                    <InputText id="certificate_number" v-model="certificate.certificate_number"/>
                    <small class="p-invalid" v-if="submitted && !certificate.certificate_number">Укажите номер карты</small>
                </div>
                <div class="field col-6">
                    <label for="certificate_date">От какой даты карта денежного довольствия</label>
                    <Calendar id="certificate_date" date-format="dd.mm.yy" v-model="certificate.certificate_date"/>
                    <small class="p-invalid" v-if="submitted && !certificate.certificate_date">Укажите дату сертификата</small>
                </div>
                <div class="field col-12">
                    <label for="certificate_expire_date">По какое число удовлетворен денежным довольствием</label>
                    <Calendar id="certificate_expire_date" date-format="dd.mm.yy" v-model="certificate.certificate_expire_date"/>
                    <small class="p-invalid" v-if="submitted && !certificate.certificate_expire_date">Укажите по какое число удовлетворен ДД</small>
                </div>
            </div>
        </Fieldset>

        <Fieldset legend="Составил" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-6">
                    <label for="card_author">Карточку составил</label>
                    <InputText id="card_author" v-model="certificate.card_author"/>
                </div>
                <div class="field col-6">
                    <label for="card_inspector">Тарификацию проверил</label>
                    <InputText id="card_inspector" v-model="certificate.card_inspector"/>
                </div>
            </div>
        </Fieldset>

        <template #footer>
            <Button label="Сохранить" icon="pi pi-check" class="p-button-success" @click="updateCertificate()" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus', false)" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss">

</style>