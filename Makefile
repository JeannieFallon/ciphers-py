PY_FILES = `find . -name '*.py'`

.PHONY: image # Build Docker development image
image:
	scripts/image.sh

.PHONY: shell # Run shell into Docker development container
shell:
	scripts/shell.sh

.PHONY: format # Run Black Python code formatter
format:
	black $(PY_FILES)

.PHONY: build # Build ciphers-py executable
build:
	scripts/build.sh

.PHONY: test # Run unit tests
test:
	python -m pytest -v

.PHONY: clean # Remove all build content
clean:
	rm -rf bin build

.PHONY: help # List all available make targets
help:
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) # \(.*\)/\1	\2/'
