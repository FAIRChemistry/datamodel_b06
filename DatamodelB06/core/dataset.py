import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from datetime import datetime
from sdRDM.base.utils import forge_signature, IDGenerator

from .author import Author
from .experiment import Experiment
from .personalid import PersonalID
from .sample import Sample
from .experimenttype import ExperimentType
from .measuredquantity import MeasuredQuantity


class Dataset(sdRDM.DataModel):
    """This is a preliminary root container for all (meta-)data."""

    id: str = Field(..., description="Unique identifier for the dataset")

    name: str = Field(..., description="Descriptive name of the dataset")

    date: datetime = Field(..., description="Date/time when the dataset was created")

    license: str = Field(..., description="License for the dataset")

    authors: List[Author] = Field(
        description="Persons who worked on the dataset", default_factory=ListPlus
    )

    subjects: List[str] = Field(
        description="Research subjects covered by the datset", default_factory=ListPlus
    )

    keywords: List[str] = Field(
        description="Descriptive keywords to describe the dataset",
        default_factory=ListPlus,
    )

    samples: List[Sample] = Field(
        description=(
            "Samples used, created, or destroyed by experiments of this dataset"
        ),
        default_factory=ListPlus,
    )

    experiments: List[Experiment] = Field(
        description="Experiments covered by this dataset", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b06.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="bb4b1117c1d706a506a972e3d67456fcc85dbc31"
    )

    def add_to_authors(
        self,
        name: str,
        affiliation: str,
        email: str,
        pid: List[PersonalID],
        phone: Optional[int] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:


            name (str): Full name of the author.


            affiliation (str): Organisation the author is affiliated with.


            email (str): Contact e-mail address of the author.


            pid (List[PersonalID]): Personal identifiers of the author.


            phone (Optional[int]): Contact phone number of the author. Defaults to None
        """
        authors = [
            Author(
                name=name, affiliation=affiliation, email=email, pid=pid, phone=phone
            )
        ]
        self.authors = self.authors + authors

    def add_to_samples(
        self, name: str, smiles: Optional[str] = None, inchi: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Sample' to the attribute 'samples'.

        Args:


            name (str): Descriptive name of the sample.


            smiles (Optional[str]): SMILES notation of the molecular structure. Defaults to None


            inchi (Optional[str]): InChI encoding of the molecular structure. Defaults to None
        """
        samples = [Sample(name=name, smiles=smiles, inchi=inchi)]
        self.samples = self.samples + samples

    def add_to_experiments(
        self,
        id: str,
        name: str,
        experiment_type: ExperimentType,
        measured_quantity: MeasuredQuantity,
    ) -> None:
        """
        Adds an instance of 'Experiment' to the attribute 'experiments'.

        Args:


            id (str): Unique identifier for the experiment.


            name (str): Descriptive name for the experiment.


            experiment_type (ExperimentType): Kind of experiment performed.


            measured_quantity (MeasuredQuantity): Quantity determined through the experiment.
        """
        experiments = [
            Experiment(
                id=id,
                name=name,
                experiment_type=experiment_type,
                measured_quantity=measured_quantity,
            )
        ]
        self.experiments = self.experiments + experiments
