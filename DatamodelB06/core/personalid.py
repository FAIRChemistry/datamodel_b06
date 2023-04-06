import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


class PersonalID(sdRDM.DataModel):
    """Container for personal identifiers related to an author"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("personalidINDEX"),
        xml="@id",
    )

    type: str = Field(
        ...,
        description="Type or scheme of personal identifier",
        dataverse="pyDaRUS.Citation.author.identifier_scheme",
    )

    identifier: str = Field(
        ...,
        description="String representation of the personal identifier",
        dataverse="pyDaRUS.Citation.author.identifier",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e2fcf28747c1686bc5dbc48709d307e1ddd7947c"
    )
