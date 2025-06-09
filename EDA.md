## 📊 Exploratory Data Analysis (EDA) Results

A thorough EDA was conducted to understand shipment patterns, cost structures, and supplier performance. Key findings and supporting visualizations are summarized below.

---

### **Packages Sent per Shipment by Supplier**

**Comparative Summary Table**

| Supplier | Median Packages Ordered | Spread (IQR) | Outliers Present? | General Pattern                  |
|----------|------------------------|--------------|-------------------|----------------------------------|
| Germany  | ~18                    | Narrow       | Yes (higher end)  | Larger, consistent shipments     |
| USA      | ~10                    | Narrow       | Yes (higher end)  | Smaller, consistent shipments    |
| China    | ~11                    | Narrow       | Yes (higher end)  | Smaller, consistent shipments    |

**Interpretation:**  
- Germany typically ships larger orders with less variability, but occasionally much larger shipments.
- USA and China have similar and smaller shipment sizes, with less frequent large orders.
- Outliers for all suppliers suggest occasional atypically large shipments, especially from Germany.

**Conclusion:**  
The boxplot clearly shows that the German supplier handles larger shipments on average, while the USA and China suppliers have similar, smaller shipment sizes. This may reflect differences in supply chain strategies, order batching, or customer demand patterns.

![result/figures/eda/1. Packages Ordered per Shipment by Supplier.png]

---

### **Fuel Surcharge Distribution by Supplier**

**Interpretation in Procurement Context:**  
- **Uniformity is Expected:** Fuel surcharges are similar across all suppliers, as they are likely set by global or regional logistics providers or freight forwarders.
- **Slight Variability:** The small range (1.20–1.40) and lack of supplier-specific trends indicate stable surcharges.
- **No Red Flags:** No extreme outliers or spikes for any supplier, suggesting consistent logistics cost management.

![results/figures/eda/2. Fuel Surcharge Distribution by Supplier.png]

---

### **Logistics Cost Over Time by Supplier**

**Interpretation:**  
- **USA:** High and volatile costs due to long-distance shipping, higher per-package costs, and lower shipment capacities. Careful planning is required to avoid costly expedited shipments.
- **Germany:** Stable and moderate costs typical for intra-European logistics, benefiting from proximity and efficient batch shipments.
- **China:** Lowest costs, possibly due to efficient bulk shipping, favorable contracts, or consolidated freight. Occasional spikes should be monitored for disruptions.

![results/figures/eda/3. Logistics Cost Over Time by Supplier.png]

---

### **Penalty Cost & Expedite Cost by Supplier**

**Summary Table**

| Supplier | Penalty Cost (Spread & Outliers) | Expedite Cost (Level & Variability) |
|----------|----------------------------------|-------------------------------------|
| Germany  | Lowest, few outliers             | Lowest, constant                    |
| USA      | Highest, many outliers           | Highest, constant                   |
| China    | Moderate, some outliers          | Moderate, constant                  |

- **Penalty Costs:** USA supplier exhibits the highest median penalty cost, with a wide spread and many significant outliers, indicating frequent and sometimes very high penalties. China shows a range with outliers, but the median is lower. Germany has the lowest penalty costs with fewer outliers.
- **Expedite Costs:** Relatively stable for each supplier. USA has the highest, followed by China, then Germany. Little to no variability within each supplier group.

![results/figures/eda/4. Penalty and Expedite Cost by Supplier.png]

---

#### **Trend Over Time for Penalty and Expedite Cost**
- **Penalty Costs:** Most volatile for USA, with frequent spikes. China also spikes but is generally lower. Germany’s penalty costs are less frequent and tend to be lower, with occasional moderate spikes.
- **Expedite Costs:** Constant over time for each supplier. USA consistently incurs the highest expedite cost, China is moderate, Germany is the lowest.

![results/figures/eda/5. Penalty Cost Over Time by Supplier.png]
![results/figures/eda/6. Expedite Cost Over Time by Supplier.png]

---

### **Shipment Patterns & Cost Structure**

- **Germany:** Ships larger, less frequent orders. Lower penalty and expedite costs, but occasional large outliers.
- **USA & China:** Smaller, more frequent shipments. Face higher penalty and expedite costs, likely due to stricter capacity constraints and higher base costs.
- **Outliers:** All suppliers occasionally handle atypically large or urgent orders, especially the USA.

---

### **Conclusion**

- **Germany is the most cost-effective supplier** in terms of penalty and expedite costs, likely due to proximity and shipment strategy.
- **USA and China incur higher costs**, especially USA, which also shows the greatest volatility and risk of high penalty events.
- **No red flags or supplier-specific issues** requiring immediate attention; cost and shipment patterns are typical for an international, diversified supply chain.
- **Fuel surcharges are uniformly managed** and do not present cost risks.

---

> All EDA figures are generated by `scripts/1_exploratory_analysis.py` and saved in `results/figures/eda/`.
