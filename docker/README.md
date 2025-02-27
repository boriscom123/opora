# opora
Опора Стандарт - тестовое задание

## Python запускается в контейнере docker и доступен локально по ссылке:
`http://127.0.0.1:5000/search?path=${path_fragment}`

### Комапнда для сборки и запуска:
`docker compose up -d --build`

## Ответ предоставляется в JSON Пример:
`[
  {
    "creation_date": "2025-02-24 05:39:49",
    "file_name": ".python_history",
    "file_path": "/root/.python_history",
    "file_size": 0
  },
]`
