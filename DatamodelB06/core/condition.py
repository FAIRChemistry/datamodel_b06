import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Condition(sdRDM.DataModel):
    """Generic container for conditions that influenced a reaction"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("conditionINDEX"),
        xml="@id",
    )

    name: str = Field(
        ..., description="Descriptive name of the condition that influenced a reaction"
    )

    explanation: str = Field(
        ..., description="Free text description and explanation of the condition"
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="4aa69459dec606669cde5b1b942ae648025a1dd4"
    )
