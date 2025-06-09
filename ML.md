## 🚀 Machine Learning & Optimization Results

This section details the predictive modeling and optimization outcomes for logistics cost forecasting and shipment planning.

---

### **1. Model Performance**

- **Mean Absolute Error (MAE):** **35.68**  
- **R² Score:** **0.97**

*A strong R² and low MAE indicate that the machine learning model accurately predicts logistics costs based on the available features and historical data.*

---

### **2. Cost Optimization Analysis**

After training the model, we used it to optimize weekly shipments for each supplier, aiming to minimize total predicted logistics costs while (approximately) preserving each supplier's total demand.

#### **Average Predicted Cost Comparison by Supplier**

| Supplier | Original Cost | Optimized Cost | Savings |
|----------|--------------|---------------|---------|
| B        | 3343.74      | 3030.49       | 313.25  |
| C        | 2227.20      | 2097.20       | 130.01  |
| A        | 2989.85      | 2960.96       | 28.89   |

**Visualization:**  
![Predicted Logistics Cost per Supplier: Original vs Optimized](https://github.com/RyanPadma/logistics-cost-forecasting-optimization-/blob/main/result/figures/ML/Predicted%20Logistics%20Cost%20per%20Supplier%20Original%20vs%20Optimized.png)

*Optimization leads to meaningful cost reductions for all suppliers, with the largest absolute savings for Supplier B.*

---

### **3. Shipment Distribution (Original vs Optimized)**

The weekly shipment patterns for each supplier before and after optimization are visualized below:

![Weekly Shipment Distribution: Original vs Optimized](https://github.com/RyanPadma/logistics-cost-forecasting-optimization-/blob/main/result/figures/ML/Weekly%20Shipment%20DIstribution%20Original%20vs%20Optimized.png)

- **Supplier A:** Optimization slightly smooths shipment numbers, slightly reducing total volume.
- **Supplier B:** More balanced shipment pattern; fewer spikes, total shipments reduced the most.
- **Supplier C:** Minor reductions and smoothing, but overall shipment pattern is similar.

---

### **4. Constraints & Limitations**

- The SLSQP solver exited with "Exit mode 4", indicating that not all constraints could be met exactly:
  - **Per-supplier annual demand was slightly under-fulfilled** due to the tight combination of demand and weekly capacity constraints.
  - Slight constraint violations per supplier (volume differences):
    | Supplier | Original Volume | Optimized Volume | Difference |
    |----------|----------------|------------------|------------|
    | A        | 1914           | 1878             | -36        |
    | B        | 1134           | 1011             | -123       |
    | C        | 1214           | 1146             | -68        |

- **Key Takeaway:**  
  - The model reduced costs overall, but strict constraints led to infeasibility (solver could not find a perfect solution).
  - In practice, supply chain optimization often requires trade-offs—relaxing some constraints may be necessary to achieve feasible and cost-effective plans.

---

### **5. Interpretation & Insights**

- **Substantial cost savings** are possible via predictive optimization, especially for suppliers with more variable or expensive shipping patterns (Supplier B).
- **Constraint management is crucial:** Over-constrained models may be infeasible. It's often necessary to allow for small deviations from targets to unlock larger cost savings.
- **Supplier-specific strategies:**  
  - Optimization results reflect differences in item type, demand pattern, and country-specific logistics costs.

---

### **6. Recommendations**

- **Review and, if possible, relax overly strict constraints** to enable the solver to find feasible, cost-saving solutions without under-fulfilling demand.
- **Continue to leverage predictive models** for scenario analysis and supply chain planning.
- **Monitor constraint violations** in implementation and develop escalation or manual override processes for critical shortages.

---

### **7. Limitations**

- Results are based on the accuracy of the predictive model and the representativeness of historical data.
- Real-world execution may face additional operational, regulatory, or contractual constraints not captured in this analysis.

---

> All results were generated using the project’s `4_ml_implementation.py` script.  
> For EDA context, see [EDA.md](EDA.md).

---

#### **Referenced Images**

- ![IMAGE1](https://github.com/RyanPadma/logistics-cost-forecasting-optimization-/raw/main/result/figures/eda/1.%20Packages%20Ordered%20per%20Shipment%20by%20Supplier.png)
- ![IMAGE2](https://github.com/RyanPadma/logistics-cost-forecasting-optimization-/raw/main/result/figures/eda/2.%20Fuel%20Surcharge%20Distribution%20by%20Supplier.png)
