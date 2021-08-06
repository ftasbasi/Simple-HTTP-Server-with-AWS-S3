# A simple application containing following HTTP endpoints. Using AWS S3 for storage.

- GET /picus/list: This endpoint will return objects on the S3 bucket created in step #2.
- POST /picus/put: This endpoint will save given JSON data to the S3 bucket and returns the S3 object key.
- GET /picus/get/{key}: This endpoint will return content of given key from S3.
