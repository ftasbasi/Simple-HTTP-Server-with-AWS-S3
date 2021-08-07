# A simple http server with Docker and AWS Services

Technologies : Amazon S3, ECS, ECR, Fargate, Docker

In this application three tasks are implemented as following:

1) GET /picus/list: This endpoint returns objects on the S3 bucket.
2) POST /picus/put: This endpoint saves given JSON data to the S3 bucket and returns the S3 object key.
3) GET /picus/get/{key}: This endpoint returns content of given key from S3.

Task1: Retrieve all objects.

![alt text](https://github.com/ftasbasi/Simple-HTTP-Server-with-AWS-S3/blob/main/img/task1.png?raw=true)


Task2: Save given JSON data to the S3 bucket and return the S3 object key ("furkan.txt").

![alt text](https://github.com/ftasbasi/Simple-HTTP-Server-with-AWS-S3/blob/main/img/task2.png?raw=true)


Task3: Get content of key "sample1.txt" from S3.

![alt text](https://github.com/ftasbasi/Simple-HTTP-Server-with-AWS-S3/blob/main/img/task3.png?raw=true)

