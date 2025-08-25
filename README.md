Customer Review Sentiment Analysis using J48 Decision Tree
A machine learning project that automatically classifies customer reviews as positive or negative using the J48 decision tree algorithm implemented in WEKA.
Project Overview
This project implements an end-to-end sentiment analysis pipeline for e-commerce customer reviews. The system scrapes product reviews from Jumia Nigeria, processes the text data, and uses machine learning to classify sentiment with high accuracy.
Key Features

Automated Web Scraping: Custom Python scraper for collecting 1,100+ unique reviews
Intelligent Text Processing: Advanced preprocessing with duplicate removal and quality filtering
Machine Learning Classification: J48 decision tree implementation via WEKA
Robust Evaluation: Both cross-validation and independent test set validation
High Performance: 95.9% training accuracy and 87.0% test accuracy

Technical Stack

Programming Language: Python 3.x
Machine Learning Platform: WEKA 3.8+
Web Scraping: Beautiful Soup, Requests
Data Format: ARFF (Attribute-Relation File Format)
Algorithm: J48 Decision Tree (C4.5 implementation)

Dataset

Source: Jumia Nigeria e-commerce platform
Total Reviews: 1,100+ unique customer reviews
Training Set: 1,000 reviews
Test Set: 100+ reviews
Products: Multiple Nivea Men products and power banks
Languages: Primarily English with some Nigerian pidgin

Project Structure
sentiment-analysis/
├── README.md
├── summary.md
├── requirements.txt
├── scrapper.py                    # Web scraping script
├── Nivea_men_reviews.txt         # Training dataset (1,000 reviews)
├── nivea_test.txt               # Test dataset (100+ reviews)
└── SENTIMENT ANALYSIS PROJECT REPORT.pdf
Installation & Setup

Clone the repository
bashgit clone https://github.com/yourusername/sentiment-analysis
cd sentiment-analysis

Install Python dependencies
bashpip install -r requirements.txt

Install WEKA

Download WEKA 3.8+ from official website
Ensure Java 8+ is installed



Usage
Data Collection
Run the web scraper to collect fresh reviews:
bashpython scrapper.py
WEKA Implementation

Launch WEKA Explorer
Load Data: Import the ARFF formatted training data
Preprocess: Apply StringToWordVector filter for text conversion
Classify: Select J48 algorithm from Trees category
Evaluate: Run 10-fold cross-validation or test on independent set

Key WEKA Settings

Classifier: J48 Decision Tree
Confidence Factor: 0.25
Minimum Objects per Leaf: 2
Pruning: Enabled
Text Processing: StringToWordVector filter

Results & Performance
Training Performance (Cross-Validation)

Accuracy: 95.9% (959/1000 correct classifications)
Kappa Statistic: 0.8423 (substantial agreement)
Precision: 96.6% (positive), 91.7% (negative)
Recall: 98.6% (positive), 82.1% (negative)
F-Measure: 97.6% (positive), 86.6% (negative)

Test Set Performance

Accuracy: 87.0% (87/100 correct classifications)
Model Build Time: 0.51 seconds
Prediction Time: 0.02 seconds

Decision Tree Characteristics

Number of Leaves: 55
Tree Size: 109 nodes
Key Decision Features: Product quality terms, satisfaction indicators

Methodology
Data Collection Strategy

Multi-product Approach: Targeted 5 different product pages
Quality Filtering: Length filters (20-1000 characters) and relevance checks
Duplicate Handling: Automatic elimination using set-based storage
Respectful Scraping: 2-second delays between requests

Sentiment Labeling

Lexicon-based Classification: Automated labeling using sentiment indicators
Positive Keywords: good, great, excellent, amazing, perfect, love, recommend
Negative Keywords: bad, terrible, poor, disappointing, problem, issue
Scoring System: (positive_count - negative_count) determines sentiment

Text Preprocessing

ARFF Conversion: Transform raw text to WEKA-compatible format
StringToWordVector: Convert text to numerical feature vectors
Bag-of-words: Generate term frequency representations
Quality Control: Remove problematic punctuation and special characters

Limitations & Future Improvements
Current Limitations

Class Imbalance: Test set heavily skewed toward positive reviews
Generalization Gap: 8.9% accuracy drop from training to test
Limited Negative Detection: Poor recall for negative sentiment (0% in test)
Simple Feature Engineering: Basic bag-of-words approach

Recommended Enhancements

Balanced Dataset: Collect equal positive and negative examples
Advanced Preprocessing: Implement stemming, lemmatization, and n-grams
Ensemble Methods: Explore Random Forest or gradient boosting
Deep Learning: Consider LSTM or BERT-based approaches
Domain-Specific Features: Develop e-commerce specific sentiment indicators

Business Applications

Product Quality Monitoring: Automated satisfaction tracking
Brand Reputation Management: Real-time sentiment analysis
Customer Service Optimization: Priority flagging of negative feedback
Product Development: Data-driven improvement insights

Technical Challenges Solved

ARFF Format Issues: Resolved file recognition problems through systematic cleaning
Text-to-Feature Conversion: Successful implementation of StringToWordVector
Duplicate Management: Efficient handling of repeated review content
Cross-platform Compatibility: Ensured consistent performance across systems

Contributing

Fork the repository
Create a feature branch (git checkout -b feature/improvement)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/improvement)
Create a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Author
Oreoluwa Anjorin

Email: [anjorinoreoluwa19@gmail.com]
LinkedIn: [https://www.linkedin.com/in/oreoluwa-anjorin-69a4441aa/]

Contact
For questions, suggestions, or collaboration opportunities, please reach out via email or LinkedIn.

This project demonstrates practical application of machine learning to real-world text classification challenges, providing a foundation for automated customer feedback analysis systems.
