from . import SpecValidator

AzureDBFSSpec = {
    'available_os': {
        'CentOS7': {
            'publisher': SpecValidator(type='string', default="OpenLogic"),
            'offer': SpecValidator(type='string', default="CentOS"),
            'sku': SpecValidator(type='string', default="7.7"),
            'ssh_user': SpecValidator(type='string', default='edbadm')
        },
        'CentOS8': {
            'publisher': SpecValidator(type='string', default="OpenLogic"),
            'offer': SpecValidator(type='string', default="CentOS"),
            'sku': SpecValidator(type='string', default="8_1"),
            'ssh_user': SpecValidator(type='string', default='edbadm')
        },
        'RedHat7': {
            'publisher': SpecValidator(type='string', default="RedHat"),
            'offer': SpecValidator(type='string', default="RHEL"),
            'sku': SpecValidator(type='string', default="7.8"),
            'ssh_user': SpecValidator(type='string', default='edbadm')
        },
        'RedHat8': {
            'publisher': SpecValidator(type='string', default="RedHat"),
            'offer': SpecValidator(type='string', default="RHEL"),
            'sku': SpecValidator(type='string', default="8_2"),
            'ssh_user': SpecValidator(type='string', default='edbadm')
        }
    },
    'postgres_server': {
        'sku': SpecValidator(
            type='choice',
            choices=[
                'B_Standard_B1ms', 'B_Standard_B2s', 'B_Standard_D16s_v3',
                'B_Standard_D2s_v3', 'B_Standard_D32s_v3',
                'B_Standard_D48s_v3', 'B_Standard_D4s_v3',
                'B_Standard_D64s_v3', 'B_Standard_D8s_v3',
                'B_Standard_E16s_v3', 'B_Standard_E2s_v3',
                'B_Standard_E32s_v3', 'B_Standard_E48s_v3',
                'B_Standard_E4s_v3', 'B_Standard_E64s_v3', 'B_Standard_E8s_v3'
                'GP_Standard_B1ms', 'GP_Standard_B2s', 'GP_Standard_D16s_v3',
                'GP_Standard_D2s_v3', 'GP_Standard_D32s_v3',
                'GP_Standard_D48s_v3', 'GP_Standard_D4s_v3',
                'GP_Standard_D64s_v3', 'GP_Standard_D8s_v3',
                'GP_Standard_E16s_v3', 'GP_Standard_E2s_v3',
                'GP_Standard_E32s_v3', 'GP_Standard_E48s_v3',
                'GP_Standard_E4s_v3', 'GP_Standard_E64s_v3',
                'GP_Standard_E8s_v3' 'MO_Standard_B1ms', 'MO_Standard_B2s',
                'MO_Standard_D16s_v3', 'MO_Standard_D2s_v3',
                'MO_Standard_D32s_v3', 'MO_Standard_D48s_v3',
                'MO_Standard_D4s_v3', 'MO_Standard_D64s_v3',
                'MO_Standard_D8s_v3', 'MO_Standard_E16s_v3',
                'MO_Standard_E2s_v3', 'MO_Standard_E32s_v3',
                'MO_Standard_E48s_v3', 'MO_Standard_E4s_v3',
                'MO_Standard_E64s_v3', 'MO_Standard_E8s_v3'
            ],
            default='B_Standard_B1ms'
        ),
        'instance_type': SpecValidator(
            type='choice',
            choices=[
                'Standard_B1ms', 'Standard_B2s', 'Standard_D16s_v3',
                'Standard_D2s_v3', 'Standard_D32s_v3', 'Standard_D48s_v3',
                'Standard_D4s_v3', 'Standard_D64s_v3', 'Standard_D8s_v3',
                'Standard_E16s_v3', 'Standard_E2s_v3', 'Standard_E32s_v3',
                'Standard_E48s_v3', 'Standard_E4s_v3', 'Standard_E64s_v3',
                'Standard_E8s_v3'
            ],
            default='Standard_B1ms'
        ),
        'volume': {
            'storage_account_type': SpecValidator(
                type='choice',
                choices=['Premium_LRS', 'StandardSSD_LRS', 'Standard_LRS',
                         'UltraSSD_LRS'],
                default='Standard_LRS'
            ),
            'size': SpecValidator(
                type='integer',
                min=5120,
                max=4194304,
                default=5120
            )
        }
    },
    'pem_server': {
        'instance_type': SpecValidator(
            type='choice',
            choices=[
                'Standard_A1_v2', 'Standard_A2_v2', 'Standard_A4_v2',
                'Standard_A8_v2', 'Standard_A2m_v2', 'Standard_A4m_v2',
                'Standard_A8m_v2'
            ],
            default='Standard_A2_v2'
        ),
        'volume': {
            'storage_account_type': SpecValidator(
                type='choice',
                choices=['Premium_LRS', 'StandardSSD_LRS', 'Standard_LRS',
                         'UltraSSD_LRS'],
                default='Standard_LRS'
            )
        }
    },
    'hammerdb_server': {
        'instance_type': SpecValidator(
            type='choice',
            choices=[
                'Standard_D4ds_v4', 'Standard_D8ds_v4'
            ],
            default='Standard_D4ds_v4'
        ),
        'volume': {
            'storage_account_type': SpecValidator(
                type='choice',
                choices=['Premium_LRS', 'StandardSSD_LRS', 'Standard_LRS',
                         'UltraSSD_LRS'],
                default='Standard_LRS'
            )
        }
    }
}

TPROCC_GUC = {
    'small': {
        'effective_cache_size': '524288',
        'max_wal_size': '51200',
    },
    'medium': {
        'effective_cache_size': '4718592',
        'max_wal_size': '102400',
    },
    'large': {
        'effective_cache_size': '13107200',
        'max_wal_size': '204800',
    },
    'xl': {
        'effective_cache_size': '29884416',
        'max_wal_size': '409600',
    },
}
