# fastapi-todo-di-example
This repo is an example for a DI application with dogpile.cache and redis.\
It reproduces an issue of using DI to inject a class attribute that is used as a decorator.

## Installation
To start the app run `poetry install`

## Start the app
Go to `todo/modules/task/repositories.py`\
uncomment `list` method in lines 25-33\
comment out `list` method in lines 35-37

Run: `uvicorn todo.main:app --reload`

Navigate to: `http://127.0.0.1:8000/docs#/default/create_task_v1_tasks_post` \
and create a task
Navigate to: `http://127.0.0.1:8000/docs#/default/list_tasks_v1_tasks_get` \
to fetch all tasks

You'll see the first try will print the `cache miss` and any following will retrieve from cache

## Start the app with issue
Run: `uvicorn todo.main:app --reload` 

The result is this exception
```
Traceback (most recent call last):
  File "/Users/nbenyechiel/.pyenv/versions/3.8.12/lib/python3.8/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/Users/nbenyechiel/.pyenv/versions/3.8.12/lib/python3.8/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/nbenyechiel/Library/Caches/pypoetry/virtualenvs/fastapi-todo-sIPcEu6I-py3.8/lib/python3.8/site-packages/uvicorn/subprocess.py", line 76, in subprocess_started
    target(sockets=sockets)
  File "/Users/nbenyechiel/Library/Caches/pypoetry/virtualenvs/fastapi-todo-sIPcEu6I-py3.8/lib/python3.8/site-packages/uvicorn/server.py", line 68, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/Users/nbenyechiel/.pyenv/versions/3.8.12/lib/python3.8/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "uvloop/loop.pyx", line 1501, in uvloop.loop.Loop.run_until_complete
  File "/Users/nbenyechiel/Library/Caches/pypoetry/virtualenvs/fastapi-todo-sIPcEu6I-py3.8/lib/python3.8/site-packages/uvicorn/server.py", line 76, in serve
    config.load()
  File "/Users/nbenyechiel/Library/Caches/pypoetry/virtualenvs/fastapi-todo-sIPcEu6I-py3.8/lib/python3.8/site-packages/uvicorn/config.py", line 456, in load
    self.loaded_app = import_from_string(self.app)
  File "/Users/nbenyechiel/Library/Caches/pypoetry/virtualenvs/fastapi-todo-sIPcEu6I-py3.8/lib/python3.8/site-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/Users/nbenyechiel/.pyenv/versions/3.8.12/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 843, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/nbenyechiel/IdeaProjects/fastapi-todo-di-example/./todo/main.py", line 3, in <module>
    from todo.containers import Container
  File "/Users/nbenyechiel/IdeaProjects/fastapi-todo-di-example/./todo/containers.py", line 5, in <module>
    from todo.modules.task.containers import TaskContainer
  File "/Users/nbenyechiel/IdeaProjects/fastapi-todo-di-example/./todo/modules/task/containers.py", line 3, in <module>
    from todo.modules.task.repositories import InMemoryTaskRepo
  File "/Users/nbenyechiel/IdeaProjects/fastapi-todo-di-example/./todo/modules/task/repositories.py", line 11, in <module>
    class InMemoryTaskRepo(TaskRepoInterface):
  File "/Users/nbenyechiel/IdeaProjects/fastapi-todo-di-example/./todo/modules/task/repositories.py", line 35, in InMemoryTaskRepo
    @cache.cache_on_arguments(expiration_time=60)
AttributeError: 'Provide' object has no attribute 'cache_on_arguments'
```

