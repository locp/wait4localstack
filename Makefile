all: build test

clean:
	docker-compose -f tests/resources/docker-compose.yml down -t 0
	rm -rf dist/ tests/resources/sut/wait4localstack-*.tar.gz

build:
	python3 -m build
	PYTHONPATH=. sphinx-build -b markdown . docs
	cp dist/wait4localstack-*.tar.gz tests/resources/sut/
	docker-compose -f tests/resources/docker-compose.yml build

publish:
	python3 -m twine upload dist/*

test:
	docker-compose -f tests/resources/docker-compose.yml up -d
	PYTHONPATH=.:.. pytest
