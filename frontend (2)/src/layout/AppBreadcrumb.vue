<script setup>
import { useRoute } from 'vue-router';
import { ref, watch } from 'vue';
import { useLayout } from '@/layout/composables/layout';

const route = useRoute();
const breadcrumbRoutes = ref([]);
const { showSidebar } = useLayout();
const searchInput = ref(null);
const searchActive = ref(false);

const setBreadcrumbRoutes = () => {
    if (route.meta.breadcrumb) {
        breadcrumbRoutes.value = route.meta.breadcrumb;

        return;
    }

    breadcrumbRoutes.value = route.fullPath
        .split('/')
        .filter((item) => item !== '')
        .filter((item) => isNaN(Number(item)))
        .map((item) => item.charAt(0).toUpperCase() + item.slice(1));
};

const activateSearch = () => {
    searchActive.value = true;
    setTimeout(() => {
        searchInput.value.$el.focus();
    }, 100);
};
const deactivateSearch = () => {
    searchActive.value = false;
};

const onSidebarButtonClick = () => {
    showSidebar();
};

watch(
    route,
    () => {
        setBreadcrumbRoutes();
    },
    { immediate: true }
);
</script>

<template>
    <div class="layout-breadcrumb flex align-items-center relative h-3rem">
        <nav>
            <ol class="relative z-2">
                <template v-for="(breadcrumbRoute, i) in breadcrumbRoutes" :key="breadcrumbRoute">
                    <li>{{ breadcrumbRoute }}</li>
                    <li v-if="i !== breadcrumbRoutes.length - 1" class="layout-breadcrumb-chevron">/</li>
                </template>
            </ol>
        </nav>
        <ul class="breadcrumb-menu flex align-items-center justify-content-end lg:hidden absolute right-0 top-0 z-4 h-3rem w-screen">
            <li class="w-full m-0 ml-3">
                <div class="breadcrumb-search flex justify-content-end" :class="{ 'breadcrumb-search-active': searchActive }">
                    <Button icon="pi pi-search" class="breadcrumb-searchbutton text-color-secondary flex-shrink-0" type="button" severity="secondary" text rounded @click="activateSearch()"></Button>
                    <div class="search-input-wrapper">
                        <span class="p-input-icon-right">
                            <InputText ref="searchInput" type="text" placeholder="Search" @blur="deactivateSearch()" @keydown.escape="deactivateSearch()" />
                            <i class="pi pi-search"></i>
                        </span>
                    </div>
                </div>
            </li>
            <li class="right-panel-button relative">
                <Button type="button" label="Today" style="width: 6.7rem" icon="pi pi-bookmark" class="layout-rightmenu-button hidden md:block font-normal" @click="onSidebarButtonClick()"></Button>
                <Button type="button" style="width: 3.286rem" icon="pi pi-bookmark" class="layout-rightmenu-button block md:hidden font-normal" @click="onSidebarButtonClick()"></Button>
            </li>
        </ul>
    </div>
</template>
