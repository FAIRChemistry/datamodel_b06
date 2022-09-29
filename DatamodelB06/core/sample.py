import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .concentrationunit import ConcentrationUnit


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

    initial_concentration: Optional[float] = Field(
        description="Numerical value of the initial concentration",
        dataverse="pyDaRUS.EnzymeMl.reactants.initial_concentration",
        default=None,
    )

    unit: Optional[InitialConcentrationUnit] = Field(
        description="Unit of the numerical value used in inital_concentration",
        dataverse="pyDaRUS.EnzymeMl.reactans.unit",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )
