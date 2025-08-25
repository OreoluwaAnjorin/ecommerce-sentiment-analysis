# E-commerce Sentiment Analysis using J48 Decision Tree

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![WEKA 3.8+](https://img.shields.io/badge/WEKA-3.8+-green.svg)](https://www.cs.waikato.ac.nz/ml/weka/)

> Machine learning sentiment classifier for e-commerce reviews using J48 decision tree algorithm. Automated web scraping, text preprocessing, and WEKA implementation achieving **95.9% training accuracy**.

##  Overview

End-to-end sentiment analysis pipeline that scrapes customer reviews from Jumia Nigeria and classifies them as positive or negative using J48 decision tree in WEKA.

**Key Results**: 95.9% training accuracy | 87.0% test accuracy | 1,100+ reviews processed

##  Project Structure

```
ecommerce-sentiment-analysis/
├── 📄 README.md                               # This file
├── 📄 summary.md                              # Detailed project summary
├── 📄 requirements.txt                        # Python dependencies
├── 🐍 scrapper.py                            # Web scraping script
│
├── 📂 Scrapped Files/                         # Raw scraped data
│   ├── Nivea_men_reviews.txt                 # Training dataset (1,000 reviews)
│   └── nivea_test.txt                         # Test dataset (100+ reviews)
│
├── 📂 Scrapping code/                         # Scraping implementation
├── 📂 Sentiment-analysis-jpegs/              # Visualization outputs
└── 📄 SENTIMENT ANALYSIS PROJECT REPORT.pdf  # Complete analysis report
```

##  Quick Start

### Prerequisites
- Python 3.x
- WEKA 3.8+ 
- Java 8+ (for WEKA)

### Installation & Usage

1. **Clone and install**
   ```bash
   git clone https://github.com/OreoluwaAnjorin/ecommerce-sentiment-analysis.git
   cd ecommerce-sentiment-analysis
   pip install -r requirements.txt
   ```

2. **Collect data**
   ```bash
   python scrapper.py
   ```

3. **Run analysis in WEKA**
   - Load ARFF data in WEKA Explorer
   - Apply StringToWordVector filter
   - Use J48 classifier with default settings
   - Evaluate with 10-fold cross-validation

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.x |
| **ML Platform** | WEKA 3.8+ |
| **Web Scraping** | Beautiful Soup, Requests |
| **Algorithm** | J48 Decision Tree |
| **Data Format** | ARFF |

##  Key Results

- **Training Accuracy**: 95.9% (959/1,000 reviews)
- **Test Accuracy**: 87.0% (87/100 reviews) 
- **Kappa Statistic**: 0.8423 (substantial agreement)
- **Dataset**: 1,100+ unique Jumia Nigeria reviews

*For detailed methodology, performance metrics, and analysis, see [summary.md](summary.md) and the project report.*

##  Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push and create Pull Request

##  License

MIT License - see [LICENSE](LICENSE) file for details.

##  Author

**Oreoluwa Anjorin**
- 📧 [anjorinoreoluwa19@gmail.com](mailto:anjorinoreoluwa19@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/oreoluwa-anjorin-69a4441aa/)
- 🐙 [@OreoluwaAnjorin](https://github.com/OreoluwaAnjorin)

---

⭐ **Star this repo if you found it helpful!**
