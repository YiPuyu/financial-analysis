# financial-analysis

```markdown
# ETF Markets Analysis Toolkit

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Source](https://img.shields.io/badge/data-yfinance-green)](https://pypi.org/project/yfinance/)
[![GitHub stars](https://img.shields.io/github/stars/YiPuyu/financial-analysis.svg?style=social&label=Star)](https://github.com/YiPuyu/financial-analysis)

A Python-based quantitative analysis tool for studying the relationship between US and Japanese equity markets with currency effects. This project examines the correlation and regression dynamics between SPDR S&P 500 ETF (SPY), iShares MSCI Japan ETF (EWJ), and USD/JPY exchange rate.

## 📊 Project Overview

This toolkit provides:
- Automated data collection for ETFs and forex rates
- Correlation analysis between US and Japanese markets  
- Rolling correlation visualization
- Multivariate regression modeling with currency factors
- Professional financial charts for reporting

## 🚀 Features

- **Automated Data Pipeline**: Fetches daily price data from Yahoo Finance
- **Dual Analysis**: Studies both price trends and daily returns
- **Currency Integration**: Incorporates USD/JPY effects in regression models
- **Dynamic Visualization**: Generates scatter plots and rolling correlation charts
- **Statistical Modeling**: OLS regression with comprehensive summary outputs

## 📈 Key Findings

Based on analysis of 2023-2024 data:
- **Correlation Coefficient**: SPY vs EWJ = 0.4236 (moderate positive correlation)
- **Market Integration**: US and Japanese equities show significant co-movement  
- **Currency Impact**: USD/JPY fluctuations explain additional variation in EWJ returns
- **Practical Implication**: 42% correlation suggests meaningful diversification benefits

## 🛠 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/YiPuyu/financial-analysis.git
cd financial-analysis
