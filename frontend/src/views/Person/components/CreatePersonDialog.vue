<script setup>


import { inject } from 'vue';
import { regularPost } from '@/api/axios';

const props = defineProps(['person'])
const emit = defineEmits('update:dialogStatus', 'getPersonList')
const { submitted, changeSubmittedStatus } = inject('submitted')
const createPersonDialog = inject('createPersonDialog')

const createPerson = () => {
    changeSubmittedStatus(true)
    if (props.person.firstname && props.person.middlename && props.person) {
        regularPost('/person/create', props.person).then(async () => {
            emit('update:dialogStatus')
            emit('getPersonList')
        })
    }
}

</script>

<template>
    <Dialog @update:visible="emit('update:dialogStatus')" :draggable="false" :pt="{
                        mask: {style: 'backdrop-filter: blur(2px)'}}"
            v-model:visible="createPersonDialog" :style="{ width: '800px' }" header="Добавление военнослужащего" :modal="true" class="p-fluid">

        <Fieldset legend="Персональная информация">
            <div class="formgrid grid">
                <div class="field col-4">
                    <label for="firstname">Имя</label>
                    <InputText id="firstname" v-model="person.firstname" :class="{ 'p-invalid': submitted && !person.firstname }" :required="true" />
                    <small class="p-invalid" v-if="submitted && !person.firstname">Не введено имя.</small>
                </div>

                <div class="field col-4">
                    <label for="middlename">Отчество</label>
                    <InputText id="middlename"  v-model="person.middlename" :class="{ 'p-invalid': submitted && !person.middlename }" :required="true" />
                    <small class="p-invalid" v-if="submitted && !person.middlename">Не введено отчество.</small>
                </div>

                <div class="field col-4">
                    <label for="lastname">Фамилия</label>
                    <InputText id="lastname" v-model="person.lastname" :class="{ 'p-invalid': submitted && !person.lastname }" :required="true" />
                    <small class="p-invalid" v-if="submitted && !person.lastname">Не введена фамилия.</small>
                </div>

                <div class="field col-6">
                    <label for="birthday">День рождения</label>
                    <Calendar id="birthday" v-model="person.birthday" :class="{ 'p-invalid': submitted && !person.birthday }" :required="false" dateFormat="dd.mm.yy" :max-date="new Date()"/>
                    <small class="p-invalid" v-if="submitted && !person.birthday">Не указана дата рождения</small>
                </div>

                <div class="field col-6">
                    <label for="person.inn">ИНН</label>
                    <InputText id="inn" v-model="person.inn" :class="{ 'p-invalid': submitted && (person.inn.length !== 12 && person.inn.length >= 1)}" :maxlength="12" :required="false" />
                    <small class="p-invalid flex" v-if="submitted && (person.inn.length !== 12 && person.inn.length >= 1)">Проверьте правильность ввода. ИНН должен состоять из 12 цифр.</small>
                </div>
            </div>
        </Fieldset>

        <template #footer>
            <Button label="Сохранить" icon="pi pi-check" class="p-button-success" @click="createPerson()" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus')" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss">

</style>