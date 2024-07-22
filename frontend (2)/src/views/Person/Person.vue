<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount, computed, provide } from 'vue';
import { regularGet } from '@/api/axios';
import { useRootStore } from '@/store/root';
import { MoneyCertificate, Person } from '@/const/const';

import CreatePersonDialog from '@/views/Person/components/CreatePersonDialog.vue';
import EditPersonDialog from '@/views/Person/components/EditPersonDialog.vue';
import CreateArmyDialog from '@/views/Person/components/CreateArmyDialog.vue';
import CreateMoneyCertificateDialog from '@/views/Person/components/CreateMoneyCertificateDialog.vue';
import DeletePersonDialog from '@/views/Person/components/DeletePersonDialog.vue';
import RestorePersonDialog from '@/views/Person/components/RestorePersonDialog.vue';

const store = useRootStore();
const loadingStatus = computed(() => store.loadingStatus)

const props = defineProps(['isActive'])

const page_size = ref(10)
const offset = ref(1)
const totalRecords = ref(0)

const onPage = (event) => {
    page_size.value = event.rows
    offset.value = event.page + 1
    getPersonList()
}

const dt = ref(null);
const filters = ref({});

onMounted(async () => {
    await getPersonList()
})

onBeforeMount(() => {
    initFilters();
});


const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};

const cm = ref();

const contextMenuModel = ref()

const getContextMenuModel = () => {
    if (props.isActive === true) {
        contextMenuModel.value =
            [
                {label: 'Персональная информация', icon: 'pi pi-fw pi-user', command: () => editPersonDialog.value = true },
                {label: 'Информация о военной службе', icon: 'pi pi-fw pi-users', command: () => createArmyDialog.value = true },
                {label: 'Карта денежного довольствия', icon: 'pi pi-fw pi-credit-card', command: () => {
                        createMoneyCertificateDialog.value = true
                        if (selectedPerson.value.status === true || selectedPerson.value.status == null) {
                            regularGet('/card/' + selectedPerson.value.money_certificate_id).then((response) => {
                                if (response?.data?.data) { certificate.value = response?.data?.data }
                            })
                        }
                    }},
                {label: 'Отметить для удаления', icon: 'pi pi-fw pi-times', command: () => deletePersonDialog.value = true }
            ]
    } else {
        contextMenuModel.value = [{label: 'Восстановить военнослужащего', icon: 'pi pi-fw pi-times', command: () => restorePersonDialog.value = true}]
    }
}

const onRowContextMenu = (event) => {
    selectedPerson.value = event.data
    cm.value.show(event.originalEvent);
};

const restorePersonDialog = ref(false)
provide('restorePersonDialog', restorePersonDialog)

const submitted = ref(false);
const changeSubmittedStatus = (status) => { submitted.value = status}
provide('submitted', {submitted, changeSubmittedStatus})

const createPersonDialog = ref(false)
provide('createPersonDialog', createPersonDialog)

const editPersonDialog = ref(false)
provide('editPersonDialog', editPersonDialog)

const createArmyDialog = ref(false)
provide('createArmyDialog', createArmyDialog)

const createMoneyCertificateDialog = ref(false)
provide('createMoneyCertificateDialog', createMoneyCertificateDialog)

const deletePersonDialog = ref(false)
provide('deletePersonDialog', deletePersonDialog)

const certificate = ref(JSON.parse(JSON.stringify(MoneyCertificate)))
const updateCertificate = (value) => { certificate.value = value}
provide('certificate', {certificate, updateCertificate})

const person = ref(Person)
const selectedPerson = ref()
const personList = ref([])
const searchFilter = ref('')

const searchPerson = async (name) => {
    await regularGet('/person/search?name=' + name + '&status=' + props.isActive).then((response) => {personList.value = response.data.data})
}

const getPersonList = async () => {
    await regularGet('/person/list?status=' + props.isActive + '&limit=' + page_size.value + '&offset=' + offset.value).then((response) => {
        searchFilter.value = ''
        personList.value = response.data.data
        totalRecords.value = response.data.count
    })
}

const hideDialog = () => {
    certificate.value = JSON.parse(JSON.stringify(MoneyCertificate))
    createPersonDialog.value = false;
    editPersonDialog.value = false;
    createArmyDialog.value = false;
    createMoneyCertificateDialog.value = false
    deletePersonDialog.value = false
    restorePersonDialog.value = false
    submitted.value = false;
    changeSubmittedStatus(false)
};

