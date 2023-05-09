const defaultUrl = "http://localhost:8000/"
let headers = new Headers();

headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');

headers.append('Access-Control-Allow-Origin', 'http://localhost:3000');
headers.append('Access-Control-Allow-Credentials', 'true');

headers.append('GET', 'POST', 'OPTIONS', 'PUT', 'DELETE');

async function post(url = "", data = {}) {
    const response = await fetch(defaultUrl + url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: headers,
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

async function del(url = "", data = {}) {
    const response = await fetch(defaultUrl + url, {
        method: "DELETE",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: headers,
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

async function put(url = "", data = {}) {
    const response = await fetch(defaultUrl + url, {
        method: "PUT",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: headers,
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

const get = (url) => {
    console.log(defaultUrl + url)
    return fetch(defaultUrl + url, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: headers,
        redirect: "follow",
        referrerPolicy: "no-referrer",
    })
        .then((response) => response.json())
}

export {
    post,
    get,
    put,
    del
}