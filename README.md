# Hangul Typing Tutor

A Django/React based korean typing tutor web app. Visit [HangulTypingTutor.com](https://HangulTypingTutor.com)!

## Why are you making this?

To sharpen my rusty Django skills and to scratch a personal itch: I am currently learning Korean! 🤓

## Why did you do X on the frontend?

My frontend engineers are [Claud](https://claud.ai) and [ChatGPT](https://chatgpt.com). 😉 Ask them! 😆

## Roadmap

- Support basic email/password user accounts 📧
- Support social logins (Google, Facebook, etc) 🔐
- Allow users to track their progress over time 📉
- i18n (internationalization: support more languages than English) 🌐
- Integrate with the OpenAI API to generate new typing challenges dynamically 🤖
- Add static pages explaining how to setup 2-set Korean keyboard on various devices 📖
- Monetize [HangulTypingTutor.com](https://HangulTypingTutor.com) (ads? referral links? TBD) 🤑
- SEO optimizations? 🙈

## Setup for development

- Requires Python 3.11 or higher. Recommended to use `pyenv` for this.
- Ensure `poetry` is installed. On OSX with brew you can install with `brew install poetry`
- Ensure `redis` is installed. On OSX with brew you can install with `brew install redis`
- Build the project (install dependencies, migrate the db) with `./local_build.sh`
- In a seperate terminal, run the redis server with the command `redis-server`
- In a seperate terminal, run a celery worker: `poetry run celery -A hangul_tutor worker`
- Run the project's debug/dev server with `./local_run.sh`
- Enjoy!
