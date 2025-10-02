# Sofware Engineering for Scientists
Computer Science (CS) departments have become increasingly effective at
teaching programming to students from diverse backgrounds and experience
levels. While the primary goal of this pedagogical shift has been to broaden
participation in CS, many other students, particularly those working with large
and complex datasets, have also benefited. However, a significant gap remains
between learning how to program and developing robust, reproducible software.
Introductory CS courses rarely cover essential software engineering principles
such as design, testing, construction, and maintenance. These topics are
typically reserved for upper-level CS courses, leaving non-CS students to
either learn them independently or risk producing lower-quality software.

Software Engineering for Scientists (SWE4S) addresses this gap by combining key
concepts from upper-level CS courses such as algorithms, data structures, data
science, and software engineering into a single, accessible semester-long
course. The challenge is to select the most relevant material and deliver it in
a way that is rigorous yet approachable. To guide topic selection, we solicited
input directly from trainees and their research advisors.

This repository contains notes and example Python and Bash scripts used in
Software Engineering for Scientists, taught at CU Boulder.

For more information about the course, contact Ryan Layer at
ryan.layer@colorado.edu.

## Fall 2025 Schedule
| Week | Dates         | Topics | Assignment |
|------|---------------|--------|------------|
| 1    | Aug 21, 26    | Intro<sup>([course intro slides](doc/Welcome%20to%20SWE4S.pdf))</sup>, Setup<sup>(["Command Line Primer" notes](doc/Command%20Line.pdf), ["Shell Scripts" notes](doc/Shell%20Scripts.pdf), ["Development Environment" notes](doc/Development%20Environment.pdf), ["Conda (mamba)" notes](doc/Conda.pdf), [US counties data](course-material/python-refresher/us-counties.csv))</sup>, GitHub<sup>(["Version Control, Git, and GitHub" slides](doc/Version%20Control%2C%20Git%2C%20and%20GitHub-slides.pdf), ["Version Control, Git, and GitHub" notes/writeup](doc/Version%20Control%2C%20Git%2C%20and%20GitHub.pdf), ["Using SSH keys with GitHub" notes](doc/Using%20SSH%20Keys%20with%20GitHub.pdf))</sup>, GitHub Classroom<sup>[1](doc/GitHub%20Classroom.pdf)</sup> | [1](assignments/Assignment%201_%20GitHub%20Classroom.pdf) |
| 2    | Aug 28, Sep 2 | Python<sup>(["Python Refresher" notes](doc/Python%20Refresher.pdf), [folder containing examply Python scripts](https://github.com/swe4s/lectures/tree/main/src/python_refresher))</sup> | [2](assignments/Assignment%202_%20Python%20Refresher.pdf) |                        
| 3    | Sep 4, 9      | Best practices<sup>[1](doc/Best%20Practices.pdf)</sup> | [3](assignments/Assignment%203_%20Best%20Practices.pdf) |
| 4    | Sep 11, 16    | Project pitches | |
| 5    | Sep 18, 23    | Unit tests<sup>[1](doc/Unit%20Testing.pdf)</sup>, Functional tests<sup>[1](doc/Functional%20Testing.pdf)</sup>   | [4](assignments/Assignment%204_%20Testing.pdf) |
| 6    | Sep 25, 30    | Continuous integration<sup>[1](doc/Continuous%20Integration%20with%20GitHub%20Actions.pdf)</sup>         | [5](assignments/Assignment%205_%20Continuous%20Integration.pdf)|
| 7    | Oct 2, 7      | Test driven development<sup>[1](doc/Test-Driven%20Development.pdf)</sup>, Sorting Searching and Indexing        | |
| 8    | Oct 9         | Reading Day | |
| 9    | Oct 14, 16    | Code review<sup>[1](doc/Code%20Review.pdf) [2](doc/Code%20Review%20Check%20List.docx) [3](doc/Code%20review%20request.pdf)</sup> | |
| 10   | Oct 21, 23    | Benchmarking, Workflow<sup>[1](doc/Piplines%20and%20workflows.pdf)</sup> | 
| 11   | Oct 28, 30    | Hash tables                    | |
| 12   | Nov 4, 6      | Using/creating libraries       | |
| 13   | Nov 11, 13    | Project code review            | |
| 14   | Nov 18, 20    | AI code assistants             | |
| 15   | Nov 25, 27    | Fall break                     | |
| 16   | Dec 2, 4      | Project presentations          | |

## Other Topics
| Topics |
|--------|
| Configuration files <sup>[1](doc/Config%20Files.pdf)</sup> |

## Class structure

## Grading
### Grad Grading					
- Weekly assignments - 60%		
- Final project - 40%		
  - Proposal - 10%
   Code Review - 10%
  - Presentation - 40%
  - Content - 40%

### Undergrad grading
- Weekly assignments - 90%
- Final project (optional)	- 30% (yes, that adds up to 120)%

## Class structure
This class is the first of its kind and we will be flexible with the pace of
topics and assignments. While attendance is not required, this is a hands-on
class and lectures will be interactive. Supporting documents will be provided,
but many details will only be covered in class.

## Assignments
All assignments and grading will be managed through GitHub Classroom. For each
assignment, we will provide a link. Follow the link it to accept the assignment
and clone the repository. Submissions must follow Python best practices and use
the appropriate GitHub workflow. Unless stated otherwise, we will only evaluate
the v1.0 release, using its release date as the official submission time. Late
or incorrectly released assignments will not be accepted. Collaboration is
allowed, but each student must submit original work. Unless noted otherwise,
assignments are due by 5 PM one week after they are posted.

## Project
All graduate students are required to propose and complete a project. Each
project team must consist of 2 to 4 members, with no more than three graduate
students per team. Teams of four must include at least one undergraduate.
Projects may address any scientific question but must incorporate the software
engineering and design principles covered in class. While the scientific
question does not need to be novel, all contributions must be original. Teams
are encouraged, but not required, to meet with the instructor to discuss their
topic. A brief in-class proposal will present the scientific question, and a
longer final presentation will highlight the software product and results. Each
team will also conduct and present a code review of another team’s project.
Undergraduates are encouraged, but not required, to either join a team or
propose their own project.
