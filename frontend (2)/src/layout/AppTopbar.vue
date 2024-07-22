<script setup>
import { ref } from 'vue';
import { useLayout } from '@/layout/composables/layout';
import AppSidebar from './AppSidebar.vue';
import AppBreadcrumb from './AppBreadcrumb.vue';
import { usePrimeVue } from 'primevue/config';

const $primevue = usePrimeVue();

defineExpose({
    $primevue
});

const { onMenuToggle, showConfigSidebar, showSidebar } = useLayout();
const searchInput = ref(null);
const searchActive = ref(false);

const date = new Date()
let currentTime = ref(date.toLocaleDateString("ru-RU", { // you can use undefined as first argument
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
}));

const onMenuButtonClick = () => {
    onMenuToggle();
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
const onConfigButtonClick = () => {
    showConfigSidebar();
};
const onSidebarButtonClick = () => {
    showSidebar();
};
</script>

<template>
    <div class="layout-topbar">
        <div class="topbar-start">
            <Button ref="menubutton" type="button" class="topbar-menubutton p-link p-trigger" @click="onMenuButtonClick()">
                <i class="pi pi-bars"></i>
            </Button>

            <div class="topbar-breadcrumb">
                <AppBreadcrumb />
            </div>
        </div>
        <div class="layout-topbar-menu-section">
            <AppSidebar />
        </div>
        <div class="topbar-end">
            <ul class="topbar-menu">
<!--                <li class="hidden lg:block">-->
<!--                    <div class="topbar-search" :class="{ 'topbar-search-active': searchActive }">-->
<!--                        <Button icon="pi pi-search" class="topbar-searchbutton text-color-secondary flex-shrink-0" severity="secondary" text rounded type="button" @click="activateSearch()"></Button>-->
<!--                        <div class="search-input-wrapper">-->
<!--                            <span class="p-input-icon-right">-->
<!--                                <InputText ref="searchInput" type="text" placeholder="Search" @blur="deactivateSearch()" @keydown.escape="deactivateSearch()" />-->
<!--                                <i class="pi pi-search"></i>-->
<!--                            </span>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </li>-->

<!--                <li class="profile-item topbar-item">-->
<!--                    <Button type="button" icon="pi pi-bell" class="text-color-secondary flex-shrink-0" severity="secondary" text rounded></Button>-->
<!--                </li>-->

<!--                <li class="profile-item topbar-item">-->
<!--                    <Button type="button" icon="pi pi-comment" class="relative text-color-secondary flex-shrink-0" severity="secondary" text rounded></Button>-->
<!--                </li>-->

                <li class="ml-3">
                    <Button type="button" icon="pi pi-cog" class="text-color-secondary flex-shrink-0" severity="secondary" text rounded @click="onConfigButtonClick()"></Button>
                </li>

                <li ref="profile" class="profile-item topbar-item">
                    <a v-ripple v-styleclass="{ selector: '@next', enterClass: 'hidden', enterActiveClass: 'px-scalein', leaveToClass: 'hidden', leaveActiveClass: 'px-fadeout', hideOnOutsideClick: true }" class="p-ripple cursor-pointer">
                        <img class="border-circle" src="/layout/images/avatar/avatar-m-1.jpg" />
                    </a>

                    <ul class="topbar-menu active-topbar-menu p-4 w-15rem z-5 hidden border-round">
                        <li role="menuitem" class="m-0 mb-3">
                            <a
                                href="#"
                                class="flex align-items-center hover:text-primary-500 transition-duration-200"
                                v-styleclass="{ selector: '@grandparent', enterClass: 'hidden', enterActiveClass: 'px-scalein', leaveToClass: 'hidden', leaveActiveClass: 'px-fadeout', hideOnOutsideClick: true }"
                            >
                                <i class="pi pi-fw pi-lock mr-2"></i>
                                <span>Privacy</span>
                            </a>
                        </li>

                        <li role="menuitem" class="m-0 mb-3">
                            <a
                                href="#"
                                class="flex align-items-center hover:text-primary-500 transition-duration-200"
                                v-styleclass="{ selector: '@grandparent', enterClass: 'hidden', enterActiveClass: 'px-scalein', leaveToClass: 'hidden', leaveActiveClass: 'px-fadeout', hideOnOutsideClick: true }"
                            >
                                <i class="pi pi-fw pi-cog mr-2"></i>
                                <span>Settings</span>
                            </a>
                        </li>
                        <li role="menuitem" class="m-0">
                            <a
                                href="#"
                                class="flex align-items-center hover:text-primary-500 transition-duration-200"
                                v-styleclass="{ selector: '@grandparent', enterClass: 'hidden', enterActiveClass: 'px-scalein', leaveToClass: 'hidden', leaveActiveClass: 'px-fadeout', hideOnOutsideClick: true }"
                            >
                                <i class="pi pi-fw pi-sign-out mr-2"></i>
                                <span>Logout</span>
                            </a>
                        </li>
                    </ul>
                </li>

                <li class="right-panel-button relative hidden lg:block">
                    <Button type="button" style="width: 5.7rem" icon="pi pi-bookmark" class="layout-rightmenu-button hidden md:block font-normal" @click="onSidebarButtonClick()">{{ currentTime }}</Button>
                    <Button type="button" icon="pi pi-bookmark" class="layout-rightmenu-button block md:hidden font-normal" @click="onSidebarButtonClick()"></Button>
                </li>
            </ul>
        </div>
    </div>
</template>
