from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign

class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        # TODO: Create a campaign on this channel and return an external id.
        if not campaign.name:
            raise ValueError("Campaign name is required.")
        if not campaign.channel:
            raise ValueError("Campaign channel is required.")
        if not campaign.daily_budget or campaign.daily_budget <= 0:
            raise ValueError("Campaign daily budget must be positive.")
        if not campaign.start_date:
            raise ValueError("Campaign start date is required.")
        if not campaign.end_date:
            raise ValueError("Campaign end date is required.")
        if not campaign.creatives:
            raise ValueError("At least one creative is required.")
        if not campaign.target_audience:
            raise ValueError("Target audience is required.")
        if not campaign.tracking:
            raise ValueError("Tracking information is required.")

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        if not campaign_id:
            raise ValueError("Campaign ID is required.")
        return None

class GoogleAdsClient(ChannelClient):
    def create_campaign(self, campaign: Campaign) -> str:
        if not campaign.name:
            raise ValueError("Campaign name is required.")
        if not campaign.channel:
            raise ValueError("Campaign channel is required.")
        if not campaign.daily_budget or campaign.daily_budget <= 0:
            raise ValueError("Campaign daily budget must be positive.")
        if not campaign.start_date:
            raise ValueError("Campaign start date is required.")
        if not campaign.end_date:
            raise ValueError("Campaign end date is required.")
        if not campaign.creatives:
            raise ValueError("At least one creative is required.")
        return campaign
       
       
class FacebookAdsClient(ChannelClient):
    def createfacebook(self, campaign: ChannelClient) -> str:
        if not campaign.name:
            raise ValueError("Campaign name is required.")
        if not campaign.channel:
            raise ValueError("Campaign channel is required.")
        if not campaign.daily_budget or campaign.daily_budget <= 0:
            raise ValueError("Campaign daily budget must be positive.")
        if not campaign.start_date:
            raise ValueError("Campaign start date is required.")
        if not campaign.end_date:
            raise ValueError("Campaign end date is required.")
        if not campaign.creatives:
            raise ValueError("At least one creative is required.")
        return f"f-{uuid4()}"

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
      # TODO: Return the appropriate client based on the channel.
        if channel == "google":
            return GoogleAdsClient()
        if channel == "facebook":
            return FacebookAdsClient()
        else:
            raise ValueError
    
'''
uv run pytest ./tests/test_channels.py
'''
