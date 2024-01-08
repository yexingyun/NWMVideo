def application(environ,start_response):
    status = "200 Ok"
    output = b"Hello wsgi"
    response_headers=[('Content-type','text/plain'),('Content-Length',str(len(output)))]
    start_response(status,response_headers)
    return[output]