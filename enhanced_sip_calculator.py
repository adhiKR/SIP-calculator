import streamlit as st

def sip_calculator(yearly_investment, annual_return_rate, years):
    """
    Calculate the future value of SIP investments with yearly compounding.

    :param yearly_investment: The total invested every year (in currency units).
    :param annual_return_rate: The expected annual return rate (in percentage).
    :param years: The investment period in years.
    :return: Future value of the SIP investment.
    """
    # Convert annual return rate to a decimal
    annual_rate = annual_return_rate / 100
    # Initialize future value
    future_value = 0

    # Loop through each year, adding yearly investments and applying interest
    for year in range(1, years + 1):
        future_value += yearly_investment * (1 + annual_rate) ** (years - year + 1)
    
    return future_value

# Streamlit app
st.title("SIP Calculator")
st.write("Know how much your systematic investments worth over a given period of time.")

# Input fields for the user
monthly_investment = st.number_input("Monthly Investment Amount (₹):", min_value=0.0, value=5000.0, step=1000.0)
annual_return_rate = st.number_input("Expected Annual Return Rate (%):", min_value=0.0, max_value=100.0, value=12.0, step=1.0)
years = st.slider("Investment Tenure (Years):", min_value=1, max_value=50, value=10)

# Button to calculate the SIP future value
if st.button("Calculate"):
    # Calculate yearly investment
    yearly_investment = monthly_investment * 12
    # Calculate future value using the modified SIP formula
    future_value = sip_calculator(yearly_investment, annual_return_rate, years)
    
    # Total investment calculation
    total_investment = yearly_investment * years
    # Total returns calculation
    total_returns = future_value - total_investment
    # Total returns percentage
    total_returns_percent = (total_returns / total_investment) * 100

    # Display results
    st.success(f"Future Value of SIP Investment: ₹{future_value:,.2f}")
    st.info(f"Total Investment: ₹{total_investment:,.2f}")
    st.success(f"Total Returns ({total_returns_percent:.2f}%): ₹{total_returns:,.2f}")

# Additional info (Formula used)
st.write("**Formula Used:**")
st.latex(r"FV = P \times (1 + r)^n")
st.write("""- \(P\): Yearly investment (monthly investment \(\times\) 12)  
- \(r\): Annual return rate (as a decimal, i.e., annual return rate / 100)  
- \(n\): Total number of years
""")
