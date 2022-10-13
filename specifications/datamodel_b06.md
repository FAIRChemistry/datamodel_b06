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
  - Dataverse: pyDaRUS.Citation.author.name
- __subjects*__
  - Type: string
  - Default: Chemistry
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
- __HiKuan__
  - Type: string
  - Description: Hi Kuan!

### Author

Container for information regarding persons who worked on a dataset.

- __name*__
  - Type: string
  - Description: Full name of the author
  - Dataverse: pyDaRUS.Citation.author.name
- __affiliation*__
  - Type: string
  - Description: Organisation the author is affiliated with.
  - Dataverse: pyDaRUS.Citation.author.affiliation
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

Container for personal identifiers related to an author.

- __type*__
  - Type: string
  - Description: Type or scheme of personal identifier
  - Dataverse: pyDaRUS.Citation.author.identifier_scheme
- __identifier*__
  - Type: string
  - Description: String representation of the personal identifier
  - Dataverse: pyDaRUS.Citation.author.identifier

### Sample

Generic container for samples used, created, or destroyed in experiments.

- __id*__
  - Type: string
  - Description: Unique identifier for the sample, following the EnzymeML convention "s[integer]", e.g. s001
  - Dataverse: pyDaRUS.EnzymeMl.reactants.identifier
- __name*__
  - Type: string
  - Description: Descriptive name of the sample
  - Dataverse: pyDaRUS.EnzymeMl.reactants.name
- __smiles__
  - Type: string
  - Description: SMILES notation of the molecular structure
  - Dataverse: pyDaRUS.EnzymeMl.reactants.smilescode
- __inchi__
  - Type: string
  - Description: InChI encoding of the molecular structure
  - Dataverse: pyDaRUS.EnzymeMl.reactants.inchicode
- __initial_concentration__
  - Type: float
  - Description: Numerical value of the initial concentration
  - Dataverse: pyDaRUS.EnzymeMl.reactants.initial_concentration
- __unit__
  - Type: ConcentrationUnit
  - Description: Unit of the numerical value used in inital_concentration
  - Dataverse: pyDaRUS.EnzymeMl.reactans.unit

### Experiment

Generic container for experiments covered by the dataset.

- __id*__
  - Type: string
  - Description: Unique identifier for the experiment
- __name*__
  - Type: string
  - Description: Descriptive name for the experiment
- __experiment_type*__
  - Type: Reaction, Analytics
  - Description: Kind of experiment performed
- __details__
  - Type: string
  - Description: Free form detailed description of the experiment

### Reaction

Generic container for reactions coverd by this dataset.

- __id*__
  - Type: string
  - Description: Unique identifier for the synthesis
- __name*__
  - Type: string
  - Description: Accepted name(s) of the reaction
  - Dataverse: pyDaRUS.EnzymeMl.reactions.name
- __starting_materials*__
  - Type: string
  - Multiple: True
  - Description: Defines samples that participate in the reaction as starting materials
  - Dataverse: pyDaRUS.EnzymeMl.reactions.educts
- __products*__
  - Type: string
  - Multiple: True
  - Description: Defines samples that participate in the reaction as products
  - Dataverse: pyDaRUS.EnzymeMl.reactions.products
- __solvents__
  - Type: string
  - Multiple: True
  - Description: Defines samples that participate in the reaction as solvents
- __intermediates__
  - Type: string
  - Multiple: True
  - Description: Defines samples that participate in the reaction as intermediates
  - Dataverse: pyDaRUS.EnzymeMl.reactions.modifiers
- __catalysts__
  - Type: string
  - Multiple: True
  - Description: Defines samples that participate in the reaction as (co-)catalysts
  - Dataverse: pyDaRUS.EnzymeMl.reactions.modifiers
- __generic_modifiers__
  - Type: string
  - Multiple: True
  - Description: Defines samples that participate in the reaction in some other manner
  - Dataverse: pyDaRUS.EnzymeMl.reactions.modifiers
- __conditions*__
  - Type: Condition
  - Multiple: True
  - Description: Different conditions that need to be specified for reproducing the reaction

### Condition

Generic container for conditions that influenced a reaction

- __name*__
  - Type: string
  - Description: Descriptive name of the condition that influenced a reaction
- __explanation*__
  - Type: string
  - Description: Free text description and explanation of the condition

### Analytics

Generic Container for analyses.

- __id*__
  - Type: string
  - Description: Unique identifier for the analysis
- __name*__
  - Type: string
  - Description: Descriptive name for the analysis
- __measured_quantity*__
  - Type: MeasuredQuantity
  - Description: Quantity determined through the analysis
- __dsv_file_raw*__
  - Type: string
  - Description: Delimiter-seperated file containing the raw data of the analysis
- __dsv_file_results__
  - Type: string
  - Description: Delimiter-seperated file containing the results of the analysis

#### ConcentrationUnit

Enum containing the units for the concentration.

```python
n_m = 'nmol/l'
u_m = 'umol/l'
m_m = 'mmol/l'
m = 'mol/l'
```

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
