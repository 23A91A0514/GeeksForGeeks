import pandas as pd

class Solution:
    def dailyProductsAndCustomers(self, activities: pd.DataFrame) -> pd.DataFrame:
        
        result = activities.groupby(['date_id', 'store_name']).agg(
            unique_products=('product_id', 'nunique'),
            unique_customers=('customer_id', 'nunique')
        ).reset_index()
        
        return result