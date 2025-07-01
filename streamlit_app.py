import streamlit as st
import plotly.graph_objects as go

# --- Function for Contact Footer ---
def contact_footer():
    st.markdown("""
    <hr style="margin-top: 40px; border: 0.5px solid #e5e7eb;">
    <div style="text-align: center; color: #6b7280; font-size: 14px; padding: 15px; line-height: 1.8;">
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-bottom: 8px;">
            <div style="display: flex; align-items: center; gap: 4px;">
                <span style="color: #10b981;">📌</span> <strong>Syed Huzaifa</strong>
            </div>
            <div style="display: flex; align-items: center; gap: 4px;">
                <span style="color: #10b981;">🏢</span> Office #09, First Floor, Royal Square Plaza
            </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px;">
            <div style="display: flex; align-items: center; gap: 4px;">
                <span style="color: #10b981;">🏙</span> Gulberg Residencia, Islamabad
            </div>
            <div style="display: flex; align-items: center; gap: 4px;">
                <a href="https://wa.me/923359199818" 
                   style="color: #10b981; text-decoration: none; display: flex; align-items: center; gap: 4px;" 
                   target="_blank">
                   <span style="color: #10b981;">📱</span>
                   <strong style="color: #25D366;">WhatsApp: +92 335 9199 818</strong>
                </a>
            </div>
            <div style="display: flex; align-items: center; gap: 4px;">
                <a href="mailto:shhkohat22@gmail.com" 
                   style="color: #10b981; text-decoration: none; display: flex; align-items: center; gap: 4px;" 
                   target="_blank">
                   <span style="color: #10b981;">✉️</span>
                   <strong>shhkohat22@gmail.com</strong>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="Disposable Factory – Investor Pitch", layout="wide")

# Custom CSS for professional styling
st.markdown("""
<style>
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 4px solid #10b981;
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: 700;
        color: #047857;
        margin-bottom: 5px;
    }
    .metric-label {
        font-size: 14px;
        color: #4b5563;
    }
    .comparison-badge {
        background: #f0fdf4;
        color: #065f46;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 12px;
        display: inline-block;
        margin-left: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style='text-align: center; color: #10b981; margin-bottom: 10px;'>
    🏭 Disposable Manufacturing Investment Opportunity
</h1>
<p style='text-align: center; color: #6b7280; margin-bottom: 30px;'>
    Addressing Pakistan's PKR 12B import substitution gap
</p>
<hr>
""", unsafe_allow_html=True)

# Tabs setup
tabs = st.tabs([
    "📊 PK Market", 
    "🏗 Ops. Advantage",
    "📈 Fin. Returns",
    "🛡 Risk Mgmt"
])

with tabs[0]:
    # Market Opportunity Tab
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">PKR 12B</div>
            <div class="metric-label">Annual import substitution opportunity</div>
            <span class="comparison-badge">+15% CAGR</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">42%</div>
            <div class="metric-label">Current import dependency 
            <span style="color: #ef4444;">(SBP 2023)</span></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">23%</div>
            <div class="metric-label">Healthcare demand growth 
            <span class="comparison-badge">Post-COVID</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">18K tons</div>
            <div class="metric-label">Monthly packaging shortfall</div>
            <span class="comparison-badge">Trade Development Authority</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Market Growth Chart
    st.markdown("### Market Demand Projection")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['2023', '2024', '2025', '2026', '2027'],
        y=[61, 66, 71, 76, 82],
        mode='lines+markers',
        line=dict(color='#10b981', width=3),
        marker=dict(size=10)
    ))
    fig.update_layout(
        yaxis_title="Demand (Thousand Tons)",
        plot_bgcolor='white',
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    contact_footer()


with tabs[1]:
    # Operational Advantage Tab
    st.markdown("""
    <div style="background: #f8fafc; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #1e40af; margin-top: 0;">Core Competitive Advantages</h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
            <div style="background: white; padding: 15px; border-radius: 8px;">
                <div style="font-weight: 600; margin-bottom: 8px;">🏭 Automated Production</div>
                <div style="font-size: 14px; color: #4b5563;">
                    60-70% labor cost reduction vs traditional manufacturing
                </div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px;">
                <div style="font-weight: 600; margin-bottom: 8px;">🔋 Solar Hybrid</div>
                <div style="font-size: 14px; color: #4b5563;">
                    45% energy cost reduction with net metering
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Cost Comparison
    st.markdown("### Cost Advantage vs Imports")
    cost_data = {
        'Cost Factor': ['Raw Materials', 'Labor', 'Energy', 'Logistics'],
        'Local Production': [35, 15, 20, 10],
        'Imported Goods': [40, 25, 30, 25]
    }
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cost_data['Cost Factor'],
        y=cost_data['Local Production'],
        name='Local Production',
        marker_color='#10b981'
    ))
    fig.add_trace(go.Bar(
        x=cost_data['Cost Factor'],
        y=cost_data['Imported Goods'],
        name='Imported Goods',
        marker_color='#ef4444'
    ))
    fig.update_layout(
        barmode='group',
        plot_bgcolor='white',
        yaxis_title="Cost Index (Lower is better)"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    contact_footer()    
    
with tabs[2]:  # 📈 Financial Returns
    st.markdown("""
    <div style="background: #f8fafc; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #1e40af; margin-top: 0;">Projected Financial Performance</h3>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 20px;">
            <div style="background: white; padding: 15px; border-radius: 8px; text-align: center;">
                <div class="metric-value">28-32%</div>
                <div class="metric-label">Annual ROI</div>
                <div style="font-size: 12px; color: #6b7280;">(Industry avg: 18-22%)</div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; text-align: center;">
                <div class="metric-value">18-24mo</div>
                <div class="metric-label">Payback Period</div>
                <div style="font-size: 12px; color: #6b7280;">(With solar tax credits)</div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; text-align: center;">
                <div class="metric-value">PKR 1.8M</div>
                <div class="metric-label">Monthly EBITDA</div>
                <div style="font-size: 12px; color: #6b7280;">@60% capacity</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ROI Comparison Chart (Pakistan Specific)
    st.markdown("### ROI Comparison vs Alternative Investments")
    roi_data = {
        'Investment Type': ['Disposable Factory', 'Textiles', 'Real Estate', 'T-Bills'],
        'Annual ROI': [30, 18, 22, 12],
        'Risk': ['Medium', 'High', 'Medium', 'Low']
    }
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=roi_data['Investment Type'],
        y=roi_data['Annual ROI'],
        marker_color=['#10b981', '#9ca3af', '#9ca3af', '#9ca3af'],
        text=roi_data['Annual ROI'],
        textposition='auto'
    ))
    fig.update_layout(
        yaxis_title="ROI (%)",
        plot_bgcolor='white',
        annotations=[dict(
            x='Disposable Factory',
            y=32,
            text="Best in class",
            showarrow=True,
            arrowhead=1,
            ax=0, ay=-40
        )]
    )
    st.plotly_chart(fig, use_container_width=True)

    # Capital Efficiency Calculator
    st.markdown("### Investment Scenario Analysis")
    col1, col2 = st.columns(2)
    with col1:
        investment = st.slider("Capital Investment (PKR millions)", 50, 150, 75)
    with col2:
        capacity = st.slider("Production Capacity Utilization", 50, 100, 80)
    
    projected_roi = 22 + (capacity - 50) * 0.3  # Dynamic ROI calculation
    st.markdown(f"""
    <div class="metric-card" style="text-align: center;">
        <div class="metric-value">PKR {investment * projected_roi/100:.1f}M</div>
        <div class="metric-label">Annual Return at {capacity}% capacity</div>
        <div style="font-size: 12px; color: #6b7280; margin-top: 8px;">
            {projected_roi:.0f}% ROI | Break-even: {24 - (capacity/10):.0f} months
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    contact_footer()

with tabs[3]:  # 🛡 Risk Management
    st.markdown("""
    <div style="background: #fef2f2; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #b91c1c; margin-top: 0;">Risk Mitigation Framework</h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #ef4444;">
                <div style="font-weight: 600; color: #b91c1c; margin-bottom: 8px;">Currency Fluctuations</div>
                <div style="font-size: 14px; color: #4b5563;">
                    <span style="color: #10b981;">✓</span> 70% raw material sourcing in PKR<br>
                    <span style="color: #10b981;">✓</span> USD hedges for imported machinery
                </div>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #ef4444;">
                <div style="font-weight: 600; color: #b91c1c; margin-bottom: 8px;">Energy Costs</div>
                <div style="font-size: 14px; color: #4b5563;">
                    <span style="color: #10b981;">✓</span> 200kW solar hybrid system<br>
                    <span style="color: #10b981;">✓</span> Net metering contract with LESCO
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Risk Matrix (Pakistan Specific)
    st.markdown("### Risk Assessment Matrix")
    risk_data = {
        'Risk Factor': ['Raw Material Prices', 'Energy Availability', 'Regulatory Changes', 'Demand Fluctuation'],
        'Likelihood': [3, 4, 2, 3],  # 1-5 scale
        'Impact': [4, 5, 3, 4],      # 1-5 scale
        'Mitigation': [
            "Long-term contracts with local suppliers",
            "Solar + grid hybrid system",
            "SEZ registration in progress",
            "Contracts with 5 major hospital chains"
        ]
    }
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=risk_data['Likelihood'],
        y=risk_data['Impact'],
        text=risk_data['Risk Factor'],
        mode='markers+text',
        marker=dict(
            size=[20, 25, 15, 20],
            color=['#ef4444', '#f97316', '#f59e0b', '#f59e0b'],
            opacity=0.8
        ),
        textposition="top center"
    ))
    fig.update_layout(
        xaxis=dict(title='Likelihood (1-5)', range=[0,6]),
        yaxis=dict(title='Impact (1-5)', range=[0,6]),
        plot_bgcolor='white',
        shapes=[
            dict(type="rect", x0=0, y0=0, x1=2.5, y1=2.5, fillcolor="green", opacity=0.1),
            dict(type="rect", x0=2.5, y0=2.5, x1=5, y1=5, fillcolor="red", opacity=0.1)
        ],
        annotations=[
            dict(x=1, y=1, text="Low Priority", showarrow=False),
            dict(x=4, y=4, text="Critical Risks", showarrow=False)
        ]
    )
    st.plotly_chart(fig, use_container_width=True)

    # Contingency Planning
    st.markdown("""
    <div class="metric-card">
        <h4 style="color: #1e40af; margin-top: 0;">Business Continuity Plan</h4>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 15px;">
            <div style="padding: 10px; background: #f0fdf4; border-radius: 6px;">
                <div style="font-weight: 600;">🛡️ 6-Month Buffer</div>
                <div style="font-size: 13px;">Raw material inventory for supply shocks</div>
            </div>
            <div style="padding: 10px; background: #f0fdf4; border-radius: 6px;">
                <div style="font-weight: 600;">💵 Forex Reserve</div>
                <div style="font-size: 13px;">15% of capital in USD for emergencies</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    contact_footer()
