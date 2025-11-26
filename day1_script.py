name = "Chyuan Duh"
print(f"SE Learning Initiated by {name}")
print("current time is 8:00 AM")
api_endpoints = ["users","posts","comments"]
sample_data = {"status": "ready", "version":1.0}
print(f"Target endpoints: {api_endpoints[0]}")
Project_status = ["Design","In Progress","QA","Ready to Deploy","Completed"]
print(f"status 4:{Project_status[3]}")
active_status = Project_status[:3]
print(f"Active statuses: {active_status}")
recent_status = Project_status[-2:]
print(f"Last Two: {recent_status}")
Project_status.append("Archived")
print(f"list length after append: {len(Project_status)}")
Project_status.remove("QA")
print(f"list after removal: {Project_status}")
mock_api_response = {
    "status": "success",
    "record_count": 42,
    "data": ['Design', 'In Progress', 'Ready to Deploy', 'Completed', 'Archived']
}
print(f"Record Count: {mock_api_response['record_count']}")
print(f"status: {mock_api_response['status']}")

data_list = mock_api_response["data"]
last_status = data_list[-1]
print(f"Last Process Status: {last_status}")

mock_api_response['record_count'] =45
print(f"New Count: {mock_api_response.get('record_count')}")

if "record_count" in mock_api_response:
    print("Record Count key exists.")
if "auth_token" not in mock_api_response:
    print("Security Check: Auth token not found in payload (Good).")
