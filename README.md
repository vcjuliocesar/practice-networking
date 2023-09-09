# practice-networking
Welcome to the practice-networking repository! This is a simple guide to help you get started with setting up and running the practice-networking project.

## Getting Started

Follow these steps to set up and run the project on your local machine:

**Clone the repository:**
```sh 
git clone git@github.com:vcjuliocesar/pynotes-api.git
```

**Create a Virtual Environment:**
```sh
 python3 -m venv env
```
**Activate the Virtual Environment:**
On macOS/Linux:
```sh
 source env/bin/activate
```
On Windows:
```sh
 .\env\Scripts\activate
```
## Docker
if you prefer to use docker follow these steps, it is important that you have docker installed on your computer
```sh
docker build -t mongoapp .
```
## Create Network
```sh
docker network create --attachable juliuznet
```

## Create mongodb container
```sh
docker run -d --name mdb mongo
```
## Connect network with database
 ```sh
docker network connect juliuznet mdb
```

## Run container
 ```sh
docker run -d --name mapp -p 5000:5000 --env MONGO_URL=mongodb://mdb:27017/test-database mongoapp
```

## Connect network with app
 ```sh
docker network connect juliuznet mapp
```
Once the project is up and running, you can access it through your browser or API client.