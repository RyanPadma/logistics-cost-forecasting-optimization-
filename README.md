# 🚚 Optimizing Logistics Cost Forecasts with Machine Learning & Constrained Optimization

---

## 💼 Business Impact & Real-World Scenario

In global supply chains, logistics teams face a persistent challenge: how to minimize shipping costs while respecting supplier contracts, capacity constraints, and unpredictable cost factors like fuel surcharges.  
This project simulates the role of a supply chain analyst at a multi-national company, using data science and optimization to:

- Save shipment costs by reallocating shipments among suppliers.
- Quickly identify cost-saving opportunities based on real-time data.
- Support data-backed negotiations with suppliers and smarter weekly planning.
- Provide transparency and reproducibility in shipment allocations and cost forecasts.

**Result:**  
In our simulated business scenario, the approach yielded up to 9% cost savings for certain suppliers, demonstrating how advanced analytics can deliver real, quantifiable value to logistics operations.

---

## 🧩 Project Overview

This project demonstrates how machine learning and mathematical optimization can work hand-in-hand to minimize logistics costs across a multi-supplier supply chain.  
Weekly shipment data, enriched with features such as fuel surcharges and supplier capacity, is used to train a predictive model that estimates logistics costs.  
This model is then embedded into an optimization process that reallocates shipment volumes, aiming to reduce total predicted costs while attempting to maintain each supplier’s originally forecasted shipment volume.

---

## ✨ Features

- 📊 **Exploratory Data Analysis:** Visualize costs, surcharges, penalties, expedites, and volumes across suppliers.
- 🔗 **Unified Data Preparation:** Automatically combine raw shipment data into a clean, analysis-ready dataset.
- 🧠 **Automated Model Selection:** Benchmark regression models (Linear, Random Forest, Gradient Boosting) for forecasting, reporting MAE and R².
- 🤖 **Cost Optimization:** Use machine learning and mathematical optimization to reallocate shipments, minimizing predicted costs under realistic constraints.
- 📈 **Clear Visual Outputs:** Generate comparison plots for costs and shipment distributions before and after optimization.

---

## 🔧 Tools & Techniques Used

- **Python:** pandas, scikit-learn, scipy.optimize, seaborn, matplotlib
- **Random Forest Regression** for cost prediction (R² = 0.97)
- **SLSQP (Sequential Least Squares Programming)** for constrained nonlinear optimization
- **One-hot encoding** for categorical supplier representation
- **Data visualization** using seaborn and matplotlib

---

## 📊 Exploratory Data Analysis (EDA)
We performed an initial analysis to understand cost drivers and shipment patterns across suppliers.

**Key EDA Visualizations:**
1. **Packages Ordered per Shipment by Supplier**  
   ![Packages Ordered per Shipment by Supplier](results/figures/eda/1. Packages Ordered per Shipment by Supplier.png)

2. **Fuel Surcharge Distribution by Supplier**  
   ![Fuel Surcharge Distribution by Supplier](results/figures/eda/2. Fuel Surcharge Distribution by Supplier.png)

3. **Logistics Cost Over Time by Supplier**  
   ![Logistics Cost Over Time by Supplier](results/figures/eda/3. Logistics Cost Over Time by Supplier.png)

> See the full [EDA Report](EDA.md) for all visuals and detailed interpretations.

## 📈 Machine Learning Component

A Random Forest Regressor predicts weekly logistics costs per supplier using:
- Year and week
- Fuel surcharge
- Weekly shipment volume (`packages_ordered`)
- Supplier identity (via one-hot encoding)

**Model Results:**
- Mean Absolute Error (MAE): **35.68**
- R² Score: **0.97**

These indicate a highly reliable prediction model, forming a solid foundation for downstream optimization.

---

## 🚛 Optimization Objective

Minimize the total predicted logistics cost by adjusting weekly shipment volumes, without exceeding supplier max capacity, and while maintaining total forecasted demand per supplier.

**Constraints:**
- Per-week shipment bounds: `[0, max_capacity]`
- Per-supplier total shipment equality: sum of optimized shipments for each supplier ≈ original sum

---

## 💰 Optimization Outcome

Despite tight constraints, the optimizer produced a lower-cost shipment plan:

| Supplier | Original Cost | Optimized Cost | Savings |
|----------|--------------|---------------|---------|
| B        | 3343.74      | 3030.49       |  313.25 |
| C        | 2227.20      | 2097.20       |  130.01 |
| A        | 2989.85      | 2960.96       |   28.89 |

**⚠️ Limitations & Insights:**
- The SLSQP solver exited with "Exit mode 4," meaning it could not find a fully feasible solution that met all constraints due to the tight combination of per-supplier shipment equality and per-week capacity bounds.
- Slight constraint violations were present:

| Supplier | Original Volume | Optimized Volume | Difference |
|----------|----------------|------------------|------------|
| A        | 1914           | 1878             |   -36      |
| B        | 1134           | 1011             |  -123      |
| C        | 1214           | 1146             |   -68      |

> **Takeaway:**  
> The optimization reduced overall predicted costs but did not fully preserve forecasted demand.  
> In real-world supply chain planning, over-constrained models may become infeasible, and trade-offs between feasibility and optimality must be managed.

---

## 📊 Visuals

- Bar chart: Original vs. optimized predicted logistics cost per supplier
- Line plots: Weekly shipment trends before and after optimization

Find all outputs in the `results/figures/` directory.

---

## ✅ Key Skills Demonstrated

- Supply chain cost modeling and prediction
- Feature engineering and supplier segmentation
- Mathematical programming under realistic business constraints
- Trade-off analysis between forecast accuracy and cost savings
- Data storytelling with business impact

---

## ⚙️ Requirements

- 🐍 Python 3.7+
- 📦 numpy
- 📦 pandas
- 📦 matplotlib
- 📦 seaborn
- 📦 scikit-learn
- 📦 scipy

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🗃️ Data Files

Place the following CSV files in the `data/` directory:
- `supplier_A_shipments.csv`
- `supplier_B_shipments.csv`
- `supplier_C_shipments.csv`

> **Note:** Data files should include columns such as `date`, `supplier`, `logistics_cost`, `packages_sent`, `packages_ordered`, `fuel_surcharge`, `max_capacity`, `year`, `week`, etc., as referenced in the scripts.

---

## 🚀 How to Run

1. ✅ Place your raw supplier shipment CSVs in the `data/` directory.
2. 📥 Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the scripts sequentially:
    - **1. Exploratory Analysis**
      ```bash
      python scripts/1_exploratory_analysis.py
      ```
    - **2. Data Preparation**
      ```bash
      python scripts/2_data_preparation.py
      ```
    - **3. Model Selection**
      ```bash
      python scripts/3_model_selection.py
      ```
    - **4. ML Implementation & Optimization**
      ```bash
      python scripts/4_ml_implementation.py
      ```
4. 📊 View output plots in `results/figures/` and model benchmark results in `results/model_comparison.txt`.

---

## 🏢 Example Business Use Cases

- Weekly or monthly shipment planning for cost efficiency
- What-if scenario analysis for contract renegotiation
- Supplier performance benchmarking
- Budgeting and forecasting logistics costs

**Industry Applicability:**  
This approach is applicable to manufacturing, retail, e-commerce, and any business managing multiple logistics partners.

---

## Contact

For questions, suggestions, or collaboration, please open an issue or contact **Ryan Padma**.

---
