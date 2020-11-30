# Demo of FastAPI with Docker and K8s

Just a little sample project to show how to setup a web app using Python, FastAPI, Docker and K8s.

## Development

1. You can build and run with just docker or use docker-compose e.g. `docker-compose up`
2. Vist localhost in your browser

## Deployment

1. Build a docker image and then push it to a repository.
2. There are some example manifests file you can use to create a basic deployment and service. You need to change the image to the image you just pushed. You can use `kubectl apply -f manifests` to apply all manifests to your k8s cluster.
3. To get an url to your app you can use an ingress