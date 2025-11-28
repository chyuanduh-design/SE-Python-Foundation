def process_request(resource, user_id, action='GET'):
    print(f"---Processing {resource} Request---")
    print(f"User ID: {user_id}")
    print(f"Action: {action}")
    print("-" *20)

print("Test 1:Pure Positional (Action defaults to 'GET')")
process_request('posts',101)
print("Test 2: Override Dafult (action becomes 'POST')")
process_request('posts',101,'POST')
print("Test 3: Explicit keyword (Action becomes 'DELETE')")
process_request(resource='comments', user_id=202, action='DELETE')

from utility_functions import check_status
print("/n--- Block 8: Testing Imprted Module ---")

statsu_404 = check_status(404)
print(f"Result from imported module: {statsu_404}")

Status_200 = check_status(200)
print(f"Result from imported module: {Status_200}")

calculate_area = lambda side: side*side 
print("n--- Lambda function test ---")
print(f"Area for side 5: {calculate_area(5)}")

user_ids = [101,105,112,119,120]
processed_ids = [id * 10 for id in user_ids]
print("n--- List Comprehension Test ---")
print(f"Original User IDs: {user_ids}")
print(f"Processed User IDs: {processed_ids}")
