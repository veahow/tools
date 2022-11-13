CC=gcc
CFLAGS=-g -Wall
SOURCES=$(wildcard src/*.c)
INCLUDES=-I./inc -I./pub
LIB_NAMES=-lpthread -lm
LIB_PATH=-L./lib
OBJS=$(patsubst %.c,%.o, $(SOURCES))
TARGET=demo

all: $(TARGET)

$(TARGET):$(OBJS)
	$(CC) $(OBJS) $(LIB_PATH) $(LIB_NAMES) -o $(TARGET)

%.o: %.c
	$(CC) $(INCLUDES) -c $(CFLAGS) $< -o $@

.PHONY:clean
clean:
	rm -rf $(OBJS) $(TARGET)
