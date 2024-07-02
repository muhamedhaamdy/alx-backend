#!/usr/bin/env python3
''' basic dict '''
BasicCache = __import__('base_caching').BaseCaching


class BasicCache(BasicCache):
    ''' baisic cache class '''

    def put(self, key, item):
        '''assign to the data the item value for the key key'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key'''
        return self.cache_data.get(key, None)
