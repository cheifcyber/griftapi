# GriftAPI Documentation

## Endpoints

### `GET /product/{name}`

Returns the real product name, real price, and real links for a given Larkin product. If the comment for the product contains "Not_sold", the comment will also be returned.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the real product name, real price, and real links. If the comment for the product contains "Not_sold", the comment will also be included.

---

### `GET /link/{name}`

Returns the real links for a given Larkin product. If the comment for the product contains "Not_sold", the comment will also be returned.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the real links. If the comment for the product contains "Not_sold", the comment will also be included.

---

### `GET /markup/{name}`

Returns the markup and percent markup for a given Larkin product. If the comment for the product contains "Not_sold", the comment will also be returned.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the markup, percent markup, real price, and Larkin price. If the comment for the product contains "Not_sold", the comment will also be included.

---

### `GET /archive/{name}`

Returns the archive link for a given Larkin product. If the comment for the product contains "Not_sold", the comment will also be returned.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the archive link. If the comment for the product contains "Not_sold", the comment will also be included.

---

### `GET /real/{name}`

Returns the real product name for a given Larkin product. If the comment for the product contains "Not_sold", the comment will also be returned.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the real product name. If the comment for the product contains "Not_sold", the comment will also be included.

---

### `GET /larp_price/{name}`

Returns the Larkin's price for a given Larkin product.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the Larkin's price.

---

### `GET /price/{name}`

Returns the real price for a given Larkin product.

**Parameters:**

- `name`: The name of the Larkin product.

**Response:**

A JSON object containing the real price.