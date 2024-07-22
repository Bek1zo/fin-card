<script setup>
import { regularGet, regularPut } from '@/api/axios';
import { inject, onMounted, ref } from 'vue';

const props = defineProps(['person'])
const emit = defineEmits('update:dialogStatus', 'getPersonList')

const { submitted, changeSubmittedStatus } = inject('submitted')
const createArmyDialog = inject('createArmyDialog')

let rankList = ref([])
let tariffCategoryList = ref([])

onMounted(() => {
    getEskk()
})

const createArmy = () => {
    changeSubmittedStatus(true)
    if (props.person.job_rank && props.person.job_position) {
        regularPut('/person/' + props.person.id, props.person).then(async () => {
            emit('getPersonList')
            emit('update:dialogStatus')
        })
    }
}

const getEskk = async () => {
    await regularGet('/eskk/rank').then((response) => {rankList.value = response.data.data})
    await regularGet('/eskk/tariff_category').then((response) => {tariffCategoryList.value = response.data.data})
}
</script>

<template>
    <Dialog @update:visible="emit('update:dialogStatus')" :draggable="false" :pt="{mask: {style: 'backdrop-filter: blur(2px)'}}" v-model:visible="createArmyDialog" :style="{ width: '800px' }" header="Внесение информации о военной службе" :modal="true" class="p-fluid">

        <Fieldset legend="Военная служба" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-6">
                    <label for="person.job_rank">Воинское звание</label>
                    <Dropdown id="job_rank" v-model="person.job_rank" :options="rankList" :class="{ 'p-invalid': submitted && !person.job_rank }" optionLabel="name" optionValue="id" placeholder="Выберите воинское звание"></Dropdown>
                    <small class="p-invalid" v-if="submitted && !person.job_rank">Выберите воинское звание</small>
                </div>
                <div class="field col-6">
                    <label for="person.tariff_category">Тарифный разряд</label>
                    <Dropdown id="tariff_category" v-model="person.tariff_category" :options="tariffCategoryList" :class="{ 'p-invalid': submitted && !person.tariff_category }" optionValue="id" optionLabel="name" placeholder="Выберите тарифный разряд"></Dropdown>
                    <small class="p-invalid" v-if="submitted && !person.tariff_category">Выберите тарифный разряд</small>
                </div>
                <div class="field col-6">
                    <label for="person.unit">Подразделение</label>
                    <InputText id="unit" v-model="person.unit"/>
                </div>
                <div class="field col-6">
                    <label for="person.job_position">Должность</label>
                    <InputText id="job_position" v-model="person.job_position"/>
                </div>
                <div class="field col-4">
                    <label for="person.arrived_from">Прибыл из</label>
                    <InputText id="arrived_from" v-model="person.arrived_from"/>
                </div>
                <div class="field col-4">
                    <label for="person.vus">ВУС</label>
                    <InputText id="vus" v-model="person.vus"/>
                </div>
                <div class="field col-4">
                    <label for="person.personal_number">Персональный номер</label>
                    <InputText id="personal_number" v-model="person.personal_number"/>
                </div>
            </div>
        </Fieldset>

        <Fieldset legend="Приказы" class="mt-3">
            <div class="formgrid grid">
                <div class="field col-6">
                    <label for="person.job_position_order_appointment_date">Номер приказа о вступление в должность</label>
                    <InputText id="job_position_order_appointment_date" v-model="person.job_position_order_appointment_number" />
                </div>
                <div class="field col-6">
                    <label for="person.job_position_order_appointment_date">Дата приказа</label>
                    <Calendar id="job_position_order_appointment_date" v-model="person.job_position_order_appointment_date" dateFormat="dd.mm.yy" :max-date="new Date()"/>
                </div>
                <div class="field col-6">
                    <label for="person.job_position_order_entry_number">Номер приказа о назначение на должность</label>
                    <InputText id="job_position_order_entry_number" v-model="person.job_position_order_entry_number"/>
                </div>
                <div class="field col-6">
                    <label for="person.job_position_order_entry_date">Дата приказа</label>
                    <Calendar id="job_position_order_entry_date" v-model="person.job_position_order_entry_date" dateFormat="dd.mm.yy" :max-date="new Date()"/>
                </div>
            </div>
        </Fieldset>

        <template #footer>
            <Button label="Сохранить" icon="pi pi-check" class="p-button-success" @click="createArmy" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus')" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss">

</style>