import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


class Experiment(sdRDM.DataModel):
    """Generic container for experiments covered by the dataset."""

    id: str = Field(..., description="Unique identifier for the experiment")

    name: str = Field(..., description="Descriptive name for the experiment")

    experiment_type: ExperimentType = Field(
        ..., description="Kind of experiment performed"
    )

    measured_quantity: MeasuredQuantity = Field(
        ..., description="Quantity determined through the experiment"
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )
