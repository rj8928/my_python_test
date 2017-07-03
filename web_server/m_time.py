import time

# def say_time():
#     return  time.ctime()

def application(env, start_response):
    status = "200 OK"
    headers =[
        ("Content-Type", "Text/plain")
    ]
    start_response(status,headers)
    return time.ctime()