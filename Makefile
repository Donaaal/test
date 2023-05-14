runtest:test
	./test
test:test.c
	g++ $^ -o $@
