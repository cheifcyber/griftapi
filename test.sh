#!/bin/bash

# Read the CSV file and get the LarkinProduct column
products=$(tail -n +2 larkin.csv | cut -d',' -f1 | tr -d '"')

# Loop over each product
for product in $products; do
    echo "Testing product: $product"
    
    # Test each API endpoint
    echo "Testing /product/$product"
    curl http://127.0.0.1:80/product/$product

    echo "Testing /link/$product"
    curl http://127.0.0.1:80/link/$product

    echo "Testing /markup/$product"
    curl http://127.0.0.1:80/markup/$product

    echo "Testing /archive/$product"
    curl http://127.0.0.1:80/archive/$product

    echo "Testing /real/$product"
    curl http://127.0.0.1:80/real/$product

    echo ""
done