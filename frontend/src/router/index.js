import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

const routes = [
    {
        path: '/',
        component: AppLayout,
        children: [
            {
                path: '/',
                name: 'about',
                meta: { breadcrumb: ['Информация о системе'] },
                component: () => import('@/views/About.vue')
            },
            {
                path: '/person_active',
                name: 'person_active',
                meta: { breadcrumb: ['Список активных военнослужащих'] },
                component: () => import('@/views/Person/PersonActive.vue')
            },
            {
                path: '/person_dismissed',
                name: 'person_dismissed',
                meta: { breadcrumb: ['Список уволенных военнослужащих'] },
                component: () => import('@/views/Person/PersonDismissed.vue')
            },
            {
                path: '/eskk',
                name: 'eskk',
                meta: { breadcrumb: ['Классификаторы'] },
                component: () => import('@/views/Eskk/Eskk.vue')
            },
            {
                path: '/reporting_period/:periodId',
                name: 'reporting_period',
                meta: { breadcrumb: ['Отчетный период'] },
                component: () => import('@/views/MoneyCertificate/MoneyCertificate.vue')
            },
        ]
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior() {
        return { left: 0, top: 0 };
    }
});

export default router;
