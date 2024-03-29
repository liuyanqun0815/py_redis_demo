import yaml
from yacs.config import CfgNode
from django.conf import settings
def init_redis():
    #从配置文件读取redis配置信息
    with open("config/redis.yml","rt")as f:
        configer = CfgNode(yaml.safe_load(f))

    url = configer["redis"]["url"]
    password = configer["redis"]["password"]
    max_connection = configer["redis"]["max_connection"]
    timeout = configer["redis"]["timeout"]
    return {
                "default": {
                    "BACKEND": 'django_redis.cache.RedisCache',
                    "LOCATION": url,
                    "OPTIONS": {
                        "CLIENT_CLASS": "django_redis.client.DefaultClient",
                        "CONNECTION_KWARGS": {"max_connection": max_connection},
                        "PASSWORD": password
                    },
                    "TIMEOUT": timeout
                }
            }

def init_redis_2():
    #从配置文件读取redis配置信息
    with open("config/redis.yml","rt")as f:
        configer = CfgNode(yaml.safe_load(f))

    url = configer["redis"]["url"]
    password = configer["redis"]["password"]
    max_connection = configer["redis"]["max_connection"]
    timeout = configer["redis"]["timeout"]
    setattr(settings, 'CACHES', {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": url,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "CONNECTION_KWARGS": {"max_connection": max_connection},
                "PASSWORD": password
            },
            "TIMEOUT": timeout
        }
    })
