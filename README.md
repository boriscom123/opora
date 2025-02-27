# opora

Опора Стандарт - тестовое задание

## Создание MCP сервиса для поиска файлов

Запуск сервиса:

```bash
python mcp_server.py
```

Пример ответа от сервера (сервер доступен на порту 8080):

```json
[
    {
        "name": "example.txt",
        "path": "./documents/example.txt",
        "size": 1024,
        "creation_time": "2023-10-01 12:34:56"
    },
    {
        "name": "example_backup.txt",
        "path": "./backups/example_backup.txt",
        "size": 2048,
        "creation_time": "2023-10-02 14:20:30"
    }
]
```

Команда для сазуска скрипта Cline:

```bash
cline mcp find example
```

Пример задачи для выполнения Cline

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Find files with Cline",
            "type": "shell",
            "command": "cline",
            "args": ["mcp", "find", "example"],
                "group": {
                        "kind": "build",
                        "isDefault": true
                    },
                "problemMatcher": []
        }
    ]
}
```
