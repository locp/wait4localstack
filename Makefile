MODULE_VERSION := $(shell cat wait4localstack/VERSION )

all: build test

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0
	rm -rf dist/ tests/resources/sut/wait4localstack-*.tar.gz

build:
	PYTHONPATH=. python3 -m build
	PYTHONPATH=. sphinx-build -b markdown . docs
	gitchangelog > CHANGELOG.md
	cp dist/wait4localstack-*.tar.gz tests/resources/sut/
	docker-compose -f tests/resources/docker-compose.yml build

test:
	@echo $(MODULE_VERSION)
	DOCKER_IMAGE_TAG=$(MODULE_VERSION) docker-compose -f tests/resources/docker-compose.yml up -d
	PYTHONPATH=.:.. pytest
