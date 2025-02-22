from . import HDFSGenerator
from odd_models.discovery.data_assets.data_asset import DataAsset, HasUpstream


class S3Artifact(DataAsset):
    def __init__(self, oddrn, name=None):
        self.oddrn = oddrn
        self.name = name

    def __rshift__(self, data_asset: HasUpstream) -> DataAsset:
        data_asset.add_upstream(self)
        return data_asset

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def from_url(cls, url: str, name=None):
        return cls(HDFSGenerator.from_url(url).get_oddrn_paths("path"), name)
