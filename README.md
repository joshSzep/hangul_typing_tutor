# Hangul Typing Tutor

A Django based typing tutor web app. Visit [HangulTypingTutor.com](https://HangulTypingTutor.com)

## Setup (for developers)
- Requires Python 3.11 or higher. Recommended to use `pyenv` for this.
- Ensure `poetry` is installed. On OSX with brew you can install with `brew install poetry`
- Ensure `redis` is installed. On OSX with brew you can install with `brew install redis`
- Build the project (install dependencies, migrate the db) with `./local_build.sh`
- In a seperate terminal, run the redis server with the command `redis-server`
- In a seperate terminal, run a celery worker: `poetry run celery -A hangul_tutor worker`
- Run the project's debug/dev server with `./local_run.sh`
- Enjoy!
