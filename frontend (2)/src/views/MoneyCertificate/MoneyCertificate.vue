<script setup>
import { computed, onMounted, ref, watch, provide } from 'vue';
import { regularGet } from '@/api/axios';
import { useRouter } from 'vue-router';
import { MoneyCertificate, rows_per_page } from '@/const/const';
import { useRootStore } from '@/store/root';

import PaymentDialog from '@/views/MoneyCertificate/components/PaymentDialog.vue';
import CertificateEditDialog from '@/views/MoneyCertificate/components/CertificateEditDialog.vue';
import CertificateNewDialog from '@/views/MoneyCertificate/components/CertificateNewDialog.vue';

const store = useRootStore()
const router = useRouter()
const loadingStatus = computed(() => (store.loadingStatus))

const page_size = ref(10)
const offset = ref(1)
const totalRecords = ref(0)
const searchFilter = ref()

const moneyCertificateList = ref([])
const moneyCertificate = ref(MoneyCertificate)
const certificateId = ref(null)

const submitted = ref(false)
const changeSubmittedStatus = (status) => { submitted.value = status}
provide('submitted', { submitted, changeSubmittedStatus })

const period = computed(() => router.currentRoute.value.params.periodId)
provide('period', period)

const selectedCertificate = ref()
provide('certificate', selectedCertificate)

const createMoneyCertificateDialog = ref(false)
provide('createMoneyCertificateDialog', createMoneyCertificateDialog)

const paymentMoneyCertificateDialog = ref(false)
provide('paymentMoneyCertificateDialog', paymentMoneyCertificateDialog)

const editMoneyCertificateDialog = ref(false)
provide('editMoneyCertificateDialog', editMoneyCertificateDialog)

// Старт

onMounted( () => {
    getMoneyCertificateList()
})

// Загрузка новых сертификатов при переходе в другой период
watch(router.currentRoute, () => {if (router.currentRoute.value.name === 'reporting_period') getMoneyCertificateList()})

// Контекстное меню

const cm = ref();
const contextMenuModel = ref(
    [
        {label: 'Карта денежного довольствия', icon: 'pi pi-fw pi-credit-card', command: () => {
                regularGet('/card/' + selectedCertificate.value.money_certificate_id).then((response) => {
                    if (response?.data?.data) {
                        moneyCertificate.value = response?.data?.data
                    }
                    editMoneyCertificateDialog.value = true
                })
            }},
        {label: 'Выплаты по карте денежного довольствия', icon: 'pi pi-fw pi-dollar', command: () => {
                certificateId.value = selectedCertificate.value.id
                paymentMoneyCertificateDialog.value = true;
            }},
        {label: 'Загрузить карту денежного довольствия', icon: 'pi pi-fw pi-download', command: () => {
                let url = import.meta.env.MODE === "development" ? import.meta.env.VITE_APP_BASE_URL_DEV : import.meta.env.VITE_APP_BASE_URL_PROD
                url +='/card/file/' + selectedCertificate.value.id
                let link = document.createElement("a");
                link.href=url;
                link.click()
                link.remove()
            }},
    ]
)
const onRowContextMenu = (event) => {
    cm.value.show(event.originalEvent);
};

// Получение списка сертификатов
const getMoneyCertificateList = async () => {
    await regularGet('/card/list?period=' + period.value + '&limit=' + page_size.value + '&offset=' + offset.value).then((response) => {
        hideDialog()
        moneyCertificateList.value = response['data']['data']
        totalRecords.value = response['data']['total']
    })
}

// Глобальный поиск по всем картам ДД
const searchMoneyCertificate = async (name) => {
    await regularGet('/card/relation/search?name=' + name + '&period=' + period.value).then((response) => {moneyCertificateList.value = response.data.data})
}

// Пагинатор
const onPage = (event) => {
    page_size.value = event.rows
    offset.value = event.page + 1
    getMoneyCertificateList()
}

