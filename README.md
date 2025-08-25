# Customer Review Sentiment Analysis using J48 Decision Tree

A machine learning project that automatically classifies customer reviews as positive or negative using the J48 decision tree algorithm implemented in WEKA.

## Project Overview

This project implements an end-to-end sentiment analysis pipeline for e-commerce customer reviews. The system scrapes product reviews from Jumia Nigeria, processes the text data, and uses machine learning to classify sentiment with high accuracy.

### Key Features
- **Automated Web Scraping**: Custom Python scraper for collecting 1,100+ unique reviews
- **Intelligent Text Processing**: Advanced preprocessing with duplicate removal and quality filtering
- **Machine Learning Classification**: J48 decision tree implementation via WEKA
- **Robust Evaluation**: Both cross-validation and independent test set validation
- **High Performance**: 95.9% training accuracy and 87.0% test accuracy

## Technical Stack

- **Programming Language**: Python 3.x
- **Machine Learning Platform**: WEKA 3.8+
- **Web Scraping**: Beautiful Soup, Requests
- **Data Format**: ARFF (Attribute-Relation File Format)
- **Algorithm**: J48 Decision Tree (C4.5 implementation)

## Dataset

- **Source**: Jumia Nigeria e-commerce platform
- **Total Reviews**: 1,100+ unique customer reviews
- **Training Set**: 1,000 reviews
- **Test Set**: 100+ reviews
- **Products**: Multiple Nivea Men products and power banks
- **Languages**: Primarily English with some Nigerian pidgin

## Project Structure

```
sentiment-analysis/
├── README.md
├── summary.md
├── requirements.txt
├── scrapper.py                    # Web scraping script
├── Nivea_men_reviews.txt         # Training dataset (1,000 reviews)
├── nivea_test.txt               # Test dataset (100+ reviews)
└── SENTIMENT ANALYSIS PROJECT REPORT.pdf
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis
   cd sentiment-analysis
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install WEKA**
   - Download WEKA 3.8+ from [official website](https://www.cs.waikato.ac.nz/ml/weka/)
   - Ensure Java 8+ is installed

## Usage

### Data Collection
Run the web scraper to collect fresh reviews:
```bash
python scrapper.py
```

### WEKA Implementation

1. **Launch WEKA Explorer**
2. **Load Data**: Import the ARFF formatted training data
3. **Preprocess**: Apply StringToWordVector filter for text conversion
4. **Classify**: Select J48 algorithm from Trees category
5. **Evaluate**: Run 10-fold cross-validation or test on independent set

### Key WEKA Settings
- **Classifier**: J48 Decision Tree
- **Confidence Factor**: 0.25
- **Minimum Objects per Leaf**: 2
- **Pruning**: Enabled
- **Text Processing**: StringToWordVector filter

## Results & Performance

### Training Performance (Cross-Validation)
- **Accuracy**: 95.9% (959/1000 correct classifications)
- **Kappa Statistic**: 0.8423 (substantial agreement)
- **Precision**: 96.6% (positive), 91.7% (negative)
- **Recall**: 98.6% (positive), 82.1% (negative)
- **F-Measure**: 97.6% (positive), 86.6% (negative)

### Test Set Performance
- **Accuracy**: 87.0% (87/100 correct classifications)
- **Model Build Time**: 0.51 seconds
- **Prediction Time**: 0.02 seconds

### Decision Tree Characteristics
- **Number of Leaves**: 55
- **Tree Size**: 109 nodes
- **Key Decision Features**: Product quality terms, satisfaction indicators

## Methodology

### Data Collection Strategy
1. **Multi-product Approach**: Targeted 5 different product pages
2. **Quality Filtering**: Length filters (20-1000 characters) and relevance checks
3. **Duplicate Handling**: Automatic elimination using set-based storage
4. **Respectful Scraping**: 2-second delays between requests

### Sentiment Labeling
- **Lexicon-based Classification**: Automated labeling using sentiment indicators
- **Positive Keywords**: good, great, excellent, amazing, perfect, love, recommend
- **Negative Keywords**: bad, terrible, poor, disappointing, problem, issue
- **Scoring System**: (positive_count - negative_count) determines sentiment

### Text Preprocessing
1. **ARFF Conversion**: Transform raw text to WEKA-compatible format
2. **StringToWordVector**: Convert text to numerical feature vectors
3. **Bag-of-words**: Generate term frequency representations
4. **Quality Control**: Remove problematic punctuation and special characters

## Limitations & Future Improvements

### Current Limitations
1. **Class Imbalance**: Test set heavily skewed toward positive reviews
2. **Generalization Gap**: 8.9% accuracy drop from training to test
3. **Limited Negative Detection**: Poor recall for negative sentiment (0% in test)
4. **Simple Feature Engineering**: Basic bag-of-words approach

### Recommended Enhancements
1. **Balanced Dataset**: Collect equal positive and negative examples
2. **Advanced Preprocessing**: Implement stemming, lemmatization, and n-grams
3. **Ensemble Methods**: Explore Random Forest or gradient boosting
4. **Deep Learning**: Consider LSTM or BERT-based approaches
5. **Domain-Specific Features**: Develop e-commerce specific sentiment indicators

## Business Applications

- **Product Quality Monitoring**: Automated satisfaction tracking
- **Brand Reputation Management**: Real-time sentiment analysis
- **Customer Service Optimization**: Priority flagging of negative feedback
- **Product Development**: Data-driven improvement insights

## Technical Challenges Solved

1. **ARFF Format Issues**: Resolved file recognition problems through systematic cleaning
2. **Text-to-Feature Conversion**: Successful implementation of StringToWordVector
3. **Duplicate Management**: Efficient handling of repeated review content
4. **Cross-platform Compatibility**: Ensured consistent performance across systems

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Oreoluwa Anjorin**
- Email: [anjorinoreoluwa19@gmail.com]
- LinkedIn: [(https://www.linkedin.com/in/oreoluwa-anjorin-69a4441aa/)]

## Contact

For questions, suggestions, or collaboration opportunities, please reach out via email or LinkedIn.

---

*This project demonstrates practical application of machine learning to real-world text classification challenges, providing a foundation for automated customer feedback analysis systems.*
