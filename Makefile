MODULE_VERSION := $(shell cat wait4localstack/VERSION )

all: lint build test

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0
	rm -rf dist/ tests/resources/sut/wait4localstack-*.tar.gz

build:
	cut -d= -f1 requirements.txt > tests/resources/requirements-latest.txt
	PYTHONPATH=. python3 -m build
	PYTHONPATH=. sphinx-build -b markdown . docs
	gitchangelog > CHANGELOG.md
	cp dist/wait4localstack-*.tar.gz tests/resources/sut/
	docker-compose -f tests/resources/docker-compose.yml build sut

lint:
	bandit -r .
	flake8

push:
	docker-compose -f tests/resources/docker-compose.yml build sut
	DOCKER_IMAGE_TAG=$(MODULE_VERSION) docker-compose -f tests/resources/docker-compose.yml build sut
	docker images
	docker push locp/wait4localstack:$(MODULE_VERSION)
	docker push locp/wait4localstack:latest

test:
	@echo $(MODULE_VERSION)
	DOCKER_IMAGE_TAG=$(MODULE_VERSION) docker-compose -f tests/resources/docker-compose.yml up -d
	PYTHONPATH=.:.. pytest
