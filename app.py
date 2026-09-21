import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Simran AI Assistant", page_icon="🤖")

st.title("🤖 সিমরান (Simran) - AI Assistant")
st.write("আপনার ডিজিটাল কাজের বিশ্বস্ত এআই সহকারী (OpenAI Powered)।")

# Sidebar for OpenAI API Key
st.sidebar.header("সেটিংস (Settings)")
api_key = st.sidebar.text_input("OpenAI API Key দিন (sk-...):", type="password")

if not api_key:
    st.info("👈 শুরু করতে বাম পাশের সাইডবারে আপনার OpenAI API Key টি বসান।")
else:
    # User Input
    user_prompt = st.text_area("আপনার প্রশ্ন বা নির্দেশ লিখুন:", height=100)
    
    if st.button("উত্তর দিন (Send)"):
        if user_prompt:
            with st.spinner("সিমরান চিন্তা করছে..."):
                try:
                    # OpenAI API Endpoint
                    url = "https://api.openai.com/v1/chat/completions"
                    
                    headers = {
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {api_key}'
                    }
                    
                    data = {
                        "model": "gpt-4o-mini",
                        "messages": [{"role": "user", "content": user_prompt}]
                    }
                    
                    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
                    
                    with urllib.request.urlopen(req) as response:
                        res_data = json.loads(response.read().decode('utf-8'))
                        ai_reply = res_data['choices'][0]['message']['content']
                        
                        st.success("উত্তর:")
                        st.write(ai_reply)
                        
                except Exception as e:
                    st.error(f"একটি সমস্যা হয়েছে: {e}")
        else:
            st.warning("অনুগ্রহ করে কোনো প্রশ্ন বা নির্দেশনা লিখুন।")
