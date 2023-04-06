import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .personalid import PersonalID


class Author(sdRDM.DataModel):
    """Container for information regarding persons who worked on a dataset."""

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

    name: str = Field(
        ...,
        description="Full name of the author",
        dataverse="pyDaRUS.Citation.author.name",
    )

    affiliation: str = Field(
        ...,
        description="Organisation the author is affiliated with.",
        dataverse="pyDaRUS.Citation.author.affiliation",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e2fcf28747c1686bc5dbc48709d307e1ddd7947c"
    )

    def add_to_pid(self, type: str, identifier: str, id: Optional[str] = None) -> None:
        """
        Adds an instance of 'PersonalID' to the attribute 'pid'.

        Args:


            id (str): Unique identifier of the 'PersonalID' object. Defaults to 'None'.


            type (str): Type or scheme of personal identifier.


            identifier (str): String representation of the personal identifier.
        """

        params = {"type": type, "identifier": identifier}
        if id is not None:
            params["id"] = id
        pid = [PersonalID(**params)]
        self.pid = self.pid + pi


d
