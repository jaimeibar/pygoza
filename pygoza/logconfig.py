logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '%(asctime)s - %(levelname)s - %(message)s'},
        'debug': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'}
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler',
                    'formatter': 'simple',
                    'level': 'INFO'
                    },
        'file': {'class': 'logging.FileHandler',
                 'filename': 'pygoza.log',
                 'formatter': 'debug',
                 'level': 'DEBUG'
                 }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
