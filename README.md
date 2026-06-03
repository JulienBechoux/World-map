# 🎲 Monte Carlo Simulator with World Map Visualization

A powerful interactive web application built with **Streamlit** that combines random world map generation with advanced **Monte Carlo simulations**. Perfect for learning about statistical methods, probability distributions, and computational simulation techniques.

## 🌟 Features

### 🌍 Random World Map Generation
- **Procedural Landmass Generation**: Creates realistic random world maps with customizable parameters
- **Dynamic Terrain Visualization**: Blue water and green landmasses with professional styling
- **Real-time Statistics**: Display land/water percentages and map dimensions
- **Reproducible Maps**: Use seeds to generate the same map consistently
- **Adjustable Complexity**: Control the number of landmasses and map size

### 🎲 Monte Carlo Simulations
- **Multiple Distributions**:
  - Normal Distribution (Gaussian) - μ and σ parameters
  - Uniform Distribution - Min and Max bounds
  - Exponential Distribution - Lambda parameter
- **Configurable Parameters**:
  - Number of trials (100 to 100,000)
  - Adjustable distribution parameters
  - Random seed for reproducibility
- **Advanced Statistics**:
  - Mean, Median, Standard Deviation
  - Min/Max values
  - Percentile analysis (5th and 95th)
  - Full sample data export

### 📊 Comprehensive Analysis & Visualization
- **Histogram with KDE Curve**: Visualize distribution shape and density
- **Statistical Overlays**: Mean line and standard deviation bands
- **Q-Q Plot**: Assess normality of distribution
- **Detailed Metrics Dashboard**: Quick-glance statistical summaries
- **Interactive Tables**: Formatted statistical results
- **Data Export**: Download results as CSV or text report

### 💾 Data Export Options
- **CSV Export**: All simulation samples with indices
- **Summary Report**: Text file with key statistics and configuration
- **Timestamped Files**: Automatic naming with generation timestamp

---

## 📋 Requirements

- Python 3.8 or higher
- All dependencies listed in `requirements.txt`

### Core Dependencies:
| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | 1.28.1 | Web app framework |
| `numpy` | 1.24.3 | Numerical computing |
| `matplotlib` | 3.7.2 | Visualization |
| `seaborn` | 0.12.2 | Statistical visualization |
| `pandas` | 2.0.3 | Data manipulation |
| `scipy` | 1.11.2 | Statistical functions |

---

## 🚀 Installation & Setup

### Step 1: Clone or Download the Repository
```bash
git clone <your-repo-url>
cd monte-carlo-simulator
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📖 User Guide

### 🌍 Tab 1: World Map

1. **Generate New Map**: Click the "Generate New World Map" button to create a new random map
2. **Adjust Settings**:
   - **Map Size**: Slider to control grid dimensions (50-200)
   - **Number of Landmasses**: Slider to control terrain complexity (5-30)
3. **View Statistics**: Right panel shows:
   - Land/Water percentages
   - Map dimensions
   - Number of landmasses

#### Map Seed
Each map has a unique seed value displayed at the top. You can use this seed to regenerate the exact same map later by modifying the code.

---

### 🎲 Tab 2: Simulation

1. **Select Distribution Type**:
   - **Normal Distribution**: Gaussian curve - enter mean (μ) and standard deviation (σ)
   - **Uniform Distribution**: Flat distribution - enter minimum and maximum values
   - **Exponential Distribution**: Decay curve - enter lambda (λ) parameter

2. **Configure Parameters**:
   - **Number of Trials**: How many random samples to generate (100-100,000)
   - **Distribution Parameters**: Specific to the selected distribution
   - **Simulation Seed**: For reproducible results (default: 42)

3. **Run Simulation**: Click the "Run Monte Carlo Simulation" button

#### Tips for Best Results:
- **More trials** = More accurate statistics but slower execution
- Use the **same seed** to reproduce exact results
- **Normal distribution** is ideal for most applications
- **Uniform distribution** for equally likely outcomes
- **Exponential distribution** for time-to-event or decay processes

---

### 📈 Tab 3: Results & Analysis

After running a simulation, you'll see:

#### 📊 Statistical Summary
Eight key metrics displayed as cards:
- **Mean (μ)**: Average value of all samples
- **Median**: Middle value (50th percentile)
- **Std Dev (σ)**: Measure of spread
- **Min/Max**: Extreme values
- **5th/95th Percentiles**: Probability boundaries

#### 📊 Visualizations

**Histogram with KDE Curve**:
- Blue bars show frequency distribution
- Red line shows smoothed kernel density estimation
- Green dashed line marks the mean
- Orange dotted lines show ±1 standard deviation

**Q-Q Plot**:
- Compares your data against a normal distribution
- Points close to the line indicate normality
- Deviations show non-normal characteristics

#### 📑 Detailed Statistics Table
A formatted table with all key statistics for easy reference

#### 💾 Export Options
- **Download Samples as CSV**: All generated samples with row numbers
- **Download Summary Report**: Text file with configuration and statistics

---

## 🔬 Understanding Monte Carlo Simulations

### What is a Monte Carlo Simulation?

A **Monte Carlo simulation** is a computational technique that:
1. Uses **random sampling** from probability distributions
2. Runs many **independent trials** (thousands to millions)
3. **Aggregates results** to estimate outcomes
4. Works with problems too complex for analytical solutions

### Why Use Monte Carlo?

| Use Case | Benefit |
|----------|---------|
| **Risk Analysis** | Quantify uncertainty in financial models |
| **Physics Simulations** | Model particle behavior and interactions |
| **Engineering** | Reliability testing and stress analysis |
| **Operations** | Queuing systems and supply chain modeling |
| **Finance** | Option pricing and portfolio optimization |

### Key Concepts

**Law of Large Numbers**: As the number of trials increases, the sample mean approaches the true expected value

**Central Limit Theorem**: Sample means from any distribution become normally distributed with enough trials

**Confidence Intervals**: 5th-95th percentiles represent the 90% confidence interval (middle 90% of outcomes)

### Probability Distributions Explained

#### Normal Distribution
- **Shape**: Bell curve, symmetric around mean
- **Use**: Most natural processes, heights, test scores
- **Parameters**: Mean (μ) and Standard Deviation (σ)
- **Formula**: Gaussian probability density function

#### Uniform Distribution
- **Shape**: Flat, equal probability everywhere
- **Use**: Random selection, modeling complete uncertainty
- **Parameters**: Minimum (a) and Maximum (b)
- **Formula**: Constant probability between bounds

#### Exponential Distribution
- **Shape**: Right-skewed, rapid decay
- **Use**: Time between events, radioactive decay, queue times
- **Parameters**: Lambda (λ) - rate parameter
- **Formula**: λ × e^(-λx)

---

## 💡 Example Workflows

### Example 1: Risk Analysis
**Scenario**: Estimating project completion time with uncertainty

1. Go to **World Map** tab, generate a map for context
2. In **Simulation** tab:
   - Distribution: Normal Distribution
   - Mean (μ): 30 (days)
   - Std Dev (σ): 5 (days)
   - Trials: 10,000
3. Review **Results** tab:
   - See 95th percentile for worst-case estimate
   - Use for project planning buffers

### Example 2: Financial Modeling
**Scenario**: Stock price fluctuations

1. **Simulation** tab:
   - Distribution: Normal Distribution
   - Mean (μ): 100 (initial price)
   - Std Dev (σ): 10 (volatility)
   - Trials: 50,000
2. **Results** tab:
   - Analyze percentiles for price ranges
   - Download data for further analysis

### Example 3: Physics Simulation
**Scenario**: Particle velocities

1. **Simulation** tab:
   - Distribution: Exponential Distribution
   - Lambda (λ): 0.5
   - Trials: 20,000
2. **Results** tab:
   - Study decay characteristics
   - Verify mathematical properties

---

## 🎨 Customization

### Modifying the App

#### Change Map Colors
Edit line in `app.py`:
```python
colors = ['#1f77b4', '#2ca02c']  # [Water, Land]
```

#### Adjust Slider Ranges
Modify sidebar settings:
```python
map_size = st.sidebar.slider("Map Size", 
    min_value=50,      # Change minimum
    max_value=200,     # Change maximum
    value=100,         # Change default
    step=10)           # Change step
