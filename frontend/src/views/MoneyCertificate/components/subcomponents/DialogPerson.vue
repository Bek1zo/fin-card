<script setup>
defineProps(['person'])
</script>

<template>
    <Fieldset legend="Военнослужащий" class="col-11">
        <div class="flex flex-column formgrid grid">
                                    <span><b>ФИО:</b>
                                        {{ person?.lastname }} {{ person?.firstname }} {{ person?.middlename }}
                                        {{ person?.birthday }} г.р., л/н {{ person?.personal_number }}
                                    </span>
            <span><b>Должность:</b> {{ person?.job_position }} </span>
            <span><b>Подразделение:</b> {{ person?.unit }} </span>
            <span><b>Воинское звание:</b> {{ person?.job_rank_relation?.name }}</span>
            <span><b>Тарифный разряд:</b> {{ person?.tariff_category_relation?.name }} </span>
        </div>
    </Fieldset>
</template>

<style scoped lang="scss">

</style>