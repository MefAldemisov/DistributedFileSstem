# Distributed File System

![Interface](https://i.imgur.com/EByMnnR.png)

## Authors

-   Alina Bogdanova
-   Nikita Dubina
-   Rufina Sirgalina

## NS API

| Request                                                                 | Response                                              |
| ----------------------------------------------------------------------- | ----------------------------------------------------- |
| **GET** `/refresh`                                                      | JSON with files description                           |
| **GET** `/copy?from=...&to=...` (`from` and `to` - pathes to the files) | JSON with files description                           |
| **GET** `/move?from=...&to=...` (`from` and `to` - pathes to the files) | JSON with files description                           |
| **GET** `/mkdir?path=...`                                               | JSON with files description                           |
| **GET** `/rmdir?path=...`                                               | JSON with files description                           |
| **GET** `/touch?path=...`                                               | JSON with files description                           |
| **GET** `/rm_file?path=...`                                             | JSON with files description                           |
| **GET** `/download?path=...`                                            | File                                                  |
| **POST** (`/upload`): file (`file`) + dir (`path`)                      | JSON with files description                           |
| **GET** `/info?name=...`                                                | **REMOVED** (data passed with fs)                     |
| **rm_rf** `/clear_all`                                                  | JSON with files description(empty array in this case) |

## How to run locally

### Start front

```
cd ./front
docker build -t front .
docker run -it -p 8080:8080 --rm --name dockerize-front front
```

### Way of testing storages

To start Storage Server

```bash
cd ./storage_server
docker build -t storage .
docker run -p 5000:5000 storage
```

To start Name Server

```bash
cd ./name_server
export FLASK_APP=main.py
flask run --host 0.0.0.0 --port 5001
```

Use it to avoid collisions between ports. Also check that `/front/src/requests` should contain this setup:

```
	baseURL: "http://0.0.0.0:5001",
```

```
cd ./name_server
python3 main.py
```

Access to site: `127.0.0.1:8080`
