
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List

@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]

class CampaignBuilder:
    def __init__(self):
        self.name: Optional[str] = None
        self.channel: Optional[str] = None
        self.daily_budget: Optional[float] = None
        self.start_date: Optional[date] = None
        self.end_date: Optional[date] = None
        self.target_audience: Dict[str] = {}
        self.creatives: List[Dict[str, str]] = []
        self.tracking: Dict[str, str] = {}

    def with_name(self, name: str):
      if self.name is None:
        self.name = name
      return self

    def with_channel(self, channel: str):
      if self.channel is None:
        self.channel = channel
      return self

    def with_budget(self, daily_budget: float):
      if self.daily_budget is None:
        self.daily_budget = daily_budget
      return self

    def with_dates(self, start_date, end_date=None):
      if self.start_date is None:
        self.start_date = start_date
      if self.end_date is None:
        self.end_date = end_date
      return self

    def with_audience(self, **kwargs):
      if not self.target_audience:
        self.target_audience = kwargs
      return self

    def add_creative(self, headline: str, image_url: str):
        self.creatives.append({"headline": headline, "image_url": image_url})
        return self

    def with_tracking(self, **kwargs):
      if not self.tracking:
        self.tracking = kwargs
      return self

    def build(self) -> Campaign:
      if not self.name:
        raise ValueError("Campaign name is required.")
      if not self.channel:
        raise ValueError("Campaign channel is required.")
      if self.daily_budget is None or self.daily_budget <= 0:
        raise ValueError("Budget must be positive.")
      if self.start_date is None:
        raise ValueError("Start date is required.")
      if self.end_date is not None and self.start_date > self.end_date:
        raise ValueError("Start date cannot be after end date.")
      if not self.creatives:
        raise ValueError("At least one creative is required.")

      return Campaign(
        name=self.name, channel=self.channel, daily_budget=self.daily_budget, start_date=self.start_date,
        end_date=self.end_date, target_audience=dict(self.target_audience), creatives=self.creatives,
        tracking=dict(self.tracking))
