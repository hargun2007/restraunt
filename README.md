# 🍽️ Restaurant Billing System

A simple **Restaurant Billing System** built using **Python** and **Streamlit**. This application allows users to view the menu, place orders, generate bills, apply discounts, and view the final bill through an interactive web interface.

---

## 🚀 Features

- 📋 View restaurant menu with prices
- 🛒 Add multiple items to the order
- 🔄 Update quantities automatically
- 🗑️ Clear the current order
- 🧾 Generate itemized bill
- 🎉 Apply a 10% discount on orders above ₹1000
- 💰 Display final bill after discount
- 💾 Uses Streamlit Session State to preserve orders during navigation

---

## 🛠️ Technologies Used

- Python 3
- Streamlit

---

## 📂 Project Structure

```
Restaurant-Billing-System/
│── app.py              # Main Streamlit application
│── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Restaurant-Billing-System.git
```

### 2. Navigate to the project directory

```bash
cd Restaurant-Billing-System
```

### 3. Install dependencies

```bash
pip install streamlit
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default browser.

---

## 📖 How to Use

### 1. View Menu
- Browse all available food items and their prices.

### 2. Place Order
- Select an item.
- Enter the quantity.
- Click **Add to Order**.
- Repeat to add more items.
- Use **Clear Order** to reset the cart.

### 3. Generate Bill
- View an itemized bill with:
  - Item name
  - Quantity
  - Price
  - Total amount

### 4. Apply Discount
- Orders above **₹1000** receive a **10% discount**.
- Orders below ₹1000 display a friendly reminder.

### 5. Final Bill
- Displays:
  - Subtotal
  - Discount (if applicable)
  - Final payable amount

---

## 💵 Discount Policy

| Order Amount | Discount |
|--------------|----------|
| ₹1000 or below | No Discount |
| Above ₹1000 | 10% Off |

---

## 🍴 Menu

| Item | Price (₹) |
|------|----------:|
| Burger | 80 |
| Pizza | 120 |
| Pasta | 100 |
| Coke | 40 |
| Pepsi | 40 |
| Sandwich | 60 |
| Fries | 50 |
| Ice Cream | 30 |
| Coffee | 70 |
| Tea | 30 |

---

## 📸 Screens

- 📋 View Menu
- 🛒 Place Order
- 🧾 Generate Bill
- 🎉 Apply Discount
- ✅ Final Bill

---

## 🔮 Future Improvements

- User Login System
- Admin Dashboard
- Database Integration (SQLite/MySQL)
- GST Calculation
- Order History
- PDF Bill Generation
- Online Payment Integration
- Menu Management
- Search and Filter Menu
- Food Images

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Hargunjeet Singh**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
