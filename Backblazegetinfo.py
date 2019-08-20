import base64
import requests

# b2 including id and key
id_and_key = 'ID_AND_KEY_HERE'
id_and_key = str(base64.b64encode(id_and_key.encode()))
# strips the binary key after converting into string
# (Possibly another way to encode without striping 'b')
id_and_key = id_and_key.lstrip('b')

# creating a header with the base64 encoded string.
basic_auth_string = 'Basic ' + id_and_key

headers = {'Authorization': basic_auth_string}

# Requests Get authorize account info
r = requests.get('https://api.backblazeb2.com/b2api/v2/b2_authorize_account', headers=headers)

# Check for successful request, return error if anything other than 200
if r.status_code == 200:
    print('Success, Status code: ' + str(r.status_code))
else:
    print('Request failed, error code: ' + str(r.status_code))

# Parse result into JSON
rj = r.json()

print(rj)

print('Your account ID is: ' + (rj['accountId']))
accountID = (rj['accountId'])

# return authorization token and stores in variable authToken
print('Your authorization token is: ' + (rj['authorizationToken']))
authToken = (rj['authorizationToken'])

# returns downloadUrl and stores in variable downloadUrl
print('Your download URL is: ' + (rj['apiUrl']))
api_url = (rj['apiUrl'])

#CREATE BUCKET
bucketName = 'thisIsANewBucketNow1'
bucketType = 'allPublic'
r = requests.get(url=api_url + '/b2api/v2/b2_create_bucket', headers={'Authorization': authToken}
                 , params={"accountId": accountID, "bucketName": bucketName, "bucketType": bucketType})
rj = r.json()
print(rj)


# LIST BUCKET
#List bucket and store bucket ID into variable: https://www.backblaze.com/b2/docs/b2_list_buckets.html
r = requests.get(headers= 'Authorization: ' + authToken, url= api_url + '/b2api/v2/b2_list_buckets', params = {"accountID": accountID})

rj = r.json()
print(rj)

#LIST FILE NAMES IN BUCKET
##List file names and store into array or dict: https://www.backblaze.com/b2/docs/b2_list_file_names.html

bucket_id = 'BUCKET_ID_HERE'
r = requests.get(url=api_url + '/b2api/v2/b2_list_file_names',
                 headers={'Authorization': authToken},
                 params={'bucketId': bucket_id})
rj = r.json()
print(rj)



##Download file based on name ID: https://www.backblaze.com/b2/docs/b2_download_file_by_name.html
