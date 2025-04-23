import streamlit as st
import re

st.set_page_config(page_title="Password Strengther" , page_icon="🔒")

st.title("🔒 Password Strength Analyzer")
st.markdown("""
## Welcome to StrongPass! Let’s make your passwords hacker-proof. 
In just a few seconds, we’ll help you check your password’s strength and make it **better—stronger, smarter, and safer**. Whether you're securing one account or many, you're in control. Let's get started!""")

get_password = st.text_input("Enter your password", type="password")

message = []
point = 0

if get_password:
    if len(get_password) >= 8:
        point += 1
    else:
        message.append("🚫 Password should be at least 8 characters long")
    
    if re.search(r"[A-Z]", get_password) and re.search(r"[a-z]", get_password):
        point += 1
    else:
        message.append("🚫 Password should be stronger. Try mixing uppercase and lowercase letters.")

    if re.search(r'\d',get_password):
        point += 1
    else:
        message.append("🚫 Password should contain at least one digit")

    if re.search(r'[!@#$%&_]',get_password):
        point += 1
    else:
        message.append("🚫 Password should contain at least one special character --- (!@#$%&_)")

    if point == 4:
        message.append("🟢 **Well done! Your password is now strong enough to resist most attacks.**")
    elif point == 3:
        message.append("🟡 **Solid progress! Now just add a few twists to reach strong territory.**")
    else:
        message.append("🔴 **This password is dangerously weak and exposed. Secure your account by creating a stronger password now!**")

    if message:
        st.markdown("### Improve Your Password")
    for msg in message:
        st.write(msg)

else:
    st.info("Please enter your password to get started..")