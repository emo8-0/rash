import streamlit as st
import requests
import pycountry
from datetime import datetime

st.set_page_config(page_title="Social Info Tool")

st.title("Social Media Info Tool (TikTok Example)")

username = st.text_input("ادخل اسم المستخدم على TikTok")

if st.button("احصل على المعلومات"):
    if username:
        fm = username.replace("@", "")
        headers = {
            "Host": "www.tiktok.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept-language": "en-US,en;q=0.9"
        }
        try:
            tikinfo = requests.get(f'https://www.tiktok.com/@{fm}', headers=headers).text
            getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]

            id = getting.split('id":"')[1].split('",')[0]
            name = getting.split('nickname":"')[1].split('",')[0]
            bio = getting.split('signature":"')[1].split('",')[0]
            country = getting.split('region":"')[1].split('",')[0]
            followers = getting.split('followerCount":')[1].split(',"')[0]
            following = getting.split('followingCount":')[1].split(',"')[0]
            like = getting.split('heart":')[1].split(',"')[0]
            video = getting.split('videoCount":')[1].split(',"')[0]

            try:
                countryn = str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
            except:
                countryn = country

            st.success(f"""
**TikTok Info**
Name: {name}  
ID: {id}  
Username: @{fm}  
Followers: {followers}  
Following: {following}  
Likes: {like}  
Videos: {video}  
Country: {countryn}  
Bio: {bio}  
URL: https://www.tiktok.com/@{fm}
""")
        except Exception as e:
            st.error("حدث خطأ! تحقق من اسم المستخدم وحاول مرة أخرى")
    else:
        st.warning("ادخل اسم المستخدم أولاً")
