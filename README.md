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
- 📬 Asynchronous notifications via Celery  
- 🌸 Task monitoring with Flower  
- 🧠 Smart recommendation engine
- ⚙️ RESTful API
- 🔓 JWT authentication

---

## 🚀 Getting Started

Follow these steps to get the project running locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/django-online-shop.git

# 2️⃣ Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Install Docker Desktop, Stripe, 
- [Download Docker](https://www.docker.com/products/docker-desktop/)
- [Download Stripe](https://github.com/stripe/stripe-cli/releases/tag/v1.29.0)
> If your device is Windows 🔽🔽🔽
>> [Download GTK](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

# 5️⃣ Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 6️⃣ Create a superuser (optional)
python manage.py createsuperuser

# 7️⃣ Create .env file
Create **.env** file inside **myshop** project
### Add keys for this sections:
- **SECRET_KEY** - Located in the settings file on django project
- **STRIPE_PUBLISHABLE_KEY** - Located in the Stripe dashboard
- **STRIPE_SECRET_KEY** - Located in the Stripe dashboard
> **STRIPE_WEBHOOK_SECRET** - 🔽🔽🔽
>> Extract Stripe application from zip
>> Open Stripe application in terminal
>> Type **stripe login**
>> Type **stripe listen --forward-to localhost:8000/payment/webhook/**
>> Copy the Webhook Secret Key

# 8️⃣ Start Docker worker
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

# 9️⃣ Start Celery working (Open another terminal)
cd myshop
celery -A myshop worker -l info

# 🔟 Start the server (Open one more terminal)
cd myshop
python manage.py runserver


```

---

## 📄 License

This project is licensed under the MIT License.
