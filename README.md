# functions-from-zero
live training - building python functions from zero

[![Python application test with Github Actions](https://github.com/ayalnic/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/ayalnic/functions-from-zero/actions/workflows/main.yml)


### To call Microservice
### Or you can run python main.py, open browser, and add /docs to the end of URL to test program

something like this
```bash
curl -X 'POST' \
  'https://probable-space-eureka-j9gwgjxjjw43vj9-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Run container

something like this
`docker run -p 127.0.0.1:8080:8080 {docker image ls}`

### Invoke POST request

run `invoke.sh`
docker run ... must have been ran first


### Build container

`docker build .`
`docker image ls`
`docker run -p 127.0.0.1:8080:8080 {image id}`