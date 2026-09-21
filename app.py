import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Simran AI Agent", page_icon="🤖")

st.title("🤖 সিমরান (Simran) - AI Assistant")
st.write("আপনার ডিজিটাল কাজের বিশ্বস্ত এআই সহকারী।")

# Sidebar for API Key
st.sidebar.header("সেটিংস (Settings)")
api_key = st.sidebar.text_input("Google AI Studio API Key দিন:", type="password")

if not api_key:
    st.info("👈 শুরু করতে বাম পাশের সাইডবারে আপনার Gemini API Key টি বসান।")
else:
    # User Input
    user_prompt = st.text_area("আপনার প্রশ্ন বা নির্দেশ লিখুন:", height=100)
    
    if st.button("উত্তর দিন (Send)"):
        if user_prompt:
            with st.spinner("সিমরান চিন্তা করছে..."):
                try:
                    # Direct API endpoint to bypass library version errors
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
                    
                    headers = {'Content-Type': 'application/json'}
                    data = {
                        "contents": [{
                            "parts": [{"text": user_prompt}]
                        }]
                    }
                    
                    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
                    
                    with urllib.request.urlopen(req) as response:
                        res_data = json.loads(response.read().decode('utf-8'))
                        ai_reply = res_data['candidates'][0]['content']['parts'][0]['text']
                        
                        st.success("উত্তর:")
                        st.write(ai_reply)
                        
                except Exception as e:
                    st.error(f"একটি সমস্যা হয়েছে: {e}")
        else:
            st.warning("অনুগ্রহ করে কোনো প্রশ্ন বা নির্দেশনা লিখুন।")