```

#### Add New Distribution
In `run_monte_carlo_simulation()` function, add:
```python
elif distribution_type == 'Beta Distribution':
    samples = np.random.beta(a=param1, b=param2, size=num_trials)
```

---

## 📊 Output Examples

### Map Statistics Output
```
Total Land %: 42.3%
Total Water %: 57.7%
Map Dimensions: 100×100
Landmasses: 15
```

### Simulation Statistics Output
```
Mean (μ): 15.2847
Median: 15.1234
Std Dev (σ): 2.3456
Min: 5.1234
Max: 24.8901
5th Percentile: 10.2345
95th Percentile: 20.3456
Sample Size: 10,000
```

---

## 🐛 Troubleshooting

### Issue: App won't start
**Solution**: Ensure all requirements are installed
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Maps look too simple
**Solution**: Increase "Number of Landmasses" slider (10-30 recommended)

### Issue: Simulation takes too long
**Solution**: Reduce "Number of Trials" (start with 5,000-10,000)

### Issue: Charts don't display
**Solution**: Ensure matplotlib backend is working
```bash
python -c "import matplotlib; print(matplotlib.get_backend())"
```

---

## 📚 Mathematical Formulas

### Normal Distribution
```
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))
```

### Uniform Distribution
```
f(x) = 1 / (b - a)  for a ≤ x ≤ b
```

### Exponential Distribution
```
f(x) = λ × e^(-λx)  for x ≥ 0
```

### Statistics
```
Mean: μ = Σx / n
Variance: σ² = Σ(x - μ)² / n
Standard Deviation: σ = √variance
Percentile: Value at (n × p / 100)th position
```

---

## 🔗 External Resources

- **Streamlit Documentation**: https://docs.streamlit.io
- **NumPy Guide**: https://numpy.org/doc/
- **SciPy Statistics**: https://docs.scipy.org/doc/scipy/reference/stats.html
- **Monte Carlo Methods**: https://en.wikipedia.org/wiki/Monte_Carlo_method
- **Probability Distributions**: https://en.wikipedia.org/wiki/Probability_distribution

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 About

Created as an educational tool for learning:
- Monte Carlo simulation techniques
- Probability distributions
- Data visualization with Python
- Interactive app development with Streamlit

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new distributions
- Improve visualizations
- Enhance the map generation algorithm
- Add new statistical measures

---

## 📧 Support

For questions or issues:
1. Check the **Troubleshooting** section above
2. Review Streamlit and NumPy documentation
3. Open an issue in the repository

---

## 🎓 Learning Path

If you're new to Monte Carlo simulations, follow this learning path:

1. **Start Simple**: Use Normal Distribution with default parameters
2. **Understand Statistics**: Review the "Understanding Monte Carlo" section
3. **Try Different Distributions**: Experiment with Uniform and Exponential
4. **Increase Complexity**: Gradually increase number of trials
5. **Analyze Results**: Study the Q-Q plots and percentiles
6. **Customize**: Modify the code to suit your needs

---

**Happy Simulating! 🚀**
