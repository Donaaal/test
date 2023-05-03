runtest:test
	./test
test:test.c
	gcc $^ -o $@
