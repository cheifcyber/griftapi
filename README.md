# GriftAPI

The GriftAPI is a Flask-based web service that provides access to the information of who makes the products Larkin is reselling for a high markup

## Getting Started

To get the API running on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/cheifcyber/griftapi.git`
2. Navigate to the project directory: `cd griftapi`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Run the Flask application: `python griftapi.py`

The API will be available at `http://localhost:5000`.

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