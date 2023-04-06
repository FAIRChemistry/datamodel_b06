import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .measuredquantity import MeasuredQuantity


@forge_signature
class Analytics(sdRDM.DataModel):
    """Generic Container for analyses."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analyticsINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Descriptive name for the analysis")

    measured_quantity: MeasuredQuantity = Field(
        ..., description="Quantity determined through the analysis"
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
        default="https://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e2fcf28747c1686bc5dbc48709d307e1ddd7947c"
    )
