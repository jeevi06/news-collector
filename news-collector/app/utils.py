# app/utils.py
from app.models import Article
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import FreqDist
import nltk
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 


# Configure logging
logging.basicConfig(filename='news_collector.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Download NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

def parse_and_process_article(article_data):
    try:
        # Implement parsing and processing logic here
        # Extract title, content, publication date, source URL, etc.
        # Perform NLP classification
        # Update database with the assigned category

        
        new_article = Article(
            title=article_data['title'],
            content=article_data['content'],
            publication_date=datetime.now(),
            source_url=article_data['source_url'],
            category=classify_article(article_data['content'])
        )
        save_article(new_article)
    except Exception as e:
        logging.error(f"Error processing article: {str(e)}")

def save_article(article):
    try:
        # Implement database storage logic
        # e.g., using SQLAlchemy with MySQL
        engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/newsarticle')
        declarative_base.metadata.create_all(engine)

        with engine.connect() as connection:
            connection.execute(
                Article.__table__.insert().values(
                    title=article.title,
                    content=article.content,
                    publication_date=article.publication_date,
                    source_url=article.source_url,
                    category=article.category
                )
            )
        logging.info("Article saved successfully.")
    except Exception as e:
        logging.error(f"Error saving article to the database: {str(e)}")

def classify_article(content):
    try:
        # Implement basic text classification logic
        # e.g., using NLTK to classify articles into predefined categories

        words = word_tokenize(content)
        words = [word.lower() for word in words if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

        ps = PorterStemmer()
        words = [ps.stem(word) for word in words]

        freq_dist = FreqDist(words)
        most_common_word = freq_dist.max()

        if most_common_word in ['terror', 'protest', 'unrest', 'riot']:
            return 'Terrorism/Protest/Political Unrest/Riot'
        elif most_common_word in ['happy', 'positive', 'uplifting']:
            return 'Positive/Uplifting'
        elif most_common_word in ['disaster', 'natural disaster']:
            return 'Natural Disasters'
        else:
            return 'Other'
    except Exception as e:
        logging.error(f"Error classifying article: {str(e)}")
        return 'Other'  # Default to 'Other' category in case of classification error
