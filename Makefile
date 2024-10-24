# Makefile

.PHONY: all build test prereqs clean

all: build test

prereqs:
	@echo "Installing prerequisites..."
	pip install --upgrade pip
	pip install -r requirements.txt

build:
	@echo "Building project..."
	# Add build commands here if necessary

test:
	@echo "Running tests..."
	python -m unittest discover -s tests

clean:
	@echo "Cleaning up..."
	# Add cleanup commands here
