#!/usr/bin/python
import json
if __name__ == '__main__':

    parameters= '{"eviction_policy": "allkeys-lru"}'
    js = f"'{json.dumps(parameters)}'"
    print(js)