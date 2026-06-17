import streamlit as st
import requests

API_KEY = "827715ada2594813a67ac2baeab77b56"

st.set_page_config(
    page_title="News Search App",
    page_icon="",
    layout="wide"
)

st.title(" AI News Search App")

search_term = st.text_input(
    "Enter a topic",
    value="tesla"
)

if st.button("Search News"):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": search_term,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 20,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    st.write("Status:", data.get("status"))
    st.write("Total Results:", data.get("totalResults"))

    if data.get("status") != "ok":
        st.error(data.get("message"))
    else:
        articles = data.get("articles", [])

        if not articles:
            st.warning("No news found.")
        else:
            for article in articles:

                col1, col2 = st.columns([1, 3])

                with col1:
                    if article.get("urlToImage"):
                        st.image(article["urlToImage"])

                with col2:
                    st.subheader(article["title"])

                    st.write(
                        article.get(
                            "description",
                            "No description available."
                        )
                    )

                    st.write(
                        f"Source: {article['source']['name']}"
                    )

                    st.write(
                        f"Published: {article['publishedAt']}"
                    )

                    st.link_button(
                        "Read Full Article",
                        article["url"]
                    )

                st.divider()