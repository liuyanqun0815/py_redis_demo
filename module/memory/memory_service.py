from django.core.cache import cache


def setCache(key: str, value: str):
    cache.set(key, value)


def getCache(key: str):
    return cache.get(key)
