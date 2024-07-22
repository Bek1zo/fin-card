<script setup>
import { ref } from 'vue';
import { formatDate } from '@/const/func';

const props = defineProps(['payment', 'submited'])

// При редактирование и сохранение выплаты
const onRowEditSave = (data) => {
    props.payment.premiumList[data.id] = data
    cancelRow(data)
};
const editingRows = ref([]);

// При выборе редактируемой выплаты
const editRow = (value) => {
    editingRows.value.push(value)
}

// При отмене редактирования выплаты
const cancelRow = (value) => {
    editingRows.value.filter((row) => {
        if (row.id === value.id) editingRows.value.splice(editingRows.value.indexOf(row))
    })
}

const disablePaymentRow = (event) => {
    props.payment.premiumList.filter((row) => {
        if (event === row) {
            row.disabled = false
        }
    })
}

const enablePaymentRow = (event) => {
    props.payment.premiumList.filter((row) => {
        if (event === row) row.disabled = true
    })
}

</script>

<template>
    <Fieldset legend="Основания для начисления надбавок и других выплат" class="col-6">
        <div class="formgrid grid">
            <div class="field col-12">
                <DataTable :editingRows="editingRows"
                           :value="payment.premiumList"
                           editMode="row"
                           dataKey="id">
                    <Column field="name" header="Наименование надбавки" style="width: 40%">
                        <template #body="slotProps">
                            <span :class="{'line-through': !slotProps.data.disabled}">{{ slotProps.data.name }}</span>
                        </template>
                        <template #editor="{ data, field }">
                            <InputText v-model="data[field]"/>
                        </template>
                    </Column>
                    <Column field="percentage" header="%">
                        <template #body="slotProps">
                            <span :class="{'line-through': !slotProps.data.disabled}">{{ slotProps.data.percentage }}</span>
                        </template>
                        <template #editor="{ data, field }">
                            <InputText v-model="data[field]"/>
                        </template>
                    </Column>
                    <Column field="order_number" header="Номер приказа">
                        <template #body="slotProps">
                            <span :class="{'line-through': !slotProps.data.disabled}">{{ slotProps.data.order_number }}</span>
                        </template>
                        <template #editor="{ data, field }">
                            <InputText v-model="data[field]"/>
                        </template>
                    </Column>
                    <Column field="order_date" header="Дата приказа">
                        <template #body="slotProps">
                            <span :class="{'line-through': !slotProps.data.disabled}">{{ formatDate(slotProps.data.order_date) }}</span>
                        </template>
                        <template #editor="{ data, field }">
                            <Calendar date-format="dd.mm.yy" v-model="data[field]"/>
                        </template>
                    </Column>
                    <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center">
                        <template #body="slotProps">
                            <Button v-tooltip.bottom="{value: 'Редактировать'}" icon="pi pi-pencil" @click="editRow(slotProps.data)" class="p-button-rounded p-button-warning p-button-text" />
                            <Button v-tooltip.bottom="{value: 'Убрать выплату из карты'}" icon="pi pi-unlock" v-if="!slotProps.data.disabled === false" @click="disablePaymentRow(slotProps.data)" class="p-button-rounded p-button-success p-button-text" />
                            <Button v-tooltip.bottom="{value: 'Включить выплату в карту'}" icon="pi pi-lock" v-else @click="enablePaymentRow(slotProps.data)" class="p-button-rounded p-button-danger p-button-text" />
                        </template>
                        <template #editor="slotProps">
                            <Button v-tooltip.bottom="{value: 'Сохранить'}" icon="pi pi-check" @click="onRowEditSave(slotProps.data)" class="p-button-rounded p-button-success p-button-text" />
                            <Button v-tooltip.bottom="{value: 'Отменить'}" icon="pi pi-times" @click="cancelRow(slotProps.data)" class="p-button-rounded p-button-danger p-button-text" />
                        </template>
                    </Column>
                </DataTable>
            </div>
        </div>
    </Fieldset>
</template>

<style scoped lang="scss">

</style>