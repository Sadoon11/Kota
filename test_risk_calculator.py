import pytest
from src.risk_calculator import RiskCalculator

def test_determine_risk_profile():
    """Test risk profile determination based on score."""
    risk_calculator = RiskCalculator()
    
    # Test different score ranges
    assert risk_calculator._determine_risk_profile(10) == "محافظ جداً"
    assert risk_calculator._determine_risk_profile(20) == "محافظ"
    assert risk_calculator._determine_risk_profile(30) == "معتدل"
    assert risk_calculator._determine_risk_profile(40) == "مغامر"

def test_asset_allocation():
    """Test asset allocation for different risk profiles."""
    risk_calculator = RiskCalculator()
    
    # Test each risk profile's allocation
    conservative = risk_calculator._get_asset_allocation("محافظ جداً")
    assert conservative["السندات الحكومية"] == 70
    assert conservative["النقد"] == 20
    assert conservative["الأسهم"] == 10

    aggressive = risk_calculator._get_asset_allocation("مغامر")
    assert aggressive["السندات الحكومية"] == 10
    assert aggressive["النقد"] == 10
    assert aggressive["الأسهم"] == 80
