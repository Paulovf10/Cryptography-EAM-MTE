# File Transfer Project

This project demonstrates a simple file transfer system using sockets in C.

## Prerequisites

- GCC Compiler
- Unix-like Operating System

## Project Structure

```
file-transfer
├── LICENSE
├── README.md
├── bin
│   ├── cliente       # Client executable
│   └── servidor      # Server executable
├── data
│   ├── output.txt    # Output file received by the client
│   ├── teste1.txt    # Test file 1
│   ├── teste2.txt    # Test file 2
│   ├── teste3.txt    # Test file 3
├── Makefile          # Makefile for building the project
└── src
    ├── cliente.c     # Client source code
    ├── servidor.c    # Server source code
```

## Compilation

This project uses a Makefile to simplify the build process. To compile both the server and client programs, simply run:

```bash
make
```

This will generate the `cliente` and `servidor` executables in the `bin` directory.

## Execution

### Step 1: Run the Server

In the project root directory, start the server with the following command:

```bash
./bin/servidor <port> <buffer_size>
```

Example:

```bash
./bin/servidor 8080 4096
```

### Step 2: Run the Client

In another terminal window, navigate to the project root directory and start the client with the following command:

```bash
./bin/cliente <server_ip> <server_port> <file_name>
```

Example:

```bash
./bin/cliente 127.0.0.1 8080 data/teste1.txt
```

## Example Usage

### Start the Server

```bash
./bin/servidor 8080 4096
```

### Start the Client

```bash
./bin/cliente 127.0.0.1 8080 data/teste1.txt
```

The client will send the specified file to the server, which will process the file and save the received data in `data/output.txt`.

## Authors

- Bárbara Pereira Medeiros Dias
- Pedro Antônio Machado Costa
- Paulo Victor Fernandes Sousa
