import streamlit as st
import requests
import pandas as pd

# Dashboard setup
st.set_page_config(page_title="Forensic IC Lab", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Industrial IC Forensic Inspector")
st.write("Deterministic Structural Similarity Analysis (Local Engine)")

uploaded_file = st.file_uploader("Upload Chip Image (Target)", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    st.image(uploaded_file, caption="Scan Target", use_container_width=True)
    
    if st.button("RUN FORENSIC SCAN"):
        with st.spinner("Calculating structural integrity..."):
            try:
                # Point to your local FastAPI backend
                backend_url = "http://127.0.0.1:8000/analyze"
                res = requests.post(backend_url, files={"file": uploaded_file.getvalue()})
                
                if res.status_code == 200:
                    data = res.json()
                    
                    # Safety check for the keys we discussed
                    if 'authenticity' in data:
                        st.divider()
                        
                        # Big Status Indicator
                        color = "normal" if data['authenticity'] == "GENUINE" else "inverse"
                        st.metric(
                            label="Structural Similarity Score", 
                            value=f"{round(data['confidence'] * 100, 1)}%", 
                            delta=data['authenticity'], 
                            delta_color=color
                        )
                        
                        st.subheader("🔬 Analysis Report")
                        st.info(f"**Verdict Reason:** {data['reason']}")
                        
                        # Show raw metrics in a table for technical depth
                        st.table(pd.DataFrame([{
                            "Metric": "SSIM Index",
                            "Value": data['confidence'],
                            "Threshold": "0.85",
                            "Status": "PASS" if data['authenticity'] == "GENUINE" else "FAIL"
                        }]))
                        
                        if data['authenticity'] == "GENUINE":
                            st.success("PART CLEARED: Optical signature matches factory master.")
                        else:
                            st.error("PART QUARANTINED: Geometry deviation exceeds tolerance.")
                    else:
                        st.error(f"Backend Error: {data.get('error', 'Unknown response format')}")
                
                else:
                    st.error(f"Server Error: {res.status_code}. Ensure main.py is running.")
            
            except Exception as e:
                st.error(f"Connection Failed: {e}")

st.sidebar.markdown("### System Specs")
st.sidebar.info("Engine: OpenCV / SSIM\nReference: golden_ref.jpg\nMode: Deterministic")
