# ☀️ Solar Power & Irradiance Prediction using NSRDB Data (2020–2023)

This project uses NSRDB (National Solar Radiation Database) data from **2020 to 2023** to predict two key outputs:

- 🌞 **Global Horizontal Irradiance (GHI)** in W/m²  
- ⚡ **Solar Power Generation per m²** in W/m²  

Using a **Random Forest Regressor**, the model estimates how much solar energy reaches a flat surface and how much power could be generated per unit area.

---

## 📂 Project Structure

- **Dataset**: NSRDB CSV files (2020, 2021, 2022, 2023)
- **Models Used**: Random Forest Regressor
- **Predicted Outputs**:
  - **Global Horizontal Irradiance (GHI)**
  - **Solar Power per square meter**
- **Key Features**:
  - Year,Month,Day,Hour
  - DNI
  - DHI
  - Temperature
  - Relative Humidity
  - Wind Speed

---

## 🎯 Objective

To build machine learning models that predict:

1. **GHI** – to understand solar energy potential  
2. **Power/m²** – to estimate energy generation performance for solar panels
### ⚙️ Formula for Power per m²

To calculate solar power generation per square meter:
Power_per_m2 = GHI × η
- `GHI`: Global Horizontal Irradiance (in W/m²)  
- `η`: Efficiency of the solar panel (assumed to be 0.18 in this project).
These predictions support clean energy planning and real-time solar forecasting.

---

## 🛠️ Tools & Libraries Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Google Colab

---

## 🚀 Workflow

1. **Data Preprocessing**
   - Loaded and combined yearly NSRDB data
   - Removed irrelevant or sparse columns
   - Selected core meteorological and solar features

2. **Feature Engineering**
   - Focused on environmental conditions influencing GHI and solar power

3. **Model Training**
   - Used RandomForestRegressor from scikit-learn
   - Trained two separate models:
     - One for **GHI prediction**
     - One for **solar power per m² prediction**

4. **Evaluation**
   - Metrics: R² Score, MAE
   - Compared predicted vs actual values through plots

---

## 📈 Results

Both models achieved good accuracy and generalization:

- 📊 **GHI Prediction**: High R² and low error across test sets  
- ⚡ **Power Prediction**: Closely matched actual power values per m²

These results enable accurate forecasting and better decision-making for solar deployment.

---

## 🔮 Future Work

- Try advanced models (e.g., XGBoost, Gradient Boosting)
- Integrate real-time solar data for live predictions
- Deploy as a web app for interactive forecasting

---
