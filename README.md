# Rainbow Table PoC

This project demonstrates the use of rainbow tables for password cracking.

## Prerequisites

- Kali Linux
- Python 3.x
- RainbowCrack tool

## Steps

1. Install required tools:
 
   sudo apt update
   sudo apt install rainbowcrack

Generate a rainbow table:

sudo rtgen md5 loweralpha-numeric 1 3 0 1000 1000 0

Sort the table:

rtsort *.rt

Create a test hash:

echo -n "sri" | md5sum

Crack the hash:

rcrack . -h <hash>

Automate using the Python script:

python rainbowcrack.py

