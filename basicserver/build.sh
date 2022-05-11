#!/bin/bash
CONTAINER_NAME="python3-basicserver"
CONTAINER_TAG="1.0"
GITHUB_REPO="emmerson"


docker build --tag "${CONTAINER_NAME}:${CONTAINER_TAG}"  --no-cache=true . 

echo "Build finished, now you can run your image locally using: docker run  -p 8080:8080 -dit ${CONTAINER_NAME}:${CONTAINER_TAG}"

echo "-------------------"
IMAGE_ID=$(docker images -q "${CONTAINER_NAME}:${CONTAINER_TAG}") 
echo "IMAGE_ID:$IMAGE_ID"
echo "docker tag ${IMAGE_ID} ${GITHUB_REPO}/${CONTAINER_NAME}:${CONTAINER_TAG}"
echo "docker push ${GITHUB_REPO}/${CONTAINER_NAME}:${CONTAINER_TAG}"
echo "-------------------"
echo ""