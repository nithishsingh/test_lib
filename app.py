import streamlit as st 



st.markdown("""
<style>
.responsive-iframe {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
}
.responsive-iframe iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)


iframe_code = f'''
<h2>Superstore PowerBI</h2>
<div class="responsive-iframe">
    <iframe title="Superstore PowerBI" src="https://app.powerbi.com/view?r=eyJrIjoiMTcxMWQ0NWUtOTg1Mi00YmYwLTg1NTUtMWU0MDc4OGI2ZjA2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>
</div>
'''
# Display the embedded Power BI report
st.markdown(iframe_code, unsafe_allow_html=True)