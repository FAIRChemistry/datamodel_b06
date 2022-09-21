import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


class PersonalID(sdRDM.DataModel):
    """Container for personal identifiers related to an author"""

    type: str = Field(..., description="Type or scheme of personal identifier")

    identifier: str = Field(
        ..., description="String representation of the personal identifier"
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("personalidINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )
