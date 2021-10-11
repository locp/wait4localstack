all: build test

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0

build:
	python3 -m build
	PYTHONPATH=. sphinx-build -b markdown . docs
	cp dist/wait4localstack-*.tar.gz tests/resources/sut/
	docker-compose -f tests/resources/docker-compose.yml build

test:
	docker-compose -f tests/resources/docker-compose.yml up -d
	PYTHONPATH=.:.. pytest
