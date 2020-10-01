# Distributed File System

![Interface](https://i.imgur.com/EByMnnR.png)

## Authors

-   Bogdanova Alina
-   Dubina Nikita
-   Sirgalina Rufina

## NS API

| API                                                                     | HowTo Implement implement?                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **GET** `/refresh`                                                      | client-> nameserver                                                                                                                                                                                                                              |
| **GET** `/copy?from=...&to=...` (`from` and `to` - pathes to the files) | [PythonImpl](https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python)                                                                                                                                                          |
| **GET** `/move?from=...&to=...` (`from` and `to` - pathes to the files) | [PythonImpl](https://stackoverflow.com/questions/8858008/how-to-move-a-file)                                                                                                                                                                     |
| **GET** `/mkdir?path=...`                                               | [PythonImpl](https://thispointer.com/how-to-create-a-directory-in-python/)                                                                                                                                                                       |
| **GET** `/rmdir?path=...`                                               | [Here use os.rmdir](https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder)                                                                                                                                                  |
| **GET** `/touch?path=...`()                                             | [If you don't remember](https://stackoverflow.com/questions/12654772/create-empty-file-using-python)                                                                                                                                             |
| **GET** `/rm_file?path=...`                                             | [Here use os.remove](https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder)                                                                                                                                                 |
| **GET** `/download?path=...`                                            | ???                                                                                                                                                                                                                                              |
| **POST** (upload) ????                                                  | ???                                                                                                                                                                                                                                              |
| **GET** `/info?name=...`                                                | [Get file size](https://stackoverflow.com/questions/6591931/getting-file-size-in-python) <br>[Date and time of creation and modification](https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python) |
| **rm_rf** `/clear_all`                                                  | [HOWTO rm non-empty dir](https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty)                                                                                                                           |
