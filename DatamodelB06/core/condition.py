import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Condition(sdRDM.DataModel):

    """Generic container for conditions that influenced a reaction"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("conditionINDEX"),
        xml="@id",
    )
    currently_under_construction_come_back_later: Optional[bool] = Field(
        default=None,
        description="tba",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="4aa69459dec606669cde5b1b942ae648025a1dd4"
    )
