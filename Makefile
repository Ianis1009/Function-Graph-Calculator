CC = gcc
CFLAGS = -Wall -O2
LIBS = -lm

CFILE = compute.c
EXE = compute

PY = python3
APP = app.py

CSV = data.csv

all: run

build:
	$(CC) $(CFLAGS) $(CFILE) -o $(EXE) $(LIBS)

generate: build
	./$(EXE)

server:
	$(PY) $(APP)

run: generate server

data: generate

web:
	$(PY) $(APP)

clean:
	rm -f $(EXE) $(CSV)