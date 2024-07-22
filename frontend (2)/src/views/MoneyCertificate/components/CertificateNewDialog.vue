<script setup>
import { regularGet, regularPost } from '@/api/axios';
import { ref, inject } from 'vue';

const props = defineProps(['certificate', 'period'])
const emit = defineEmits(['update:dialogStatus', 'getMoneyCertificateList'])
let { submitted, changeSubmittedStatus } = inject('submitted')

const createMoneyCertificateDialog = inject('createMoneyCertificateDialog')
const foundedPersonList = ref([])

const searchPersonNoCertificate = (query) => {
    regularGet('/person/search_no_certificate?name=' + query + '&period=' + props.period).then((response) => foundedPersonList.value = response.data.data)
}

const createMoneyCertificate = () => {
    changeSubmittedStatus(true)
    let cert = props.certificate
    if (cert.person !== null || cert.certificate_number !== null) {
        regularPost('/card/create?person=' + cert.person.id + '&period=' + props.period, cert).then(async () => {
            emit('getMoneyCertificateList')
        })
    }
}

</script>

<template>
    <Dialog :draggable="false" :pt="{
                        mask: {style: 'backdrop-filter: blur(2px)'}}"
            v-model:visible="createMoneyCertificateDialog" :style="{ width: '800px' }" header="Создание новой карты денежного довольствия" @update:visible="emit('update:dialogStatus')" :modal="true" class="p-fluid">

        <Fieldset legend="Военнослужащий" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-12">
                    <label for="person">ФИО</label>
                    <AutoComplete id="person"
                                  @complete="searchPersonNoCertificate($event.query)"
                                  v-model="props.certificate.person"
                                  :suggestions="foundedPersonList"
                                  optionLabel="fullname"
                                  forceSelection/>
                    <small>У военнослужающего должна отсутствовать карта денежного довольствия в текущем периоде</small>
                    <small class="p-invalid" v-if="submitted && !props.certificate.person"><br>Выберите военнослужающего введя его ФИО!</small>
                </div>
            </div>
        </Fieldset>

        <Fieldset legend="Карта денежного довольствия" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-6">
                    <label for="certificate_number">Номер карты денежного довольствия</label>
                    <InputText id="certificate_number" v-model="props.certificate.certificate_number"/>
                    <small class="p-invalid" v-if="submitted && !props.certificate.certificate_number">Укажите номер карты денежного довольствия</small>
                </div>
                <div class="field col-6">
                    <label for="person.certificate_date">От какой даты карта денежного довольствия</label>
                    <Calendar date-format="dd.mm.yy" id="certificate_date" v-model="props.certificate.certificate_date"/>
                </div>
                <div class="field col-12">
                    <label for="person.certificate_expire_date">По какое число удовлетворен денежным довольствием</label>
                    <Calendar date-format="dd.mm.yy" id="certificate_expire_date" v-model="props.certificate.certificate_expire_date"/>
                </div>
            </div>
        </Fieldset>

        <Fieldset legend="Составил" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-6">
                    <label for="card_author">Карточку составил</label>
                    <InputText id="card_author" v-model="props.certificate.card_author"/>
                </div>
                <div class="field col-6">
                    <label for="card_inspector">Тарификацию проверил</label>
                    <InputText id="card_inspector" v-model="props.certificate.card_inspector"/>
                </div>
            </div>
        </Fieldset>

        <template #footer>
            <Button label="Сохранить" icon="pi pi-check" class="p-button-success" @click="createMoneyCertificate" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus', false)" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss">

</style>