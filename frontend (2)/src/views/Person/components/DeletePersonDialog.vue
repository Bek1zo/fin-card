<script setup>
import { regularPut } from '@/api/axios';
import { inject } from 'vue';

const props = defineProps(['person'])
const emit = defineEmits('update:dialogStatus', 'getPersonList')

const deletePersonDialog = inject('deletePersonDialog')

const deletePerson = async () => {
    await regularPut('/person/' + props.person.id, {isActive: false}).then(async () => {
        emit('update:dialogStatus')
        emit('getPersonList')
    })
}
</script>

<template>
    <Dialog @update:visible="emit('update:dialogStatus')" v-model:visible="deletePersonDialog" :style="{ width: '450px' }" header="Подтвердите действие" :modal="true">
        <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span>Вы действительно хотите отметить военнослужащего<br> <b>{{ props.person.lastname }} {{ props.person.firstname }} {{  props.person.middlename }}</b> для удаления?</span>
        </div>
        <template #footer>
            <Button label="Подтвердить" icon="pi pi-check" class="p-button-success" @click="deletePerson()" />
            <Button label="Закрыть" icon="pi pi-times" class="p-button-danger" @click="emit('update:dialogStatus')" />
        </template>
    </Dialog>
</template>

<style scoped lang="scss">

</style>