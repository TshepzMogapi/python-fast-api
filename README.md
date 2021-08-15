# python-fast-api

# run app

- uvicorn main:app --reload

# build image

docker build -t NAME_OF_IMAGE .

run container

docker run -p 8088:8000 --name NAME_OF_CONATINER NAME_OF_IMAGE
