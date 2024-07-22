import { defineStore } from 'pinia';
import { ref } from 'vue';
// import { useRequestStore } from './request';

export const useRootStore = defineStore('root', () => {

    const loadingStatus = ref(false)

    return { loadingStatus }
})