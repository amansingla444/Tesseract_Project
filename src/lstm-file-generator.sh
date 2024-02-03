#!/bin/bash

start_index=1
end_index=281

# Loop through files from 1.tif to 281.tif
for ((i=start_index; i<=end_index; i++)); do
    # Run Tesseract OCR on each file
    tesseract "${i}.tif" "${i}" lstm.train
done