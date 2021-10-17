MODULE_VERSION := $(shell cat wait4localstack/VERSION )

all: build test

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0
	rm -rf dist/ tests/resources/sut/wait4localstack-*.tar.gz

build:
	PYTHONPATH=. python3 -m build
	PYTHONPATH=. sphinx-build -b markdown . docs
	cp dist/wait4localstack-*.tar.gz tests/resources/sut/
	docker-compose -f tests/resources/docker-compose.yml build

publish:
	python3 -m twine upload dist/*
	docker push locp/wait4localstack:$(MODULE_VERSION)
	docker push locp/wait4localstack:latest

test:
	@echo $(MODULE_VERSION)
	DOCKER_IMAGE_TAG=$(MODULE_VERSION) docker-compose -f tests/resources/docker-compose.yml up -d
	PYTHONPATH=.:.. pytest
