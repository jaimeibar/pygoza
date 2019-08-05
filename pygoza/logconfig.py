logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '%(asctime)s - %(levelname)s - %(message)s'},
        'debug': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'}
    },
    'handlers': {
        'file': {'class': 'logging.handlers.RotatingFileHandler',
                 'filename': 'pygoza.log',
                 'maxBytes': 5000000,
                 'backupCount': 5,
                 'formatter': 'debug',
                 'level': 'DEBUG'
                 }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}