// Скрытие всех диалогов
const hideDialog = () => {
    changeSubmittedStatus(false)

    moneyCertificate.value = JSON.parse(JSON.stringify(MoneyCertificate))

    createMoneyCertificateDialog.value = false
    editMoneyCertificateDialog.value = false
    paymentMoneyCertificateDialog.value = false
}
</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="card" style="height: 660px;">
                <div class="flex flex-row gap-3 h-full">
                    <div class="flex flex-column align-items-center justify-content-center w-full h-full">
                        <Toolbar class="w-full">
                            <template v-slot:start>
                                <div class="my-2">
                                    <Button label="Создать карту денежного довольствия" icon="pi pi-plus" class="mr-2" severity="success" @click="createMoneyCertificateDialog = true" />
                                </div>
                            </template>
                            <template v-slot:end>
                                <div class="flex gap-2 justify-content-center align-items-center">
                                    <i class="pi pi-search" />
                                    <AutoComplete v-model="searchFilter" placeholder="Поиск по ФИО" @clear="getMoneyCertificateList" @complete="searchMoneyCertificate($event.query)"/>
                                </div>
                           </template>
                        </Toolbar>
                        <ContextMenu ref="cm" class="w-auto" :model="contextMenuModel" @select="onRowContextMenu"/>
                        <DataTable
                            :loading="loadingStatus"
                            @page="onPage($event)"
                            scrollable
                            scrollHeight="520px"
                            ref="dt"
                            size="large"
                            class="w-full h-full flex flex-column align-content-between align-items-between justify-content-between"
                            :value="moneyCertificateList"
                            v-model:selection="selectedCertificate"
                            dataKey="id"
                            lazy :totalRecords="totalRecords"
                            :paginator="true"
                            :rows="page_size"
                            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                            :rowsPerPageOptions="rows_per_page"
                            currentPageReportTemplate="отображено с {first} по {last} запись, из {totalRecords}"
                            v-model:contextMenuSelection="selectedCertificate"
                            context-menu
                            @row-contextmenu="onRowContextMenu">
                            <Column selectionMode="single" headerStyle="width: 3rem;"></Column>
                            <Column field="job_rank" header="Воинское звание" headerStyle="width:14%; min-width:10rem;"></Column>
                            <Column field="firstname" header="ФИО" sort-field="lastname" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                                <template #body="slotProps">
                                    {{ slotProps.data.lastname.toUpperCase() }}<br>
                                    {{ slotProps.data.firstname }}
                                    {{ slotProps.data.middlename }}<br>
                                </template>
                            </Column>
                            <Column field="certificate_number" header="Номер карты ДД" headerStyle="width:14%; min-width:10rem;"></Column>
                            <Column field="certificate_date" header="От какого числа" headerStyle="width:14%; min-width:10rem;"></Column>
                            <Column field="certificate_expire_date" header="Действителен по" headerStyle="width:14%; min-width:8rem;"></Column>
                            <Column field="card_author" header="Составитель" headerStyle="width:14%; min-width:8rem;"></Column>
                            <Column field="card_inspector" header="Проверяющий" headerStyle="width:14%; min-width:7rem;"></Column>
                            <Column field="year_first" header="Первый год" headerStyle="width:14%; min-width:7rem;" class="flex justify-content-center">
                                <template #body="slotProps">
                                    <span v-if="slotProps.data.year_first_status === true" v-tooltip="'Выплата проверена'" class="bg-green-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-check"></span>
                                    <span v-if="slotProps.data.year_first_status === false" v-tooltip="'Заполнены не все данные'" class="bg-red-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-ban"></span>
                                    <span v-if="slotProps.data.year_first_status === null" v-tooltip="'Выплата не проверена'" class="bg-yellow-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-info"></span>
                                </template>
                            </Column>
                            <Column field="year_second" header="Второй год" headerStyle="width:14%; min-width:8rem;">
                                <template #body="slotProps">
                                    <span v-if="slotProps.data.year_second_status === true" v-tooltip="'Выплата проверена'" class="bg-green-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-check"></span>
                                    <span v-if="slotProps.data.year_second_status === false" v-tooltip="'Заполнены не все данные'" class="bg-red-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-ban"></span>
                                    <span v-if="slotProps.data.year_second_status === null" v-tooltip="'Выплата не проверена'" class="bg-yellow-600 border-circle w-2rem h-2rem flex align-items-center justify-content-center pi pi-info"></span>
                                </template>
                            </Column>
                        </DataTable>
                    </div>
                </div>
            </div>
        </div>
    </div>




    <CertificateNewDialog :certificate="moneyCertificate" :period="period" @getMoneyCertificateList="getMoneyCertificateList" @update:dialogStatus="hideDialog()"/>
    <CertificateEditDialog :certificate="moneyCertificate" @getMoneyCertificateList="getMoneyCertificateList" @update:dialogStatus="hideDialog()"/>
    <PaymentDialog :period="period" :certificateId="certificateId" :dialogStatus="paymentMoneyCertificateDialog" @update:dialogStatus="hideDialog()"/>

</template>

<style lang="scss">



</style>