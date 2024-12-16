# E-Commerce Website

This is an e-commerce website built with **Django** and integrated with **PayPal** for secure online payments. The website includes essential features like product browsing, user authentication, shopping cart functionality, order processing, and responsive design.

## Features

- **User Authentication**: 
  - Register, log in, log out, and reset passwords.
- **Product Browsing**: 
  - View product categories and details.
  - Filter products by categories.
- **Shopping Cart**: 
  - Add items to the cart.
  - Adjust quantities of items.
- **Order Processing**: 
  - Place orders, view order history, and track orders.
- **Payment Integration**: 
  - PayPal API integration for secure online payments.
- **Responsive Design**: 
  - Fully responsive layout for various devices.

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django
- **Database**: SQLite (used for development)
- **Payment Gateway**: PayPal APIs

---

## Installation

### Prerequisites

- **Python** 3.10 or higher
- **Git**: For cloning the repository
- **Virtual Environment** (recommended for isolating dependencies)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/bassy1992/e-commerce_alx_final.git
    ```

2. **Navigate into the project directory**:

    ```bash
    cd e-commerce_alx_final
    ```

3. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    - Open your browser and go to `http://127.0.0.1:8000/` to view the e-commerce website in action.

---

## Usage

Once the application is up and running, you can use the following features:

### 1. **Home Page**
   - Browse through various products and explore different categories.

### 2. **Account Management**
   - **Register** a new account or **log in** to an existing one.
   - **Reset your password** if needed.

### 3. **Shopping Cart**
   - Add products to the cart and adjust the quantities.
   - View the cart summary to see the total cost.

### 4. **Checkout & Payment**
   - Proceed to **checkout** after reviewing your cart.
   - Review your **order details** and make payments securely using **PayPal**.

---

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- The e-commerce website was built with **Django** and integrates with **PayPal API** for payments.
- **Bootstrap** is used for styling and responsive design.


## Compile tailwind.css 
```bash
npx tailwindcss -i ./static/css/index.css -o ./static/css/output.css --watch
 
`