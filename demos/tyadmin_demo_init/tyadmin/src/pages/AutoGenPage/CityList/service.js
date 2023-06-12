import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryCity(params) {
  return request('/api/xadmin/v1/city', {
    params,
  });
}
export async function removeCity(params) {
  return request(`/api/xadmin/v1/city/${params}`, {
    method: 'DELETE',
  });
}
export async function addCity(params) {
  let fileFieldList = ["image"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/city', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateCity(params, id) {
  let fileFieldList = ["image"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/city/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryCityVerboseName(params) {
  return request('/api/xadmin/v1/city/verbose_name', {
    params,
  });
}
export async function queryCityListDisplay(params) {
  return request('/api/xadmin/v1/city/list_display', {
    params,
  });
}
export async function queryCityDisplayOrder(params) {
  return request('/api/xadmin/v1/city/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

