import streamlit as st

restaurant_menu = {
    "burger": 80,
    "pizza": 120,
    "pasta": 100,
    "coke": 40,
    "pepsi": 40,
    "sandwich": 60,
    "fries": 50,
    "icecream": 30,
    "coffee": 70,
    "tea": 30
}

# Initialize cart in session state (persists across button clicks)
if "saved_bill" not in st.session_state:
    st.session_state.saved_bill = {}

st.title("🍽️ Welcome to the Restaurant")

menu_choice = st.sidebar.radio(
    "Menu",
    ["View Menu", "Place Order", "Generate Bill", "Apply Discount", "Final Bill"]
)

# ---------------- VIEW MENU ----------------
if menu_choice == "View Menu":
    st.header("📋 Menu")
    for item, price in restaurant_menu.items():
        st.write(f"**{item.title()}** : ₹{price}")

# ---------------- PLACE ORDER ----------------
elif menu_choice == "Place Order":
    st.header("🛒 Place Order")
    item_choice = st.selectbox("Select item", list(restaurant_menu.keys()))
    quantity = st.number_input("Quantity", min_value=1, value=1, step=1)

    if st.button("Add to Order"):
        if item_choice in st.session_state.saved_bill:
            st.session_state.saved_bill[item_choice] += quantity
        else:
            st.session_state.saved_bill[item_choice] = quantity
        st.success(f"Added {quantity} x {item_choice} to your order!")

    if st.session_state.saved_bill:
        st.subheader("Current Order")
        for item, qty in st.session_state.saved_bill.items():
            st.write(f"{item.title()} : {qty}")

    if st.button("Clear Order"):
        st.session_state.saved_bill = {}
        st.info("Order cleared.")

# ---------------- GENERATE BILL ----------------
elif menu_choice == "Generate Bill":
    st.header("🧾 Your Bill")
    if not st.session_state.saved_bill:
        st.warning("No items ordered yet. Go to 'Place Order' first.")
    else:
        total = 0
        for item, quantity in st.session_state.saved_bill.items():
            price = restaurant_menu[item]
            total_price = price * quantity
            total += total_price
            st.write(f"{item.title()} : {quantity} x ₹{price} = ₹{total_price}")
        st.markdown(f"### Total: ₹{total}")

# ---------------- APPLY DISCOUNT ----------------
elif menu_choice == "Apply Discount":
    st.header("🎉 Discount")
    if not st.session_state.saved_bill:
        st.warning("No items ordered yet.")
    else:
        total = 0
        for item, quantity in st.session_state.saved_bill.items():
            price = restaurant_menu[item]
            total += price * quantity

        if total > 1000:
            discount_amount = total * 0.1
            total_after_discount = total - discount_amount
            st.write(f"Total: ₹{total}")
            st.write(f"Discount (10%): ₹{discount_amount}")
            st.success(f"Total after discount: ₹{total_after_discount}")
        else:
            st.info("Pehle kharcha to kar le fir discount ki baat karna 😄 (Order above ₹1000 to get 10% off)")

# ---------------- FINAL BILL ----------------
elif menu_choice == "Final Bill":
    st.header("✅ Final Bill")
    if not st.session_state.saved_bill:
        st.warning("No items ordered yet.")
    else:
        total = 0
        for item, quantity in st.session_state.saved_bill.items():
            price = restaurant_menu[item]
            total += price * quantity

        discount_amount = 0
        if total > 1000:
            discount_amount = total * 0.1

        total_after_discount = total - discount_amount

        st.write(f"Subtotal: ₹{total}")
        if discount_amount > 0:
            st.write(f"Discount: ₹{discount_amount}")
        st.markdown(f"### Final Bill: ₹{total_after_discount}")
        st.write("Thank you for dining with us! 🙏")