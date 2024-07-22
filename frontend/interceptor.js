import { useRootStore } from '@/store/root';

export function initValidationInterceptor(axiosApp, app) {
    const store = useRootStore();

    axiosApp.interceptors.request.use((response)=>{
        store.loadingStatus = true
        return response
    })

    axiosApp.interceptors.response.use((response)=> {
        if (store.loadingStatus) {store.loadingStatus = false}
        if ('messages' in response.data && 'messages' in response.data && response.data.messages !== null) {
            response.data.messages.forEach((message) => {
                app.config.globalProperties.$toast.add(message)
            })
        }
        return response
    },(error)=>{
        error.response.data.messages.forEach((message) => {
            app.config.globalProperties.$toast.add(message)
        })
        return error
    });
}
