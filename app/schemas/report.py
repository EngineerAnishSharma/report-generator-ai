# from pydantic import BaseModel, Field
# from typing import List


# # ------------------ Key Metrics ------------------ #
# class KeyMetrics(BaseModel):
#     total_rows: int = Field(..., example=12)
#     average_revenue: float = Field(..., example=109833.33)
#     average_units_sold: float = Field(..., example=418.33)
#     average_marketing_spend: float = Field(..., example=13583.33)

#     revenue_std_dev: float = Field(..., example=17652.37)
#     units_sold_std_dev: float = Field(..., example=52.54)
#     marketing_spend_std_dev: float = Field(..., example=2382.07)

#     min_revenue: float = Field(..., example=87000.0)
#     max_revenue: float = Field(..., example=145000.0)
#     min_units_sold: float = Field(..., example=340.0)
#     max_units_sold: float = Field(..., example=520.0)
#     min_marketing_spend: float = Field(..., example=10000.0)
#     max_marketing_spend: float = Field(..., example=18000.0)


# # ------------------ Trends & Correlations ------------------ #
# class TrendsAndCorrelations(BaseModel):
#     observations: str = Field(
#         ...,
#         example="Revenue shows a positive upward trend with increased marketing spend."
#     )
#     potential_correlations: str = Field(
#         ...,
#         example="Higher marketing spend correlates with higher units sold."
#     )


# # ------------------ Recommendations ------------------ #
# class Recommendations(BaseModel):
#     action_items: List[str] = Field(
#         ...,
#         example=[
#             "Increase marketing spend during high-performing months.",
#             "Focus sales efforts on regions with higher conversion rates."
#         ]
#     )


# # ------------------ Summary ------------------ #
# class Summary(BaseModel):
#     overview: str = Field(
#         ...,
#         example="Overall performance is strong with consistent growth across all key metrics."
#     )


# # ------------------ Final Report ------------------ #
# class Report(BaseModel):
#     key_metrics: KeyMetrics
#     trends_and_correlations: TrendsAndCorrelations
#     recommendations: Recommendations
#     summary: Summary


# # ------------------ API Response Wrapper ------------------ #
# class ReportResponse(BaseModel):
#     report: Report
