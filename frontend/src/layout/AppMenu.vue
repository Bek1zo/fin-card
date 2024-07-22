<script setup>
import AppMenuItem from './AppMenuItem.vue';
import { onMounted, ref } from 'vue';
import { regularGet } from '@/api/axios';

onMounted(() => {
    getPeriodList()
})

const model = ref([
    {
        label: 'Информация',
        icon: 'pi pi-home',
        items: [
            {
                label: 'О подсистеме',
                icon: 'pi pi-fw pi-question-circle',
                to: '/'
            }
        ]
    },
    {
        label: 'Сотрудники',
        icon: 'pi pi-users',
        items: [
            {
                label: 'Активные',
                icon: 'pi pi-fw pi-user-plus',
                to: '/person_active'
            },
            {
                label: 'Уволенные',
                icon: 'pi pi-fw pi-user-minus',
                to: '/person_dismissed'
            },
        ]
    },
    {
        label: 'Отчеты',
        icon: 'pi pi-calendar',
        items: [
            // {
            //     label: 'Создать отчетный период',
            //     icon: 'pi pi-fw pi-calendar-plus',
            //     to: '/reporting_period/create'
            // },
        ]
    },
    {
        label: 'Справочная информация',
        icon: 'pi pi-inbox',
        to: '/eskk'
    },
]);

// Динамическое меню со списком периодов
const getPeriodList = async () => {
    await regularGet('/eskk/period').then((result) => {
        for (let i in result['data']['data']) {
            model.value[2].items.push({
                label: result['data']['data'][i].value,
                icon: 'pi pi-fw pi-calendar',
                to: '/reporting_period/' + result['data']['data'][i].value
            })
        }
    })
}

</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <AppMenuItem v-if="!item.separator" :item="item" root :index="i" />

            <li v-else class="menu-separator"></li>
        </template>
    </ul>
</template>
