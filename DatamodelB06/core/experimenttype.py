import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class ExperimentType(sdRDM.DataModel):

    """Generic container for the different kinds of experiment."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimenttypeINDEX"),
        xml="@id",
    )
    none: Optional[str] = Field(
        description="Some text",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="afa61b8ac16f4ea92deb322da982e2f9148b3b12"
    )
