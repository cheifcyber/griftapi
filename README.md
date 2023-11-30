# GriftAPI

GriftAPI is a Flask application that provides an API for accessing product data.

## New Features

- Product API: Get detailed information about a product.
- Link API: Get the link to a product.
- Markup API: Get the markup for a product.
- Archive API: Get the archive status of a product.
- Real API: Get the real name of a product.

## cURL Examples

Here are some examples of how to use the API with cURL:

\`\`\`bash
curl https://grift.vuln.dad/product/ObeliskOne
curl https://grift.vuln.dad/link/ObeliskOne
curl https://grift.vuln.dad/markup/ObeliskOne
curl https://grift.vuln.dad/archive/ObeliskOne
curl https://grift.vuln.dad/real/ObeliskOne
\`\`\`

## Starting the Container

To start the Docker container, run the following command:

\`\`\`bash
docker run -p 5000:5000 -d griftapi
\`\`\`

This command maps port 5000 of the host to port 5000 of the container and runs the container in detached mode.

Visit `https://grift.vuln.dad` in your web browser to access the application.

## API Endpoints

The Larkin API provides the following endpoints:

- `/product/<name>`: Returns the real product name, real price, and links for the product with the given name. If the product's comment field contains "Not_sold", the comment is also returned.
- `/link/<name>`: Returns the real links for the product with the given name. If the product's comment field contains "Not_sold", the comment is also returned.
- `/markup/<name>`: Returns the markup, percent markup, real price, and Larkin price for the product with the given name. If the product's comment field contains "Not_sold", the comment is also returned.
- `/archive/<name>`: Returns the archive.is link for the product with the given name. If the product's comment field contains "Not_sold", the comment is also returned.
- `/real/<name>`: Returns the real product name for the product with the given name. If the product's comment field contains "Not_sold", the comment is also returned.

Replace `<name>` with the name of the product you want to query.

## Testing

A bash script is provided for testing the API. The script reads the `LarkinProduct` column from the `larkin.csv` file and makes a curl request to each API endpoint for each product. To run the script, use the command `./test.sh`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.