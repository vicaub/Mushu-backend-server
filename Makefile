run: build
	docker run -it --rm -p 5000:5000 mushu-back:latest

run-service: build
	docker run --rm -p 5000:5000 mushu-back:latest

build:
	docker build . -t mushu-back:latest --target production

build-test:
	docker build . -t mushu-back:test-latest --target test

test: build-test
	docker run -it --rm mushu-back:test-latest

sh:
	docker run -it --rm mushu-back:latest bash

sh-test:
	docker run -it --rm mushu-back:test-latest bash

local-setup:
	pip install --user pipenv
	pipenv install

mypy:
	pipenv run bash -c "MYPYPATH=$$PYTHONPATH mypy ."

black:
	black -l 120 .
