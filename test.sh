#!/bin/bash

# Read the CSV file and get the LarkinProduct column
products=$(tail -n +2 larkin.csv | cut -d',' -f1 | tr -d '"')

# Loop over each product
for product in $products; do
    echo "Testing product: $product"
    
    # Test each API endpoint
    echo "Testing /product/$product"
    curl http://localhost:5000/product/$product

    echo "Testing /link/$product"
    curl http://localhost:5000/link/$product

    echo "Testing /markup/$product"
    curl http://localhost:5000/markup/$product

    echo "Testing /archive/$product"
    curl http://localhost:5000/archive/$product

    echo "Testing /real/$product"
    curl http://localhost:5000/real/$product

    echo ""
done