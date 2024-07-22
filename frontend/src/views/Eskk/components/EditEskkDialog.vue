<script setup>
import { regularPut } from '@/api/axios';
import { inject } from 'vue';

const props = defineProps(['selectedCategory', 'eskk'])
const emit = defineEmits(['update:dialogStatus'])

const { submitted, changeSubmittedStatus } = inject('submitted')

const editEskkDialog = inject('editEskkDialog')
const editEskk = () => {
    changeSubmittedStatus(true)
    if (props.selectedCategory.id === 0) {
        if (props.eskk.value !== null && parseInt(props.eskk.value.split('-')[1]) === (parseInt(props.eskk.value.split('-')[0]) + 1)) {
            regularPut('/eskk/period/' + props.selectedEskk.id, props.selectedEskk)
        }
    } else {
        if (props.eskk.name && props.eskk.value) {
            const type = props.selectedCategory.id === 1 ? 'rank' : 'tariff_category'
            regularPut('/eskk/' + type + '/' + props.selectedEskk.id, props.selectedEskk)
        }}
}
</script>

<template>
    <Dialog :draggable="false" :pt="{mask: {style: 'backdrop-filter: blur(2px)'}}" v-model:visible="editEskkDialog" :style="{ width: '430px' }" header="Изменение информации в классификаторе" :modal="true" class="p-fluid">
        <Fieldset :legend="selectedCategory.name" class="mt-3">
            <div class="formgrid grid">
                <div class="" v-if="selectedCategory.columns[1]">
                    <div class="field col-12">
                        <label for="name">{{ selectedCategory.columns[0]?.name }}</label>
                        <InputText id="name" v-model="eskk.name" :class="{ 'p-invalid': submitted && !eskk.name }"/>
                        <small id="value" v-if="submitted && !eskk.name">Укажите наименование.</small>
                    </div>
                    <div class="field col-12">
                        <label for="value">{{ selectedCategory.columns[1]?.name }}</label>
                        <InputNumber id="value" v-model="eskk.value" :class="{ 'p-invalid': submitted && !eskk.value }" mode="currency" currency="RUB" locale="ru-RU"/>
                        <small id="value" v-if="submitted && !eskk.value">Укажите сумму оклада.</small>
                    </div>
                </div>
                <div class="col-12" v-else>
                    <div class="field">
                        <label for="value">{{ selectedCategory.columns[0]?.name }}</label>
                        <InputMask id="value" mask="2099-2099" v-model="eskk.value" :class="{ 'p-invalid': submitted && !eskk.value }"/>
                        <small id="value" v-if="submitted">Отчетный период указан в неверном формате. (Прим. 2020-2021)</small>
                        <small id="value" v-else>Укажите новый отчетный период. (Прим. 2020-2021)</small>
                    </div>
                </div>
            </div>
        </Fieldset>

        <template #footer>
            <Button label="Сохранить" icon="pi pi-check" class="p-button-success" @click="editEskk" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus')" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss">

</style>