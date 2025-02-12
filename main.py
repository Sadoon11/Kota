import streamlit as st
from src.portfolio_manager import PortfolioManager
from src.stock_analyzer import StockAnalyzer
from src.risk_calculator import RiskCalculator

def main():
    st.title("الاستثمار الذكي - Investment Intelligence")
    
    # Sidebar navigation
    menu = st.sidebar.selectbox("القائمة الرئيسية", 
        [
            "إدارة المحفظة", 
            "تحليل الأسهم", 
            "تقييم المخاطر", 
            "توصيات الاستثمار"
        ])
    
    # Initialize managers
    portfolio_manager = PortfolioManager()
    stock_analyzer = StockAnalyzer()
    risk_calculator = RiskCalculator()
    
    # Main application logic
    if menu == "إدارة المحفظة":
        st.header("إدارة المحفظة الاستثمارية")
        portfolio_manager.display_portfolio_management()
    
    elif menu == "تحليل الأسهم":
        st.header("تحليل أداء الأسهم")
        stock_analyzer.display_stock_analysis()
    
    elif menu == "تقييم المخاطر":
        st.header("تقييم مخاطر الاستثمار")
        risk_calculator.display_risk_assessment()
    
    elif menu == "توصيات الاستثمار":
        st.header("توصيات الاستثمار الذكية")
        stock_analyzer.display_investment_recommendations()

if __name__ == "__main__":
    main()
