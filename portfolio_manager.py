import streamlit as st
import pandas as pd
import yfinance as yf

class PortfolioManager:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Stock', 'Quantity', 'Purchase Price', 'Current Value'])
    
    def display_portfolio_management(self):
        # Add Stock to Portfolio
        st.subheader("إضافة سهم جديد")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            stock_symbol = st.text_input("رمز السهم")
        with col2:
            quantity = st.number_input("الكمية", min_value=0)
        with col3:
            purchase_price = st.number_input("سعر الشراء", min_value=0.0)
        with col4:
            st.write(" ")
            if st.button("إضافة"):
                self._add_stock(stock_symbol, quantity, purchase_price)
        
        # Display Portfolio
        st.subheader("محفظتك الحالية")
        if not self.portfolio.empty:
            st.dataframe(self.portfolio)
        else:
            st.info("لا توجد أسهم في محفظتك حتى الآن")
    
    def _add_stock(self, symbol, quantity, purchase_price):
        if symbol and quantity > 0 and purchase_price > 0:
            # Fetch current stock price
            try:
                stock = yf.Ticker(symbol)
                current_price = stock.history(period="1d")['Close'].iloc[-1]
                
                # Add to portfolio
                new_stock = pd.DataFrame({
                    'Stock': [symbol],
                    'Quantity': [quantity],
                    'Purchase Price': [purchase_price],
                    'Current Value': [current_price * quantity]
                })
                
                self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
                st.success(f"تمت إضافة {symbol} بنجاح!")
            except Exception as e:
                st.error(f"خطأ في إضافة السهم: {e}")
        else:
            st.warning("يرجى إدخال معلومات صحيحة للسهم")
