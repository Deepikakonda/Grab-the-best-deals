

# 🛍️ Grab-the-Best-Deals – Student Shopping Companion
A full-stack web application built for students to effortlessly **compare and grab the best deals** across major e-commerce sites like **Amazon**, **BestBuy**, and more. It filters and displays the cheapest options for groceries, stationery, electronics, and more — making smart shopping easier, faster, and cost-effective for students on a budget.

> 🎓 Helping students save money, one smart deal at a time.

![Built with Django](https://img.shields.io/badge/Backend-Django-green)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-blue)
![Database](https://img.shields.io/badge/DataSource-ECommerce%20Sites-lightgrey)
![Web Scraping](https://img.shields.io/badge/Scraping-BeautifulSoup-orange)

---

## 🚀 Key Features

* 🛒 **Search & Compare Products** – Instantly find and compare items like electronics, stationery, and groceries.
* 🔍 **Category Filtering** – Browse items by categories: Groceries, Stationery, Electronics, Clothing, and more.
* 💸 **Real-time Price Comparison** – Scrapes latest prices from multiple retailers to show the best deals.
* 🔗 **Redirect to Product Pages** – Click to purchase directly from the seller's page (Amazon, BestBuy, etc.).
* 📬 **User-Friendly Interface** – Designed with students in mind — fast, simple, responsive.
* ⚙️ **Backend Logic** – Uses BeautifulSoup for real-time web scraping and Django for API and request handling.

---

## 🧠 Technologies Used

| Category            | Tool / Library                   | Purpose                                              |
| ------------------- | -------------------------------- | ---------------------------------------------------- |
| **Frontend**        | HTML, CSS, JavaScript, Bootstrap | Build responsive and intuitive UI                    |
| **Backend**         | Python, Django                   | API, user requests, view rendering                   |
| **Web Scraping**    | BeautifulSoup, Requests          | Extract real-time product data from e-commerce sites |
| **Deployment**      | Render / Localhost               | Hosting the full-stack app                           |
| **Version Control** | Git, GitHub                      | Collaboration and codebase management                |

---

## 📁 Categories Covered

* 🛒 **Groceries**
* ✏️ **Stationery**
* 💻 **Electronics**
* 👕 **Clothing**
* 🎧 **Accessories**

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/grab-the-best-deals.git
cd grab-the-best-deals
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the development server**

```bash
python manage.py runserver
```

---

## 🔍 Web Scraping Logic

* **Library**: BeautifulSoup, Requests
* **Function**: Parses HTML content from e-commerce platforms.
* **Goal**: Extract and display the lowest priced product matching the user’s search query.
* **Security**: Basic headers added to mimic browser behavior and avoid blocks.

---

## 👥 Contributors

* **Harish** – Frontend Development & UI Design
* **Deepika** – Backend Development & Web Scraping Logic



