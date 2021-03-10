import request from '@/utils/request'

export function getTasks() {
  return request({
    url: 'api/pretreat_tasks/',
    method: 'get'
  })
}

export function getTask(taskId) {
  return request({
    url: `api/pretreat_tasks/${taskId}/`,
    method: 'get'
  })
}

export function createTask(data) {
  return request({
    url: 'api/pretreat_tasks/',
    method: 'post',
    data
  })
}

export function updateTask(taskId, data) {
  return request({
    url: `api/pretreat_tasks/${taskId}/`,
    method: 'put',
    data
  })
}

export function deleteTask(taskId) {
  return request({
    url: `api/pretreat_tasks/${taskId}/`,
    method: 'delete'
  })
}

export function deleteTasks(data) {
  return request({
    url: 'api/pretreat_task/list/',
    method: 'delete',
    data
  })
}
