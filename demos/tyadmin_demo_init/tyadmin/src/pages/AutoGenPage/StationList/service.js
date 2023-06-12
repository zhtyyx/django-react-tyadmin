import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryStation(params) {
  return request('/api/xadmin/v1/station', {
    params,
  });
}
export async function removeStation(params) {
  return request(`/api/xadmin/v1/station/${params}`, {
    method: 'DELETE',
  });
}
export async function addStation(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/station', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateStation(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/station/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryStationVerboseName(params) {
  return request('/api/xadmin/v1/station/verbose_name', {
    params,
  });
}
export async function queryStationListDisplay(params) {
  return request('/api/xadmin/v1/station/list_display', {
    params,
  });
}
export async function queryStationDisplayOrder(params) {
  return request('/api/xadmin/v1/station/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

