# Data model for CRC 1333 project B06

This is the perliminary data model for CRC 1333 project B06. At the current time, the data model is still under development and major changes can occur at any time. Please feel free to make changes and contribute to the project.

### Dataset

This is a preliminary root container for all (meta-)data.

- __id*__
  - Type: string
  - Description: Unique identifier for the dataset
- __name*__
  - Type: string
  - Default: Insert dataset name
  - Description: Descriptive name of the dataset
  - Dataverse: pyDaRUS.Citation.title
- __date*__
  - Type: datetime
  - Default_factory: datetime.now
  - Description: Date/time when the dataset was created
  - Dataverse: pyDaRUS.Citation.production_date
- __authors*__
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset
  - pyDaRUS.Citation.author.name
- __subjects*__
  - Type: pyDaRUS.Citation.SubjectEnum
  - Default_factory: pyDaRUS.Citation.SubjectEnum.chemistry
  - Multiple: True
  - Description: Research subjects covered by the datset
  - Dataverse: pyDaRUS.Citation.subject
- __keywords*__
  - Type: string
  - Multiple: True
  - Description: Descriptive keywords to describe the dataset
  - Dataverse: pyDaRUS.Citation.keyword.term
- __license*__
  - Type: string
  - Default: MIT
  - Description: License for the dataset
- __samples*__
  - Type: Sample
  - Multiple: True
  - Description: Samples used, created, or destroyed by experiments of this dataset
- __experiments*__
  - Type: Experiment
  - Multiple: True
  - Description: Experiments covered by this dataset

### Author

Container for information regarding persons who worked on a dataset.

- __name*__
  - Type: string
  - Description: Full name of the author
- __affiliation*__
  - Type: string
  - Description: Organisation the author is affiliated with.
- __email*__
  - Type: string
  - Description: Contact e-mail address of the author
- __phone__
  - Type: int
  - Description: Contact phone number of the author
- __pid__
  - Type: PersonalID
  - Multiple: True
  - Description: Personal identifiers of the author

### PersonalID

Container for personal identifiers related to an author

- __type*__
  - Type: string
  - Description: Type or scheme of personal identifier
- __identifier*__
  - Type: string
  - Description: String representation of the personal identifier

### Sample

Generic container for samples used, created, or destroyed in experiments.

- __name*__
  - Type: string
  - Description: Descriptive name of the sample
- __smiles__
  - Type: string
  - Description: SMILES notation of the molecular structure
- __inchi__
  - Type: string
  - Description: InChI encoding of the molecular structure

### Experiment

Generic container for experiments covered by the dataset.

- __id*__
  - Type: string
  - Description: Unique identifier for the experiment
- __name*__
  - Type: string
  - Description: Descriptive name for the experiment
- __experiment_type*__
  - Type: ExperimentType
  - Description: Kind of experiment performed
- __measured_quantity*__
  - Type: MeasuredQuantity
  - Description: Quantity determined through the experiment

### ExperimentType

Generic container for the different kinds of experiment.

- __none__
  - Type: string
  - Description: Some text

#### MeasuredQuantity

Enum containing quantities that are measured.

```python
EE = "ee"
TON = "TON"
TOF = "TOF"
YIELD = "yield"
TIME = "time"
TEMPERATURE = "temperature"
CONCENTRATION = "concentration"
MOLARITY = "molarity"
```
