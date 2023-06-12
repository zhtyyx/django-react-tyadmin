import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryAirQualityIndex(params) {
  return request('/api/xadmin/v1/air_quality_index', {
    params,
  });
}
export async function removeAirQualityIndex(params) {
  return request(`/api/xadmin/v1/air_quality_index/${params}`, {
    method: 'DELETE',
  });
}
export async function addAirQualityIndex(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/air_quality_index', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateAirQualityIndex(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/air_quality_index/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryAirQualityIndexVerboseName(params) {
  return request('/api/xadmin/v1/air_quality_index/verbose_name', {
    params,
  });
}
export async function queryAirQualityIndexListDisplay(params) {
  return request('/api/xadmin/v1/air_quality_index/list_display', {
    params,
  });
}
export async function queryAirQualityIndexDisplayOrder(params) {
  return request('/api/xadmin/v1/air_quality_index/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

