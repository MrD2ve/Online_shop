# Online_Shop  
# 🛍️ Django E-Commerce Platform

A powerful Django-based e-commerce platform packed with essential features like **product catalogs**, **shopping carts**, **discounts**, **credit card payments**, and more.

This project demonstrates how to build a modern, scalable online shop using Django along with tools like **Redis**, **Celery**, and **RabbitMQ** for real-time functionality and asynchronous processing.

---

## ✨ Features

- 📦 Product catalog management  
- 🛒 Session-based shopping cart  
- 🏷️ Discount code support  
- 💳 Stripe credit card payment integration  
- 🧾 PDF invoice generation  
- 📈 Redis-powered image view counter  
- ⚙️ Custom context processors  
- 📬 Asynchronous notifications via Celery  
- 🌸 Task monitoring with Flower  
- 🧠 Smart recommendation engine  
- 🌍 Internationalization (i18n) support  

---

## 🚀 Getting Started

Follow these steps to get the project running locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/django-online-shop.git
cd django-online-shop

# 2️⃣ Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Start Redis and RabbitMQ
# Make sure Redis and RabbitMQ servers are running

# 5️⃣ Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Create a superuser (optional)
python manage.py createsuperuser

# 7️⃣ Start Celery worker and Flower (in separate terminals)
celery -A config worker -l info
celery -A config flower  # Opens Flower at http://localhost:5555

# 8️⃣ Run the development server
python manage.py runserver

```

---

## 📄 License

This project is licensed under the MIT License.
