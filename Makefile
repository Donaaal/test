runtest:test
	./test
test:test2.cpp
	g++ $^ -o $@
