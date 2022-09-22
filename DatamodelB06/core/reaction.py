import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .condition import Condition


@forge_signature
class Reaction(sdRDM.DataModel):

    """Generic container for reactions coverd by this dataset."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionINDEX"),
        xml="@id",
    )
    id: str = Field(
        ...,
        description="Unique identifier for the synthesis",
    )

    name: str = Field(
        ...,
        description="Accepted name(s) of the reaction",
        dataverse="pyDaRUS.EnzymeMl.reactions.name",
    )

    educts: List[str] = Field(
        description="Definied samples that participated in the reaction as educts",
        dataverse="pyDaRUS.EnzymeMl.reactions.educts",
        default_factory=ListPlus,
    )

    products: List[str] = Field(
        description="Definied samples that participated in the reaction as products",
        dataverse="pyDaRUS.EnzymeMl.reactions.products",
        default_factory=ListPlus,
    )

    intermediates: List[str] = Field(
        description=(
            "Definied samples that participated in the reaction as intermediates"
        ),
        dataverse="pyDaRUS.EnzymeMl.reactions.modifiers",
        default_factory=ListPlus,
    )

    catalysts: List[str] = Field(
        description=(
            "Definied samples that participated in the reaction as (co-)catalysts"
        ),
        dataverse="pyDaRUS.EnzymeMl.reactions.modifiers",
        default_factory=ListPlus,
    )

    generic_modifiers: List[str] = Field(
        description=(
            "Definied samples that participated in the reaction in some other manner"
        ),
        dataverse="pyDaRUS.EnzymeMl.reactions.modifiers",
        default_factory=ListPlus,
    )

    conditions: List[Condition] = Field(
        description=(
            "Different conditions that need to be specified for reproducing the"
            " reaction"
        ),
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="4aa69459dec606669cde5b1b942ae648025a1dd4"
    )

    def add_to_conditions(
        self,
        currently_under_construction_come_back_later: Optional[bool] = None,
    ) -> None:
        """
        Adds an instance of 'Condition' to the attribute 'conditions'.

        Args:
            currently_under_construction_come_back_later (Optional[bool]): tba. Defaults to None
        """

        conditions = [
            Condition(
                currently_under_construction_come_back_later=currently_under_construction_come_back_later,
            )
        ]

        self.conditions = self.conditions + conditions
