const apiHost = 'http://127.0.0.1:8000'

const ToDoListApis = {
    ToDoListDetailUrl: apiHost + '/todolist/#{id}/',
    ToDoListUrl: apiHost + '/todolist/',
}

export {
    ToDoListApis
}