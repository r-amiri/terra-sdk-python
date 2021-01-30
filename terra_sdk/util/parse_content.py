from terra_sdk.core.gov.proposals import TextProposal
from terra_sdk.core.distribution.proposals import CommunityPoolSpendProposal
from terra_sdk.core.treasury.proposals import (
    TaxRateUpdateProposal,
    RewardWeightUpdateProposal,
)
from terra_sdk.core.params.proposals import ParameterChangeProposal
from .base import create_demux

parse_content = create_demux(
    [
        TextProposal,
        CommunityPoolSpendProposal,
        TaxRateUpdateProposal,
        RewardWeightUpdateProposal,
        ParameterChangeProposal,
    ]
)