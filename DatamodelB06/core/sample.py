import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


class Sample(sdRDM.DataModel):
    """Generic container for samples used, created, or destroyed in experiments."""

    name: str = Field(..., description="Descriptive name of the sample")

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    smiles: Optional[str] = Field(
        description="SMILES notation of the molecular structure", default=None
    )

    inchi: Optional[str] = Field(
        description="InChI encoding of the molecular structure", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )
