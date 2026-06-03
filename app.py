"""
Monte Carlo Simulator with World Map Visualization
A Streamlit app that generates random world maps and runs Monte Carlo simulations
with user-configurable parameters.
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Monte Carlo Simulator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
        }
        .stMetric {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 0.5rem 0;
        }
        .header-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 0.5rem;
            color: white;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'world_map_seed' not in st.session_state:
    st.session_state.world_map_seed = np.random.randint(0, 10000)
if 'simulation_results' not in st.session_state:
    st.session_state.simulation_results = None


def generate_random_world_map(seed, num_landmasses=15, map_size=100):
    """
    Generate a random world map using random landmasses.
    
    Parameters:
    -----------
    seed : int
        Random seed for reproducibility
    num_landmasses : int
        Number of landmasses to generate
    map_size : int
        Size of the map grid
    
    Returns:
    --------
    np.ndarray : 2D array representing the map (1 = land, 0 = water)
    """
    np.random.seed(seed)
    world_map = np.zeros((map_size, map_size))
    
    for _ in range(num_landmasses):
        # Random center point
        center_x = np.random.randint(5, map_size - 5)
        center_y = np.random.randint(5, map_size - 5)
        
        # Random landmass size
        radius = np.random.randint(3, 15)
        
        # Create landmass using circles
        for i in range(map_size):
            for j in range(map_size):
                distance = np.sqrt((i - center_x)**2 + (j - center_y)**2)
                if distance <= radius:
                    # Add some irregularity
                    if np.random.random() > 0.2:
                        world_map[i, j] = 1
    
    return world_map


def visualize_world_map(world_map):
    """
    Create a visualization of the world map.
    
    Parameters:
    -----------
    world_map : np.ndarray
        2D array representing the map
    
    Returns:
    --------
    matplotlib.figure.Figure : The figure object
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create custom colormap (water = blue, land = green)
    colors = ['#1f77b4', '#2ca02c']
    n_bins = 100
    cmap = LinearSegmentedColormap.from_list('water_land', colors, N=n_bins)
    
    # Display map
    im = ax.imshow(world_map, cmap=cmap, origin='upper', interpolation='nearest')
    
    # Styling
    ax.set_title('🌍 Randomly Generated World Map', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Terrain Type', rotation=270, labelpad=20)
    cbar.set_ticks([0.25, 0.75])
    cbar.set_ticklabels(['Water', 'Land'])
    
    plt.tight_layout()
    return fig


def run_monte_carlo_simulation(num_trials, distribution_type, param1, param2, seed):
    """
    Run a Monte Carlo simulation with user-defined parameters.
    
    Parameters:
    -----------
    num_trials : int
        Number of simulation trials
    distribution_type : str
        Type of distribution ('normal', 'uniform', 'exponential')
    param1 : float
        First parameter (mean/min/lambda)
    param2 : float
        Second parameter (std/max)
    seed : int
        Random seed
    
    Returns:
    --------
    dict : Dictionary containing simulation results
    """
    np.random.seed(seed)
    
    # Generate random samples based on distribution
    if distribution_type == 'Normal Distribution':
        samples = np.random.normal(loc=param1, scale=param2, size=num_trials)
    elif distribution_type == 'Uniform Distribution':
        samples = np.random.uniform(low=param1, high=param2, size=num_trials)
    elif distribution_type == 'Exponential Distribution':
        samples = np.random.exponential(scale=param1, size=num_trials)
    
    # Calculate statistics
    results = {
        'samples': samples,
        'mean': np.mean(samples),
        'std': np.std(samples),
        'min': np.min(samples),
        'max': np.max(samples),
        'median': np.median(samples),
        'percentile_5': np.percentile(samples, 5),
        'percentile_95': np.percentile(samples, 95),
        'distribution_type': distribution_type,
        'num_trials': num_trials
    }
    
    return results


def visualize_monte_carlo_results(results):
    """
    Create visualizations for Monte Carlo simulation results.
    
    Parameters:
    -----------
    results : dict
        Dictionary containing simulation results
    
    Returns:
    --------
    tuple : (histogram_figure, stats_figure)
    """
    samples = results['samples']
    
    # Histogram with distribution curve
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    
    n, bins, patches_hist = ax1.hist(samples, bins=50, density=True, alpha=0.7, 
                                      color='#667eea', edgecolor='black')
    
    # Add KDE curve
    from scipy import stats
    kde = stats.gaussian_kde(samples)
    x_range = np.linspace(samples.min(), samples.max(), 200)
    ax1.plot(x_range, kde(x_range), 'r-', linewidth=2, label='KDE')
    
    # Add vertical lines for mean and std
    ax1.axvline(results['mean'], color='green', linestyle='--', linewidth=2, 
                label=f"Mean: {results['mean']:.2f}")
    ax1.axvline(results['mean'] - results['std'], color='orange', linestyle=':', 
                linewidth=2, label=f"±1 Std Dev")
    ax1.axvline(results['mean'] + results['std'], color='orange', linestyle=':', linewidth=2)
    
    ax1.set_title(f'📊 Monte Carlo Simulation Results ({results["distribution_type"]})', 
                  fontsize=14, fontweight='bold')
    ax1.set_xlabel('Value', fontsize=12)
    ax1.set_ylabel('Probability Density', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Q-Q plot
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    stats.probplot(samples, dist="norm", plot=ax2)
    ax2.set_title('Q-Q Plot (Normality Test)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig1, fig2


# Main app layout
st.markdown("""
    <div class="header-section">
        <h1>🎲 Monte Carlo Simulator with World Map</h1>
        <p>Generate random world maps and run powerful Monte Carlo simulations</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar for controls
st.sidebar.markdown("## 🎛️ Control Panel")

# Map generation section
st.sidebar.markdown("### 🌍 World Map Settings")
if st.sidebar.button("🔄 Generate New World Map", use_container_width=True):
    st.session_state.world_map_seed = np.random.randint(0, 10000)
    st.rerun()

st.sidebar.markdown(f"**Current Map Seed:** `{st.session_state.world_map_seed}`")

map_size = st.sidebar.slider("Map Size", min_value=50, max_value=200, value=100, step=10)
num_landmasses = st.sidebar.slider("Number of Landmasses", min_value=5, max_value=30, value=15)

# Monte Carlo simulation section
st.sidebar.markdown("### 🎲 Monte Carlo Settings")

num_trials = st.sidebar.number_input("Number of Trials", min_value=100, max_value=100000, 
                                     value=10000, step=1000)

distribution_type = st.sidebar.selectbox("Distribution Type", 
                                         ["Normal Distribution", "Uniform Distribution", 
                                          "Exponential Distribution"])

# Distribution parameters based on type
if distribution_type == "Normal Distribution":
    param1 = st.sidebar.number_input("Mean (μ)", value=0.0, step=0.1)
    param2 = st.sidebar.number_input("Standard Deviation (σ)", value=1.0, min_value=0.1, step=0.1)
    param_help = "Normal distribution parameters"
elif distribution_type == "Uniform Distribution":
    param1 = st.sidebar.number_input("Minimum (a)", value=0.0, step=0.1)
    param2 = st.sidebar.number_input("Maximum (b)", value=10.0, step=0.1)
    param_help = "Uniform distribution parameters"
else:  # Exponential
    param1 = st.sidebar.number_input("Lambda (λ)", value=1.0, min_value=0.1, step=0.1)
    param2 = 0  # Not used for exponential
    param_help = "Exponential distribution parameter"

simulation_seed = st.sidebar.number_input("Simulation Seed (for reproducibility)", 
                                          value=42, step=1)

# Main content area with tabs
tab1, tab2, tab3 = st.tabs(["🌍 World Map", "🎲 Simulation", "📈 Results & Analysis"])

# Tab 1: World Map
with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        world_map = generate_random_world_map(st.session_state.world_map_seed, 
                                              num_landmasses, map_size)
        fig_map = visualize_world_map(world_map)
        st.pyplot(fig_map)
    
    with col2:
        st.markdown("### 📊 Map Statistics")
        land_percentage = (np.sum(world_map) / world_map.size) * 100
        water_percentage = 100 - land_percentage
        
        st.metric("Total Land %", f"{land_percentage:.1f}%", delta=None)
        st.metric("Total Water %", f"{water_percentage:.1f}%", delta=None)
        st.metric("Map Dimensions", f"{map_size}×{map_size}")
        st.metric("Landmasses", num_landmasses)
        
        st.markdown("---")
        st.markdown("**Map Information:**")
        st.info("🌊 Blue areas represent water\n🟢 Green areas represent land")

# Tab 2: Simulation Setup
with tab2:
    st.markdown("### 🎲 Configure Your Monte Carlo Simulation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Distribution Type:** {distribution_type}")
        st.markdown(f"**Number of Trials:** {num_trials:,}")
    
    with col2:
        if distribution_type == "Normal Distribution":
            st.markdown(f"**Mean (μ):** {param1}")
            st.markdown(f"**Std Dev (σ):** {param2}")
        elif distribution_type == "Uniform Distribution":
            st.markdown(f"**Min (a):** {param1}")
            st.markdown(f"**Max (b):** {param2}")
        else:
            st.markdown(f"**Lambda (λ):** {param1}")
    
    st.markdown("---")
    
    # Run simulation button
    if st.button("▶️ Run Monte Carlo Simulation", use_container_width=True, type="primary"):
        with st.spinner("Running simulation..."):
            st.session_state.simulation_results = run_monte_carlo_simulation(
                num_trials, distribution_type, param1, param2, simulation_seed
            )
            st.success("✅ Simulation completed successfully!")
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📋 Simulation Parameters")
    st.info("""
    **About Monte Carlo Simulations:**
    - A Monte Carlo simulation uses random sampling to model complex systems
    - The more trials you run, the more accurate your statistical estimates
    - Ideal for problems where analytical solutions are difficult or impossible
    - Common applications: risk analysis, financial modeling, physics simulations
    """)

# Tab 3: Results & Analysis
with tab3:
    if st.session_state.simulation_results is None:
        st.warning("⚠️ No simulation results yet. Run a simulation first in the 'Simulation' tab!")
    else:
        results = st.session_state.simulation_results
        
        # Display statistics
        st.markdown("### 📊 Statistical Results")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Mean (μ)", f"{results['mean']:.4f}")
        col2.metric("Median", f"{results['median']:.4f}")
        col3.metric("Std Dev (σ)", f"{results['std']:.4f}")
        col4.metric("Sample Size (n)", f"{results['num_trials']:,}")
        
        col5, col6, col7, col8 = st.columns(4)
        col5.metric("Min Value", f"{results['min']:.4f}")
        col6.metric("Max Value", f"{results['max']:.4f}")
        col7.metric("5th Percentile", f"{results['percentile_5']:.4f}")
        col8.metric("95th Percentile", f"{results['percentile_95']:.4f}")
        
        st.markdown("---")
        
        # Visualizations
        st.markdown("### 📈 Visualizations")
        
        fig1, fig2 = visualize_monte_carlo_results(results)
        
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig1)
        with col2:
            st.pyplot(fig2)
        
        st.markdown("---")
        
        # Detailed statistics table
        st.markdown("### 📑 Detailed Statistics")
        
        stats_data = {
            'Statistic': ['Mean', 'Median', 'Std Dev', 'Min', 'Max', '5th Percentile', 
                         '95th Percentile', 'Sample Size'],
            'Value': [
                f"{results['mean']:.6f}",
                f"{results['median']:.6f}",
                f"{results['std']:.6f}",
                f"{results['min']:.6f}",
                f"{results['max']:.6f}",
                f"{results['percentile_5']:.6f}",
                f"{results['percentile_95']:.6f}",
                f"{results['num_trials']:,}"
            ]
        }
        
        df_stats = pd.DataFrame(stats_data)
        st.dataframe(df_stats, use_container_width=True, hide_index=True)
        
        # Download results
        st.markdown("---")
        st.markdown("### 💾 Export Results")
        
        # Export as CSV
        csv_data = pd.DataFrame({
            'Sample': range(1, len(results['samples']) + 1),
            'Value': results['samples']
        })
        
        csv_string = csv_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Samples as CSV",
            data=csv_string,
            file_name=f"monte_carlo_samples_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        # Export statistics summary
        summary_text = f"""
Monte Carlo Simulation Results
==============================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CONFIGURATION
- Distribution Type: {results['distribution_type']}
- Number of Trials: {results['num_trials']:,}

STATISTICS
- Mean: {results['mean']:.6f}
- Median: {results['median']:.6f}
- Standard Deviation: {results['std']:.6f}
- Minimum: {results['min']:.6f}
- Maximum: {results['max']:.6f}
- 5th Percentile: {results['percentile_5']:.6f}
- 95th Percentile: {results['percentile_95']:.6f}
"""
        
        st.download_button(
            label="📄 Download Summary Report",
            data=summary_text,
            file_name=f"monte_carlo_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray; font-size: 0.9em;">
        <p>🚀 Monte Carlo Simulator v1.0 | Built with Streamlit 🎈</p>
        <p>For more information about Monte Carlo methods, visit: <a href="https://en.wikipedia.org/wiki/Monte_Carlo_method">Wikipedia</a></p>
    </div>
""", unsafe_allow_html=True)
