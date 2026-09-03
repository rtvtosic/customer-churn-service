import os
import requests
import streamlit as st

from user_data import UserData


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Предсказание оттока клиентов")
st.write("Введите данные клиента")

st.write("Личная информация")
gender = st.pills("Gender", ['Female', 'Male'])
partner = st.pills("Partner", ['Yes', 'No'])
dependents = st.pills("Dependents", ['Yes', 'No'])


senior_citizen = st.pills("Senior citizen", [1, 0])

st.write("Оплаченные услуги")
phone_service = st.pills("Phone service", ['Yes', 'No'])
multiple_lines = st.pills("Multiple lines", ['Yes', 'No'])
online_security = st.pills("Online security", ['Yes', 'No'])
online_backup = st.pills("Online backup", ['Yes', 'No'])
device_protection = st.pills("Device protection", ['Yes', 'No'])
tech_support = st.pills("Tech support", ['Yes', 'No'])
streaming_tv = st.pills("Streaming tv", ['Yes', 'No'])
streaming_movies = st.pills("Streaming movies", ['Yes', 'No'])
internet_service = st.pills("Internet service", ['DSL', 'Fiber optic', 'No'])
paperless_billing = st.pills("Paperless billing", ['Yes', 'No'])
contract = st.pills("Contract", ['Month-to-month', 'One year', 'Two year'])
payment_method = st.pills("Payment method", ['Electronic check', 'Mailed check', 
                            'Bank transfer (automatic)', 'Credit card (automatic)'])

tenure = st.number_input("Tenure", 1)
monthly_charges = st.number_input("Monthly charges", 0)
total_charges = st.number_input("Total charges", 0)

if st.button("Предсказать отток"):
    try:
        user = UserData(
            gender=gender,
            partner=partner,
            dependents=dependents,
            phone_service=phone_service,
            multiple_lines=multiple_lines,
            online_security=online_security,
            online_backup=online_backup,
            device_protection=device_protection,
            tech_support=tech_support,
            streaming_tv=streaming_tv,
            streaming_movies=streaming_movies,
            paperless_billing=paperless_billing,
            internet_service=internet_service,
            contract=contract,
            payment_method=payment_method,
            senior_citizen=senior_citizen,
            tenure=tenure,
            monthly_charges=monthly_charges,
            total_charges=total_charges
        )

        try:
            # Предсказание через сервис
            ans = requests.post(url=f"{API_URL}/predict/",
                                json=user.model_dump())
            
            st.write(f"Вероятность оттока клиента: {ans.json()['churn_proba']}")
        except Exception as e:
            st.write(f"Ошибка! {e}")

    except:
        st.write("Ошибка! Заполните все поля о клиенте")
