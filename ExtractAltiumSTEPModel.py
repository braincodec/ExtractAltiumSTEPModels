##########################################################
# Get a 3D model (STEP format) from an Altium PCB project
# Author: @BrainCodec
# Date: June 15, 2016
# WARNING: This is a PoC so you must use it in your own risk.

import zlib

# Open binary file for reading
binaryFile = open("0.dat", "rb")

# Create a file for writing STEP data
stepFile = open("0.step", "wb")

zLibWorker = zlib.decompressobj()

while True:
    data = zLibWorker.unconsumed_tail
    if data == "":
        data = binaryFile.read(4096)
        if data == "":
            break
    inflateData = zLibWorker.decompress(data)
    if inflateData == "":
        break;
    stepFile.write(inflateData)