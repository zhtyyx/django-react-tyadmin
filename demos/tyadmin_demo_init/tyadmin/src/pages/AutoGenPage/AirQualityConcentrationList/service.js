import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryAirQualityConcentration(params) {
  return request('/api/xadmin/v1/air_quality_concentration', {
    params,
  });
}
export async function removeAirQualityConcentration(params) {
  return request(`/api/xadmin/v1/air_quality_concentration/${params}`, {
    method: 'DELETE',
  });
}
export async function addAirQualityConcentration(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/air_quality_concentration', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateAirQualityConcentration(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/air_quality_concentration/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryAirQualityConcentrationVerboseName(params) {
  return request('/api/xadmin/v1/air_quality_concentration/verbose_name', {
    params,
  });
}
export async function queryAirQualityConcentrationListDisplay(params) {
  return request('/api/xadmin/v1/air_quality_concentration/list_display', {
    params,
  });
}
export async function queryAirQualityConcentrationDisplayOrder(params) {
  return request('/api/xadmin/v1/air_quality_concentration/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

