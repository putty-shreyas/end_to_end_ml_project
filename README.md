## End to End Machine Learning Project

## Run from Terminal to build docker image:

docker build -t testdockerputty.azurecr.io/endtoendapp:latest .
## docker build -t (azure login server)/(docker image name):latest .

docker login testdockerputty.azurecr.io

docker push testdockerputty.azurecr.io/endtoendapp:latest