</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="card" style="height: 660px;">
                <div class="flex flex-row gap-3 h-full">
                    <div class="flex flex-column align-items-center justify-content-center w-full h-full">
                        <Toolbar class="w-full">
                            <template v-slot:start>
                                <div v-if="props.isActive" class="my-2">
                                    <Button label="Добавить" icon="pi pi-plus" class="mr-2" severity="success" @click="createPersonDialog = true" />
                                    <Button label="Отметить для удаления" icon="pi pi-trash" severity="danger" @click="deletePersonDialog = true" :disabled="!selectedPerson" />
                                </div>
                                <div v-else class="my-2">
                                    <Button label="Восстановить военнослужащего" icon="pi pi-plus" class="mr-2" severity="success" @click="restorePersonDialog = true" />
                                </div>
                            </template>
                            <template v-slot:end>
                                <div class="flex gap-2 justify-content-center align-items-center">
                                    <i class="pi pi-search" />
                                    <AutoComplete v-model="searchFilter" placeholder="Поиск по ФИО" @clear="getPersonList" @complete="searchPerson($event.query)"/>
                                </div>
                            </template>
                        </Toolbar>
                        <ContextMenu ref="cm" class="w-auto" :model="contextMenuModel" @show="getContextMenuModel()" @select="onRowContextMenu()"/>
                        <DataTable
                            :loading="loadingStatus"
                            @page="onPage($event)"
                            lazy :totalRecords="totalRecords"
                            scrollable
                            scrollHeight="520px"
                            ref="dt"
                            size="large"
                            class="w-full h-full flex flex-column align-content-between align-items-between justify-content-between"
                            :value="personList"
                            v-model:selection="selectedPerson"
                            dataKey="id"
                            :paginator="true"
                            :rows="10"
                            :filters="filters"
                            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                            :rowsPerPageOptions="[10, 15, 20]"
                            currentPageReportTemplate="отображено с {first} по {last} запись, из {totalRecords}"
                            v-model:contextMenuSelection="selectedPerson"
                            context-menu
                            @row-contextmenu="onRowContextMenu">
                            <Column selectionMode="single" headerStyle="width: 3rem;"></Column>
                            <Column field="job_rank_relation.name" header="Воинское звание" headerStyle="width:14%; min-width:10rem;">
                                <template #body="slotProps">
                                    {{ slotProps.data.job_rank_relation?.name ? slotProps.data.job_rank_relation.name : 'отсутствует' }}
                                </template>
                            </Column>
                            <Column field="firstname" header="ФИО" sort-field="lastname" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                                <template #body="slotProps">
                                    {{ slotProps.data.lastname.toUpperCase() }}<br>
                                    {{ slotProps.data.firstname }}
                                    {{ slotProps.data.middlename }}<br>
                                </template>
                            </Column>
                            <Column field="personal_number" header="Личный номер" headerStyle="width:14%; min-width:10rem;"></Column>
                            <Column field="job_position" header="Должность" headerStyle="width:14%; min-width:10rem;"></Column>
                            <Column field="unit" header="Подразделение" :sortable="true" headerStyle="width:14%; min-width:8rem;">
                                <template #body="slotProps">
                                    {{ slotProps.data?.unit ? slotProps.data.unit : 'отсутствует' }}
                                </template>
                            </Column>
                            <Column field="arrived_from" header="Прибыл из" :sortable="true" headerStyle="width:14%; min-width:8rem;"></Column>

                            <Column field="status" header="Карточка ДД">
                                <template #body="slotProps">
                                    <span v-if="slotProps.data.status === true" v-tooltip.bottom="'Карта заполнена'" class="bg-green-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-check"></span>
                                    <span v-if="slotProps.data.status === null" v-tooltip.bottom="'Карта заполнена не полностью'" class="bg-yellow-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-info"></span>
                                    <span v-if="slotProps.data.status === false" v-tooltip.bottom="'Карта отсутствует в последнем периоде'" class="bg-red-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-ban"></span>
                                </template>
                            </Column>
                        </DataTable>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <CreatePersonDialog :person="person" @update:dialogStatus="hideDialog()" @getPersonList="getPersonList()"/>
    <EditPersonDialog :person="selectedPerson" @update:dialogStatus="hideDialog()" @getPersonList="getPersonList()"/>
    <CreateArmyDialog :person="selectedPerson" @update:dialogStatus="hideDialog()" @getPersonList="getPersonList()"/>
    <CreateMoneyCertificateDialog :person="selectedPerson" @update:dialogStatus="hideDialog()" @getPersonList="getPersonList()"/>
    <DeletePersonDialog :person="selectedPerson" @update:dialogStatus="hideDialog()" @getPersonList="getPersonList()"/>
    <RestorePersonDialog v-if="props.isActive === false" :person="selectedPerson" @update:dialogStatus="hideDialog()" @getPersonList="getPersonList()"/>
</template>