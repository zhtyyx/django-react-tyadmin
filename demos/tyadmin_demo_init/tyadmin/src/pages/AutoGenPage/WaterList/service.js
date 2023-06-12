import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryWater(params) {
  return request('/api/xadmin/v1/water', {
    params,
  });
}
export async function removeWater(params) {
  return request(`/api/xadmin/v1/water/${params}`, {
    method: 'DELETE',
  });
}
export async function addWater(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/water', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateWater(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/water/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryWaterVerboseName(params) {
  return request('/api/xadmin/v1/water/verbose_name', {
    params,
  });
}
export async function queryWaterListDisplay(params) {
  return request('/api/xadmin/v1/water/list_display', {
    params,
  });
}
export async function queryWaterDisplayOrder(params) {
  return request('/api/xadmin/v1/water/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

