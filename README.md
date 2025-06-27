# Python PoCs

- [Basic HTTP Server](./basicserver/) with docker and kubernetes.
- [Unit testing NGINX configuration](./nginxtest/) with crossplane and pytest.

## Debug with VS Code

Bellow snippet allow us debug a module code using VS Code's lunch configuration file. In this we will assume that the project folder is called "myproject" and inside we have another folder called "src" that contains python files and one of them is called "main.py".

`myproject/.vscode/lunch.json`
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: src.main Module",
            "type": "debugpy",
            "request": "launch",
            "module": "src.main",
            "cwd": "${workspaceFolder}",
            "justMyCode": true,
            "env": {
                "PYTHONUNBUFFERED": "1"
            },
            "autoReload": {
                "enable": true
            },
            "args": [
                "--my-python-argument-present"
            ]
        }
    ]
}
```

# Other links

- Command line and environment https://docs.python.org/3/using/cmdline.html
- Built-in Functions https://docs.python.org/3/library/functions.html
