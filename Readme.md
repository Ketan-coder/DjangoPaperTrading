# Paper Trading Web Application

The Paper Trading Web Application is a Django-based platform that simulates stock and options trading in a risk-free environment. Users can register, receive an initial virtual balance, and start buying and selling stocks and options. The app provides real-time market data for the Nifty 50, Bank Nifty, and Fin Nifty indexes, enabling users to practice their trading strategies without risking real money.

## Features

- User Authentication: Users can create accounts, log in, and log out of the platform.
- Virtual Balance: Each user is provided with an initial virtual balance to trade with.
- Stock and Options Trading: Users can buy and sell stocks and options based on real-time data.
- Transaction History: All user transactions are recorded, and users can review their trading history.
- Portfolio Management: Users can track their holdings and see the current value of their portfolio.
- Real-Time Market Data: Real-time data for Nifty 50, Bank Nifty, and Fin Nifty is fetched to reflect market conditions accurately.

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Ketan-coder/DjangoPaperTrading.git
cd DjangoPaperTrading
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run database migrations:

```bash
python manage.py migrate
```

4. Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the app in your web browser:

   - Admin Dashboard: `http://localhost:8000/admin/`
   - Paper Trading App: `http://localhost:8000/`

## Usage

1. Create an account or log in with your credentials.
2. Explore the option chain for Nifty 50, Bank Nifty, and Fin Nifty.
3. Use the virtual balance to buy and sell stocks and options.
4. Monitor your portfolio performance and transaction history.
5. Use the admin dashboard to manage user data and perform administrative tasks.

## Technologies Used

- Django: Backend framework for web application development.
- nsepython: Python module to fetch real-time market data from NSE.
- HTML/CSS & React: Frontend design and styling.
- SQLite: Database to store user data and transactions.

## Contributing

Contributions are welcome! If you have any suggestions, or feature requests, or find any issues, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

- Your Ketan Vishwakarma, Siddhesh Yadav
- Email: ketanv288@gmail.com
- Website: https://codingfox.pythonanywhere.com/about/
