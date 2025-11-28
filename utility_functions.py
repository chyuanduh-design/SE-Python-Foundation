def check_status(code):
    if code >= 200 and code < 299:
        message = "Success: Data Ready for Processing."
    elif code >= 300 and code < 399:
        message = "Redirect: Location Change Required."
    elif code >= 400 and code < 499:
        message = "Client Error: Invalid request or Auth Failure" 
    elif code >= 500 :
        message = "Server Error: Retry Mechanism Needed."
    else:
        message = "Unknown Code."
    return message



