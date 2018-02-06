import logging
from logging.config import dictConfig


config = {
    'version': 1,
    'disable_exiting_loggers': True,

    'formatters': {
        'formatter_1': {
            'format': '%(asctime)s - %(levelname)s - %(name)s -%(message)s'
        },
        'formatter_2': {
            'format': '%(asctime)s %(name)s'
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'formatter_1'
        },
    },

    'loggers': {
        'logger_1': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'logger_2': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    },
}

dictConfig(config)

logger_1 = logging.getLogger('logger_1')
logger_1.info('debug message')
print(
    'hello'
    'world'
)

logger_2 = logging.getLogger('logger_2')
logger_2.info('info message')

logger_1.debug('debug message again')