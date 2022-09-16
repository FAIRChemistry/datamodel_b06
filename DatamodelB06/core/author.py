import sdRDM

from typing import Optional
from typing import List
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .personalid import PersonalID


class Author(sdRDM.DataModel):
    """Container for information regarding persons who worked on a dataset."""

    name: str = Field(..., description="Full name of the author")

    affiliation: str = Field(
        ..., description="Organisation the author is affiliated with."
    )

    email: str = Field(..., description="Contact e-mail address of the author")

    phone: Optional[int] = Field(
        description="Contact phone number of the author", default=None
    )

    pid: List[PersonalID] = Field(
        description="Personal identifiers of the author", default_factory=ListPlus
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )

    def add_to_pid(self, type: str, identifier: str) -> None:
        """
        Adds an instance of 'PersonalID' to the attribute 'pid'.

        Args:


            type (str): Type or scheme of personal identifier.


            identifier (str): String representation of the personal identifier.
        """
        pid = [PersonalID(type=type, identifier=identifier)]
        self.pid = self.pid + pid
