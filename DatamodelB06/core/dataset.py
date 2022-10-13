import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from typing import Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from datetime import datetime
from sdRDM.base.utils import forge_signature, IDGenerator

from .author import Author
from .experiment import Experiment
from .personalid import PersonalID
from .sample import Sample
from .reaction import Reaction
from .analytics import Analytics
from .concentrationunit import ConcentrationUnit


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

    HiKuan: Optional[str] = Field(description="Hi Kuan!", default=None)

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
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:


            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.


            name (str): Full name of the author.


            affiliation (str): Organisation the author is affiliated with.


            email (str): Contact e-mail address of the author.


            pid (List[PersonalID]): Personal identifiers of the author.


            phone (Optional[int]): Contact phone number of the author. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
            "email": email,
            "pid": pid,
            "phone": phone,
        }
        if id is not None:
            params["id"] = id
        authors = [Author(**params)]
        self.authors = self.authors + authors

    def add_to_samples(
        self,
        id: str,
        name: str,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        initial_concentration: Optional[float] = None,
        unit: Optional[ConcentrationUnit] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Sample' to the attribute 'samples'.

        Args:


            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.


            id (str): Unique identifier for the sample, following the EnzymeML convention "s[integer]", e.g. s001.


            name (str): Descriptive name of the sample.


            smiles (Optional[str]): SMILES notation of the molecular structure. Defaults to None


            inchi (Optional[str]): InChI encoding of the molecular structure. Defaults to None


            initial_concentration (Optional[float]): Numerical value of the initial concentration. Defaults to None


            unit (Optional[ConcentrationUnit]): Unit of the numerical value used in inital_concentration. Defaults to None
        """

        params = {
            "id": id,
            "name": name,
            "smiles": smiles,
            "inchi": inchi,
            "initial_concentration": initial_concentration,
            "unit": unit,
        }
        if id is not None:
            params["id"] = id
        samples = [Sample(**params)]
        self.samples = self.samples + samples

    def add_to_experiments(
        self,
        id: str,
        name: str,
        experiment_type: Union[Reaction, Analytics],
        details: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Experiment' to the attribute 'experiments'.

        Args:


            id (str): Unique identifier of the 'Experiment' object. Defaults to 'None'.


            id (str): Unique identifier for the experiment.


            name (str): Descriptive name for the experiment.


            experiment_type (Union[Reaction,Analytics]): Kind of experiment performed.


            details (Optional[str]): Free form detailed description of the experiment. Defaults to None
        """

        params = {
            "id": id,
            "name": name,
            "experiment_type": experiment_type,
            "details": details,
        }
        if id is not None:
            params["id"] = id
        experiments = [Experiment(**params)]
        self.experiments = self.experiments + experiments
