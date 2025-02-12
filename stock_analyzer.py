import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class StockAnalyzer:
    def display_stock_analysis(self):
        # Stock Symbol Input
        stock_symbol = st.text_input("أدخل رمز السهم (مثل AAPL, GOOGL)", value="AAPL")
        
        if stock_symbol:
            try:
                # Fetch Stock Data
                stock = yf.Ticker(stock_symbol)
                stock_data = stock.history(period="1y")
                
                # Create Subplot
                fig = make_subplots(rows=2, cols=1, 
                    subplot_titles=(f"سعر السهم {stock_symbol}", "حجم التداول"),
                    vertical_spacing=0.1)
                
                # Price Chart
                fig.add_trace(
                    go.Candlestick(
                        x=stock_data.index,
                        open=stock_data['Open'],
                        high=stock_data['High'],
                        low=stock_data['Low'],
                        close=stock_data['Close'],
                        name='أسعار'
                    ),
                    row=1, col=1
                )
                
                # Volume Chart
                fig.add_trace(
                    go.Bar(x=stock_data.index, y=stock_data['Volume'], name='حجم التداول'),
                    row=2, col=1
                )
                
                fig.update_layout(height=600, title_text=f"تحليل السهم {stock_symbol}")
                st.plotly_chart(fig)
                
                # Stock Information
                st.subheader("معلومات الشركة")
                info = stock.info
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("السعر الحالي", f"{info.get('currentPrice', 'غير متوفر')} $")
                    st.metric("القيمة السوقية", f"{info.get('marketCap', 'غير متوفر')} $")
                
                with col2:
                    st.metric("نسبة الربحية", f"{info.get('trailingPE', 'غير متوفر')}")
                    st.metric("توزيعات الأرباح", f"{info.get('dividendRate', 'غير متوفر')} $")
                
            except Exception as e:
                st.error(f"خطأ في جلب بيانات السهم: {e}")
    
    def display_investment_recommendations(self):
        st.write("سيتم تقديم توصيات استثمارية ذكية باستخدام تحليل البيانات التاريخية")
        
        # Example sectors for diversification
        sectors = {
            "التكنولوجيا": ["AAPL", "MSFT", "GOOGL"],
            "الطاقة": ["XOM", "CVX"],
            "الصحة": ["JNJ", "PFE"],
            "المالية": ["JPM", "BAC"]
        }
        
        st.subheader("توصيات التنويع")
        for sector, stocks in sectors.items():
            st.write(f"**{sector}**")
            for stock in stocks:
                try:
                    ticker = yf.Ticker(stock)
                    recommendation = ticker.recommendations.iloc[-1] if not ticker.recommendations.empty else "لا توجد توصية"
                    st.write(f"{stock}: {recommendation}")
                except Exception as e:
                    st.write(f"{stock}: خطأ في جلب التوصية")
