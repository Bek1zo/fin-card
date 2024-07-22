import axios from "axios";

export const requestAxios = axios.create({
    baseURL: import.meta.env.MODE === "development" ? import.meta.env.VITE_APP_BASE_URL_DEV : import.meta.env.VITE_APP_BASE_URL_PROD,
    headers: {
        'Content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*"
    },

})

export function regularGet(path) {
    return requestAxios.get(path)
        .then(res => res)
        .catch((error) => error)
}

export function regularPost (path, payload) {
    return requestAxios.post(path, payload)
        .then(res => res)
        .catch((error) => error)
}

export function regularPut (path, payload) {
    return requestAxios.put(path, payload)
        .then(res => res)
        .catch((error) => error)
}

export function regularDelete (path) {
    return requestAxios.delete(path)
        .then(res => res)
        .catch((error) => error)
}


export function getWithParam (path, config) {
    return requestAxios.get(path, config)
        .then(res => res)
        .catch(error => error)
}

