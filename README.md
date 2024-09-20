## Tagir Khalilov "Архитектура FastAPI приложения | Шаблон"

В данном уроке мы рассмотрим как построить удобную структуру приложения FastAPI.

### Создаём стартовую структуру проекта:

* Пакет app (здесь будет храниться все наше приложение)
* Папка docker
-1- docker/api (хранение докер-файлов для самого FastAPI)
-2- docker/redis (хранение докер-файлов для сопутствующих сервисов, например это может быть redis)
* Общие docker-файлы
-1- файл dockerignore
-2- файл docker-compose.yaml (в следующем уроке рассмотрим как fastapi и redis обернуть в контейнеры и связать между собой при помощи docker-compose)
* Папки и файлы VCS
-1- файлы ВО venv или poetry
-2- файл .gitignore
-3- файл requirements.txt
