# Port Scanner

This is a simple Python script that performs a port scan on a given IP address using multithreading. The script scans well-known ports (1-1024) and prints the open ports it finds.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine.
Prerequisites

Python 3.x

## Installing

Clone this repository to your local machine.

    git clone https://github.com/josemlwdf/Python3-Port_Scan.git

## Usage

Open a terminal or command prompt and navigate to the directory where the script is located.


    cd Python3-Port_Scan

Run the script.

    python port_scanner.py

Enter the target IP address when prompted.

## How it Works

The script creates multiple threads, each scanning a single port on the target IP address using a socket connection. If a port is open, the script prints a message indicating that the port is open. The script uses the socket and threading modules in Python to perform the port scan.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

    This script was inspired by various online resources and tutorials on Python network programming.
