import streamlit as st
import requests

st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detector")

# Input field
url = st.text_input("Enter article URL")

# Button click
if st.button("Analyze"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Analyzing article..."):
            try:
                response = requests.post(
                    "http://localhost:8000/predict",
                    json={"url": url},
                    timeout=10
                )

                # Raise error for bad status codes (4xx, 5xx)
                response.raise_for_status()

                data = response.json()

                if "error" in data:
                    st.error(data["error"])
                else:
                    st.subheader("Results")

                    fake_score = data.get("fake_score", 0)
                    ai_score = data.get("ai_generated_score", None)

                    st.write(f"**Fake News Score:** {fake_score:.2f}")

                    if ai_score is not None:
                        st.write(f"**AI Generated Score:** {ai_score:.2f}")

                    # Add interpretation
                    if fake_score > 0.7:
                        st.error("⚠️ Likely Fake News")
                    elif fake_score < 0.3:
                        st.success("✅ Likely Real News")
                    else:
                        st.warning("⚠️ Uncertain / Mixed Signals")

            except requests.exceptions.RequestException as e:
                st.error(f"Backend error: {e}")

            except ValueError:
                st.error("Invalid response from backend (not JSON)")