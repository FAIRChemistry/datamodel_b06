# Data model for CRC 1333 project B06

This is the perliminary data model for CRC 1333 project B06. At the current time, the data model is still under development and major changes can occur at any time. Please feel free to make changes and contribute to the project.

### Dataset

This is a preliminary root container for all (meta-)data.

- __id*__
  - Type: string
  - Description: Unique identifier for the dataset
- __name*__
  - Type: string
  - Description: Descriptive name of the dataset
- __date*__
  - Type: date
  - Description: Date/time when the dataset was created
- __authors*__
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset
- __subjects*__
  - Type: string
  - Multiple: True
  - Description: Research subjects covered by the datset
- __keywords*__
  - Type: string
  - Multiple: True
  - Description: Descriptive keywords to describe the dataset
- __license*__
  - Type: string
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

### Experiment

Generic container for experiments covered by the dataset.

- __id*__
  - Type: string
  - Description: Unique identifier for the experiment
