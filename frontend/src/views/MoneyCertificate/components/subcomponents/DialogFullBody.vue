<script setup>
import DialogPerson from '@/views/MoneyCertificate/components/subcomponents/DialogPerson.vue';
import DialogPnvl from '@/views/MoneyCertificate/components/subcomponents/DialogPnvl.vue';
import DialogPremium from '@/views/MoneyCertificate/components/subcomponents/DialogPremium.vue';
import DialogResult from '@/views/MoneyCertificate/components/subcomponents/DialogResult.vue';
import { ref } from 'vue';

defineProps(['person', 'payment'])

const submitted = ref(false)

</script>

<template>
    <div>
        <div class="flex flex-row">
            <div class="flex flex-column">
                <DialogPerson :person="person" :submitted="submitted"/>
                <DialogPnvl :payment="payment" :submitted="submitted"/>
            </div>
            <DialogPremium :payment="payment" :submitted="submitted"/>
        </div>
        <DialogResult :payment="payment" :submitted="submitted"/>
    </div>
</template>

<style scoped lang="scss">

</style>