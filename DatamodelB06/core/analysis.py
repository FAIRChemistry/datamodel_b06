import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .measuredquantity import MeasuredQuantity


@forge_signature
class Analysis(sdRDM.DataModel):

    """Generic Container for analyses."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )
    id: str = Field(
        ...,
        description="Unique identifier for the analysis",
    )

    name: str = Field(
        ...,
        description="Descriptive name for the analysis",
    )

    measured_quantity: MeasuredQuantity = Field(
        ...,
        description="Quantity determined through the analysis",
    )

    dsv_file_raw: str = Field(
        ...,
        description="Delimiter-seperated file containing the raw data of the analysis",
    )

    dsv_file_results: Optional[str] = Field(
        description="Delimiter-seperated file containing the results of the analysis",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="4aa69459dec606669cde5b1b942ae648025a1dd4"
    )
