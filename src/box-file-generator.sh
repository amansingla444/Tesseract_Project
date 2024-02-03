#!/bin/bash

# Define the range limits
start_index=1
end_index=281

# Loop through files from start_index to end_index
for ((i=start_index; i<=end_index; i++)); do
    # Run Tesseract OCR on each file
    tesseract "${i}.tif" "${i}" --psm 4 -l best/deu lstmbox
done