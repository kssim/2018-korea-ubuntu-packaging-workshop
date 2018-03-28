EXEC = hello
CC = gcc

CFLAGS = -g -O2 -Wall -Wunused -Wstrict-prototypes
OBJS = hello.o

all: $(OBJS)
	$(CC) -o $(EXEC) *.o

clean:
	rm -f *.o $(EXEC)
