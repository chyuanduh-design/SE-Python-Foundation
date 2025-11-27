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

Status_message = check_status(504)
                            
print(Status_message)
api_endpoints = ["users","posts","comments"]
for endpoint in api_endpoints:
    print(f"Preparing to connect to: {endpoint}")

mock_api_response = {
    "status": "success",
    "record_count": 42,
    "data": ['Design', 'In Progress', 'Ready to Deploy', 'Completed', 'Archived']
}
for key, value in mock_api_response.items():
    print(f"{key}: {value}")

max_retries = 3
attemp_count = 0
while attemp_count < max_retries:
    print(f"Attempt {attemp_count + 1} of {max_retries}")
    attemp_count += 1
    if attemp_count == 2:
        print("Connection Successful.")
        break

if attemp_count < max_retries:
        print("Loop finished successfully.")
else:
        print("Max retries reached. Exiting loop.")

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result

print("\n--- Test 1 (Zero Division) ---")
print(safe_divide(10, 0))

print("\n--- Test 2 (Value Error) ---")
print(safe_divide(10, 'a'))

print("\n--- Test 3 (Success) ---")
print(safe_divide(10, 2))