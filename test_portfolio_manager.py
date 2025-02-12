import pytest
import pandas as pd
from src.portfolio_manager import PortfolioManager

def test_portfolio_manager_initialization():
    """Test that PortfolioManager initializes with an empty DataFrame."""
    portfolio_manager = PortfolioManager()
    assert portfolio_manager.portfolio.empty
    assert list(portfolio_manager.portfolio.columns) == ['Stock', 'Quantity', 'Purchase Price', 'Current Value']

def test_add_stock():
    """Test adding a stock to the portfolio."""
    portfolio_manager = PortfolioManager()
    
    # Simulate adding a stock
    portfolio_manager._add_stock('AAPL', 10, 150.0)
    
    assert not portfolio_manager.portfolio.empty
    assert len(portfolio_manager.portfolio) == 1
    assert portfolio_manager.portfolio.iloc[0]['Stock'] == 'AAPL'
    assert portfolio_manager.portfolio.iloc[0]['Quantity'] == 10
    assert portfolio_manager.portfolio.iloc[0]['Purchase Price'] == 150.0
