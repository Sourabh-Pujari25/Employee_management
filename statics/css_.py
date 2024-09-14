# Sidebar hide
import streamlit as st

def sidebar_hide():
    st.markdown(f"""<style>[class="st-emotion-cache-6qob1r eczjsme11"]{{display:none;}}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[class="st-emotion-cache-1gv3huu eczjsme18"]{{display:none;}}</style>""",unsafe_allow_html=True)
def header_hide():
    st.markdown(f"""<style>[class="st-emotion-cache-12fmjuu ezrtsby2"]{{display:none;}}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[class="st-emotion-cache-12fmjuu ezrtsby2"]{{display:none;}}</style>""",unsafe_allow_html=True)
def hide_pages():
    st.markdown(f"""<style>[class="st-emotion-cache-j7qwjs eczjsme15"]{{display:none; }}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[class="st-emotion-cache-1mi2ry5 eczjsme9"]{{display:none; }}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[data-testid="stSidebarNavSeparator"]{{display:none; }}</style>""",unsafe_allow_html=True)
def sidebar_colour():
    st.markdown(f"""<style>[class="st-emotion-cache-6qob1r eczjsme11"]{{background: linear-gradient(135deg, #053C47 0%, #078A97 100%, #078A97 100%);}}</style>""",unsafe_allow_html=True)
def margin_top():
    st.markdown(f"""<style>[class="block-container st-emotion-cache-1jicfl2 ea3mdgi5"]{{margin-top:-150px; }}</style>""",unsafe_allow_html=True)

def divider_space():
    st.markdown(' <div style="height: 27px; visibility: hidden;">< div>', unsafe_allow_html=True)

def sidebar_col():
    st.markdown(f"""<style>[class="st-emotion-cache-6qob1r eczjsme11"]{{
               background: linear-gradient(135deg, #053c47, #078a97);
    }}</style>""",unsafe_allow_html=True)


def hide_pages_sb():
    st.markdown(f"""<style>[class="st-emotion-cache-79elbk eczjsme17"]{{
               display: none;
    }}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[class="st-emotion-cache-1mi2ry5 eczjsme9"]{{
               display: none;
    }}</style>""",unsafe_allow_html=True)

def hide_header_top():
    st.markdown(f"""<style>[class="st-emotion-cache-12fmjuu ezrtsby2"]{{
               display: none;
    }}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[class="st-emotion-cache-12fmjuu ezrtsby2"]{{
               display: none;
    }}</style>""",unsafe_allow_html=True)

def padding_page_top():
    st.markdown(f"""<style>[class="block-container st-emotion-cache-1jicfl2 ea3mdgi5"]{{
               padding-top: 0px;
    }}</style>""",unsafe_allow_html=True)
    

# if __name__=="__main__":
#     css()