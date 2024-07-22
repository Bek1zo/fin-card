<script setup>

import { onMounted, ref, provide } from 'vue';
import { regularGet } from '@/api/axios';
import { eskk_list } from '@/const/const';
import CreateEskkDialog from '@/views/Eskk/components/CreateEskkDialog.vue';
import EditEskkDialog from '@/views/Eskk/components/EditEskkDialog.vue';


const selectedCategory = ref(eskk_list[0])
const tableData = ref([])
const eskk = ref({name: null, value: null})
const selectedEskk = ref(null)

const submitted = ref(false);
const changeSubmittedStatus = (status) => { submitted.value = status}
provide('submitted', {submitted, changeSubmittedStatus})

const createEskkDialog = ref(false)
provide('createEskkDialog', createEskkDialog)

const editEskkDialog = ref(false)
provide('editEskkDialog', editEskkDialog)

onMounted(() => {
    chooseMenu({value: eskk_list[0]})
})

const hideDialog = () => {
    chooseMenu({value: eskk_list[selectedCategory.value.id]})
    eskk.value = {name: null, value: null}
    createEskkDialog.value = false;
    editEskkDialog.value = false
    submitted.value = false;
};


const editEskkShow = (data) => {
    editEskkDialog.value = true
    selectedEskk.value = data
    eskk.value = data
}

const chooseMenu = (event) => {
    let id = event?.value?.id
    switch (id) {
        case 0:
            regularGet('eskk/period').then((response) => {
                tableData.value = response.data.data
            })
            break
        case 1:
            regularGet('eskk/rank').then((response) => {
                tableData.value = response.data.data
            })
            break
        case 2:
            regularGet('eskk/tariff_category').then((response) => {
                tableData.value = response.data.data
            })
            break
    }
}

</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="card" style="height: 660px;">
                <div class="flex flex-row gap-3 h-full">
                    <div class="flex flex-column align-items-center justify-content-center" style="width: 650px;">
                        <Listbox @change="chooseMenu($event)" v-model="selectedCategory" :options="eskk_list" optionLabel="name" class="flex flex-column w-full h-full">
                            <template #option="slotProps">
                                <div class="flex gap-2">
                                    <span class="pi p-icon pi-id-card"></span>
                                    <span class="text-lg">{{ slotProps.option.name }}</span>
                                </div>
                            </template>
                        </Listbox>
                    </div>
                    <div class="flex flex-column align-items-center justify-content-center w-full h-full">
                        <Toolbar class="w-full">
                            <template v-slot:start>
                                <div class="my-2">
                                    <Button label="Добавить" icon="pi pi-plus" class="mr-2" severity="success" @click="createEskkDialog = true" />
                                    <Button label="Редактировать" icon="pi pi-pencil" severity="warning" @click="editEskkShow(selectedEskk)" />
                                </div>
                            </template>
                        </Toolbar>
                        <DataTable
                            scrollable
                            scrollHeight="520px"
                            size="large"
                            class="w-full h-full flex flex-column align-content-between align-items-between justify-content-between"
                            v-model:selection="selectedEskk"
                            :value="tableData"
                            ref="dt"
                            dataKey="id"
                            :paginator="true"
                            :rows="10"
                            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                            :rowsPerPageOptions="[10, 15, 20]"
                            currentPageReportTemplate="отображено с {first} по {last} запись, из {totalRecords}">
                            <Column selectionMode="single" headerStyle="width: 3rem;"></Column>
                            <Column v-for="col of eskk_list[selectedCategory.id].columns" :key="col.field" :field="col.field" :header="col.name">
                                <template v-if="selectedCategory.id !== 0" #body="slotProps">
                                    {{ col.field === 'value' ? slotProps.data.value + ' ₽': slotProps.data.name }}
                                </template>
                                <template v-else #body="slotProps"> {{ slotProps.data.value }} </template>
                            </Column>
                            <Column headerStyle="width: 1%">
                                <template #body="slotProps">
                                    <Button v-if="selectedCategory.id !== 0" icon="pi pi-pencil" @click="editEskkShow(slotProps.data)" class="p-button-rounded p-button-warning mr-2" />
                                </template>
                            </Column>
                        </DataTable>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <CreateEskkDialog :selectedCategory="selectedCategory" :eskk="eskk"/>
    <EditEskkDialog :selectedCategory="selectedCategory" :eskk="eskk"/>



</template>

<style scoped lang="scss">
.p-focus {
    border-color: transparent !important;
}

</style>