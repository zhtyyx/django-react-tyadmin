[
    {
        name: 'Home',
        path: '/xadmin/index',
        icon: 'dashboard',
        component: './TyAdminBuiltIn/DashBoard'
    },
    {
        path: '/xadmin/',
        redirect: '/xadmin/index',
    },
    {
        name: 'Authentication and Authorization',
        icon: 'BarsOutlined',
        path: '/xadmin/auth',
        routes:
        [
            {
                name: 'permission',
                path: '/xadmin/auth/permission',
                component: './AutoGenPage/PermissionList',
            },
            {
                name: 'group',
                path: '/xadmin/auth/group',
                component: './AutoGenPage/GroupList',
            }
        ]
    },
    {
        name: 'Demo',
        icon: 'BarsOutlined',
        path: '/xadmin/demo',
        routes:
        [
            {
                name: 'user',
                path: '/xadmin/demo/user_profile',
                component: './AutoGenPage/UserProfileList',
            },
            {
                name: 'city',
                path: '/xadmin/demo/city',
                component: './AutoGenPage/CityList',
            },
            {
                name: 'region',
                path: '/xadmin/demo/region',
                component: './AutoGenPage/RegionList',
            },
            {
                name: 'station',
                path: '/xadmin/demo/station',
                component: './AutoGenPage/StationList',
            },
            {
                name: 'air quality concentration',
                path: '/xadmin/demo/air_quality_concentration',
                component: './AutoGenPage/AirQualityConcentrationList',
            },
            {
                name: 'air quality index',
                path: '/xadmin/demo/air_quality_index',
                component: './AutoGenPage/AirQualityIndexList',
            }
        ]
    },
    {
        name: 'TyadminBuiltin',
        icon: 'VideoCamera',
        path: '/xadmin/sys',
        routes:
        [
            {
                name: 'TyAdminLog',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_sys_log',
                component: './TyAdminBuiltIn/TyAdminSysLogList'
            },
            {
                name: 'TyAdminVerify',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_email_verify_record',
                component: './TyAdminBuiltIn/TyAdminEmailVerifyRecordList'
            }
        ]
    },
    {
        name: 'passwordModify',
        path: '/xadmin/account/change_password',
        hideInMenu: true,
        icon: 'dashboard',
        component: './TyAdminBuiltIn/ChangePassword',
    },
    {
        component: './404',
    },
]
