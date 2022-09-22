import sdRDM

from typing import Optional
from typing import Optional, Union
from typing import Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .analysis import Analysis
from .reaction import Reaction


class Experiment(sdRDM.DataModel):
    """Generic container for experiments covered by the dataset."""

    id: str = Field(..., description="Unique identifier for the experiment")

    name: str = Field(..., description="Descriptive name for the experiment")

    experiment_type: ExperimentType = Field(
        ..., description="Kind of experiment performed"
    )

    details: Optional[str] = Field(
        description="Free form detailed description of the experiment", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )
