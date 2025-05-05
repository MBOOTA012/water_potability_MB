import numpy as np
import streamlit as st
import pickle
with open('model.pkl','rb') as file:
    model=pickle.load(file)



    # Page config
    st.set_page_config(page_title="Water Potability Predictor", page_icon="💧", layout="centered")

    # Title and subtitle
    st.title("💧 Water Potability Prediction App")
    st.markdown(
        "Use this tool to predict whether a sample of water is **safe to drink** based on its chemical properties.")

    # Decorative separator
    st.markdown("---")

    # Input layout
    st.header("🔢 Enter Water Quality Parameters")

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("ph", min_value=0.0, max_value=14.0, step=0.1, format="%.2f")
        hardness = st.number_input("Hardness (mg/L)", min_value=0.0, step=0.1)
        solids = st.number_input("Solids (ppm)", min_value=0.0, step=0.1)
        chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, step=0.1)

    with col2:
        sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, step=0.1)
        conductivity = st.number_input("conductivity (μS/cm) ", min_value=0.0, step=0.1)
        organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, step=0.1)
        trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, step=0.1)
        turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, step=0.1)

    # Predict button
    st.markdown("---")
    if st.button("🚀 Predict Water Potability"):
        input_data = np.array([[ph, hardness, solids, chloramines,
                                sulfate, conductivity, organic_carbon,
                                trihalomethanes, turbidity]])

        prediction = model.predict(input_data)[0]

        st.subheader("📊 Prediction Result:")
        if prediction== 1:
            st.success("✅ The water **is potable** – safe to drink.")
        else:
            st.error("❌ The water **is not potable** – not safe to drink.")

    # Footer
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")
