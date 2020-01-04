qa = $(wildcard ./questions_answers/*.csv)

docs/index.html: $(qa)
	python3 ./gen_index.py > docs/index.html

.PHONY: clean
clean:
	rm docs/index.html