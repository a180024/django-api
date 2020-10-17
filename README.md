# Description
> Sample project to accept file uploads and calculate sensitivity score on a cron schedule based on keywords 

1. Authentication
- Handled by Djoser 
- JWT expires in 15min

2. API endpoints for files
- CRUD operations are handled in the core app
- The update endpoint will allow user to replace the current file
- A user will only be able to access the files he has uploaded

3. Models 
- File model contains a flag signalling if the sensitivity score has been updated
- The flag is false by default and will be set to True each time the beat scheduler runs

4. Celery
- Cronjob set to every 30 secs for the ease of this project
- Uses Redis as a message broker

# Set Up
```
$ cd restapi 
$ docker-compose up
```

# Usage

**Authentication Endpoints**

1. Create User
```
$ curl -X POST http://127.0.0.1:8000/auth/users/ --data 'username=testuser&password=alpine12'
```

2. Create JWT (15 minutes expiry)
```
$ TOKEN=$(curl -X POST http://127.0.0.1:8000/auth/jwt/create/ --data 'username=testuser&password=alpine12'| jq -r '.access')
$ REFRESH_TOKEN=$(curl -X POST http://127.0.0.1:8000/auth/jwt/create/ --data 'username=testuser&password=alpine12'| jq -r '.refresh')
$ echo $TOKEN
$ echo $REFRESH_TOKEN
```

3. Refresh JWT
```
$ TOKEN=$(CURL -X POST http://127.0.0.1:8000/auth/jwt/refresh/ -data "refresh=${REFRESH_TOKEN}" | jq -r '.access')
```

**API Endpoints**

1. Upload File
```
$ curl -F "file=@./testfiles/example.txt" -H "Authorization: JWT ${TOKEN}" -H "Content-Type: multipart/form-data" http://127.0.0.1:8000/api/files/upload/
```

2. List Files 
```
$ curl -X GET -H "Authorization: JWT ${TOKEN}" http://127.0.0.1:8000/api/files/ | jq
```

3. File Detail 
```
$ curl -X GET -H "Authorization: JWT ${TOKEN}" http://127.0.0.1:8000/api/files/<pk>/ | jq
```

4. Update File
```
$ curl -X PUT -F "file=@./testfiles/example2.txt -H "Authorization: JWT ${TOKEN}" -H "Content-Type: multipart/form-data" http://127.0.0.1:8000/api/files/<pk>/update/
```

5. Delete File
```
$ curl -X DELETE -H "Authorization: JWT ${TOKEN}" http://127.0.0.1:8000/api/files/<pk>/delete/
```



