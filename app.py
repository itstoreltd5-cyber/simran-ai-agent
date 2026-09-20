
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Simran AI Agent", page_icon="🤖")

st.title("🤖 সিমরান (Simran) - AI Assistant")
st.write("আপনার ডিজিটাল কাজের বিশ্বস্ত এআই সহকারী।")

# Sidebar for API Key
st.sidebar.header("সেটিংস (Settings)")
api_key = st.sidebar.text_input("Google AI Studio API Key দিন:", type="password")

if not api_key:
    st.info("👈 শুরু করতে বাম পাশের সাইডবারে আপনার Gemini API Key টি বসান।")
else:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # User Input
        user_prompt = st.text_area("আপনার প্রশ্ন বা নির্দেশ লিখুন:", height=100)
        
        if st.button("উত্তর দিন (Send)"):
            if user_prompt:
                with st.spinner("সিমরান চিন্তা করছে..."):
                    response = model.generate_content(user_prompt)
                    st.success("উত্তর:")
                    st.write(response.text)
            else:
                st.warning("অনুগ্রহ করে কোনো প্রশ্ন বা নির্দেশনা লিখুন।")
    except Exception as e:
        st.error(f"একটি সমস্যা হয়েছে: {e}")
