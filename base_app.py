"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os
import matplotlib.pyplot as plt

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl", "rb")
# loading your vectorizer from the pkl file
tweet_cv = joblib.load(news_vectorizer)

# Load your raw data
raw = pd.read_csv("resources/train.csv")
sentiment = ["1", "2", "0", "-1"]

# The main function where we will build the actual app


def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages

	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Home", "About", "Features", "Model", "Contact Us"]
	selection = st.sidebar.selectbox("",options)

	# Building out the "About" page
	if selection == "About":
		st.title("About")
		# You can read a markdown file from supporting resources folder
		st.subheader("Background")
		st.markdown("Many companies are built around lessening one’s environmental impact or carbon footprint. They offer products and services that are environmentally friendly and sustainable, in line with their values and ideals. They would like to determine how people perceive climate change and whether or not they believe it is a real threat. This would add to their market research efforts in gauging how their product/service may be received. ")
		st.subheader("How to Make a Prediction")
		st.markdown("The following steps will provide you with a seamless interaction with our tweet classifiction app.")

	# Building out the "Features" page
	if selection == "Features":
		st.title("Features")
		st.subheader("Sentiments")
		# You can read a markdown file from supporting resources folder
		st.markdown("2 = News : Tweets linked to factual news about climate change.")
		st.markdown("1 = Pro : Tweets that support the belief of man-made climate change.")
		st.markdown("0 = Neutral : Tweets that neither support nor refuse beliefs of climate change.")
		st.markdown("-1 = Anti : Tweets that do not support the belief of man-made climate change.")

		st.subheader("Pie chart distribution of sentiments in percentage")
        
		labels = 'Pro', 'News', 'Neutral', 'Anti'
		sizes = [8530, 3640, 2353, 1296]
		explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%0.1f%%',
        shadow=True, startangle=90)
		ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

		st.pyplot(fig1)

	# Building out the "Model" page
	if selection == "Model":
		st.title("Model")
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some information here")

	# Building out the "Contact Us" page
	if selection == "Contact Us":
		st.title("Contact Us")
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some information here")

	# Building out the Home page
	if selection == "Home":
		st.title("Tweet Classifer")

		option = st.sidebar.multiselect(
     	'Sentiment:',
     	('Pro', 'News', 'Neutral', 'Anti'))

		st.info("Prediction with ML Models")
		# Creating a text box for user input
		tweet_text = st.text_area("Enter Text","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

		st.subheader("Raw Twitter data and label")
		if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			st.write(raw[['sentiment', 'message']]) # will write the df to the page

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
