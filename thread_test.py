from threading import Thread
import time
import json
import requests


def request():
    while True:
        data = {"username": "zhaoyu",
                "password": "pbkdf2_sha256$36000$0gpJ24Y2mJAM$01LM5Hr7TdNVL1e0E41BKrcfCFsEvm7eRk3wiwmL4qo="}
        rep = requests.post('http://localhost:5000/auth/gettoken/',
                            data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
                            headers={'Content-Type': 'application/json'})
        print(rep.text)
        time.sleep(1)


_threads = []


def init_thread(n=10):
    global _threads
    for i in range(n):
        _thread = Thread(target=request)
        _threads.append(_thread)


if __name__ == '__main__':
    init_thread()
    for t in _threads:
        t.start()

    for t in _threads:
        t.join()