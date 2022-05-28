.PHONY: image # Build Docker development image
image:
	scripts/image.sh

.PHONY: shell # Run shell into Docker development container
shell:
	scripts/shell.sh

.PHONY: help # List all available make targets
help:
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) # \(.*\)/\1	\2/'
