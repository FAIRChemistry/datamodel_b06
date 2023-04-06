import sdRDM

from typing import Optional
from typing import Optional, Union
from typing import Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .reaction import Reaction
from .analytics import Analytics


class Experiment(sdRDM.DataModel):
    """Generic container for experiments covered by the dataset."""

    name: str = Field(..., description="Descriptive name for the experiment")

    details: Optional[str] = Field(
        description="Free form detailed description of the experiment", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentINDEX"),
        xml="@id",
    )

    experiment_type: Union[Reaction, Analytics] = Field(
        ..., description="Kind of experiment performed"
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e2fcf28747c1686bc5dbc48709d307e1ddd7947c"
    )
