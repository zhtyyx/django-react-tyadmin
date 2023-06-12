import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryRegion(params) {
  return request('/api/xadmin/v1/region', {
    params,
  });
}
export async function removeRegion(params) {
  return request(`/api/xadmin/v1/region/${params}`, {
    method: 'DELETE',
  });
}
export async function addRegion(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/region', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateRegion(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/region/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryRegionVerboseName(params) {
  return request('/api/xadmin/v1/region/verbose_name', {
    params,
  });
}
export async function queryRegionListDisplay(params) {
  return request('/api/xadmin/v1/region/list_display', {
    params,
  });
}
export async function queryRegionDisplayOrder(params) {
  return request('/api/xadmin/v1/region/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

