.PHONY: image # Build Docker development image
image:
	scripts/image.sh

.PHONY: shell # Run shell into Docker development container
shell:
	scripts/shell.sh

.PHONY: build # Build ciphers-py executable
build:
	scripts/build.sh

.PHONY: clean # Remove all build content
clean:
	rm -rf bin build

.PHONY: help # List all available make targets
help:
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) # \(.*\)/\1	\2/'
