SRC=ctest.c
EXEC=test
CC=g++
CFLAGS=-Wall

run: format $(EXEC)
	./$(EXEC)

$(EXEC): $(SRC)
	$(CC) $(CFLAGS) $^ -o $@ -g

format:
	clang-format-15 -i $(SRC)

clean:
	rm -f $(EXEC)

.PHONY:format
