# Sofware Engineering for Scientists
Computer science (CS) departments have become good at teaching computer programming to students from various backgrounds and experience levels. While the primary goal of this pedagogical expansion has been to increase the diversity in CS departments, many other students have also benefited from improvements to these classes. In particular, there has been a surge of trainees wanting to learn to program to develop new software to analyze large and complex data sets. Unfortunately, there is a gap between knowing how to program and knowing how to design and implement robust and reproducible software. In particular, introductory CS classes do not cover core principles of software engineering, such as software design, construction, testing, and maintenance. Since these classes target CS students, the expectation is that students will learn these skills in subsequent upper-level courses. Non-CS students must either learn these topics on their own or, more likely, develop lower-quality software.

Software Engineering for Scientists (SWE4S) aims to bridge this gap by aggregating topics from the relevant upper-level CS classes, including algorithms, data structures, data science, and software engineering. The challenge is to select the right subset of subjects from each class and integrate them into an engaging, not overwhelming, single-semester course. To help us prioritize topics, we actively solicited input from trainees and their advisors.

This repo contains the notes and small Python and Bash scripts used in teaching Sofware Engineering for Scientists taught at CU Boulder.

For more information about the course contct Ryan Layer at ryan.layer@colorado.edu

## Fall 2023 Schedule
| Week | Dates | Topics | Assignment |
|------|-------|--------|------------|
| 1	| Aug 29, 31	| Intro<sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Welcome%20to%20SWE4S.pdf)</sup>, Setup <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Command%20Line.pdf) [2](https://github.com/swe4s/lectures/blob/master/doc/Shell%20Scripts.pdf) [3](https://github.com/swe4s/lectures/blob/master/doc/Development%20Environment.pdf) [4](https://github.com/swe4s/lectures/blob/master/doc/Conda.pdf)</sup>, GitHub <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Git%20Workflow.pdf) [2](https://github.com/swe4s/lectures/blob/master/doc/Branching.pdf) [3](https://github.com/swe4s/lectures/blob/master/doc/Pull%20Request.pdf) [4](https://github.com/swe4s/lectures/blob/master/doc/Version%20Control%2C%20Git%2C%20and%20GitHub.pdf) [5](https://github.com/swe4s/lectures/blob/master/doc/Using%20SSH%20Keys%20with%20GitHub.pdf)</sup>, and GitHub Classroom<sup>[1](https://github.com/swe4s/lectures/blob/master/doc/GitHub%20Classroom.pdf)</sup>| [1](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%201_%20GitHub%20Classroom.pdf) |
| 2	| Sep 5, 7	| Python <sup>[1](https://github.com/swe4s/lectures/tree/master/src/python_refresher) [2](https://github.com/swe4s/lectures/blob/master/doc/Python%20Refresher.pdf)</sup> | [2](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%202_%20Python%20Refresher.pdf) |
| 3	| Sep 12, 14	| Best Practices <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Best%20Practices.pdf)</sup> | [3](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%203_%20Best%20Practices.pdf) |
| 4	| Sep 19, 21	| Project pitches | |
| 5	| Sep 26, 28	| Unit tests<sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Unit%20Testing.pdf)</sup>, Functional tests<sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Functional%20Testing.pdf)</sup>| [4](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%204_%20Testing.pdf)	|
| 6	| Oct 3, 5	| Continuous integration <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Continuous%20Integration%20with%20GitHub%20Actions.pdf)</sup> | [5](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%205_%20Continuous%20Integration.pdf) |
| 7	| Oct 10, 12	| Benchmarking <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Profiling%20and%20Benchmarking.pdf)</sup>, Workflow <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Piplines%20and%20workflows.pdf)</sup> | [6](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%206_%20Workflows.pdf) |
| 8	| Oct 17, 19	| Code review <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Code%20Review.pdf) [2](https://github.com/swe4s/lectures/blob/master/doc/Code%20Review%20Check%20List.docx) [3](https://github.com/swe4s/lectures/blob/master/doc/Code%20review%20request.pdf)</sup> | [7](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%207_%20Code%20Review.pub.pdf) |
| 9	| Oct 24, 26	| Test driven development<sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Test-Driven%20Development.pdf)</sup>, Sorting Searching and Indexing | [8](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%208_%20Searching%20and%20Test%20Driven%20Development.pdf) |
| 1	| Oct 31, Nov 2	| Using libraries - Michael Bradshaw | [9](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%209_%20Libraries%20Pandas%20and%20MatPlotLib.pdf) |
| 11	| Nov 7, 9	|  Project code review | [10](https://github.com/swe4s/lectures/blob/master/assignments/Assignment%2010_%20Project%20Code%20Review%20copy.pub.pdf) |
| 12	| Nov 14, 16	| Hash tables <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Hash%20Tables.pdf)</sup> | 11 |
| 13	| Nov 21, 23	| Fall Break | |			
| 14	| Nov 28, 30	| Data Science / Machine learning - Jamie Dixon | |
| 15	| Dec 5, 7	| Project presentations | |
| 16	| Dec 12, 14	| Project presentations | |

## Other Topics
| Topics |
|--------|
| Configuration files <sup>[1](https://github.com/swe4s/lectures/blob/master/doc/Config%20Files.pdf)</sup> |

## Grading
### Grad Grading					
- Weekly assignments 60%		
- Final project 40%		
  - Proposal	10%
  - Code Review 10%
  - Presentation	40%
  - Content 40%

### Undergrad grading
- Weekly assignments		90%
- Final project (optional)	30% (yes, that adds up to 120)
  
## Class structure
This class is the first of its kind and we will be flexible with the pace of topics and assignments. While attendance is not required, this is a hands-on class and lectures will be interactive. Supporting documents will be provided, but many details will only be covered in class. 

## Assignments
All assignments and grading will be through GitHub classroom. We will post the link to the assignment. Go to the link, accept the assignment, and clone the repository. All assignments must adhere to the Python best practices and must use the proper GitHub workflow. Unless directed otherwise, we will only consider the v1.0 release and use the date of that release as the submit time. Late assignments will not be considered. Assignments without the correct release will not be considered. You may work together on assignments, but I expect original contributions from every student. In most cases, assignments will be due at 5PM one week after they are posted.

## Project
All graduate students must propose and submit a project. Each project will have between 2 and 4 team members. A team may not have more than three graduate students. A team of 4 must have at least one undergraduate. Projects can address any scientific question and must incorporate all of the software engineering and software design topics covered in class. The question does not need to be novel, but all contributions must be original. Teams are encouraged, but not required, to meet with me about their topic. A short in-class proposal will focus on the scientific question and a longer final presentation will focus on the resulting software product and any results. Each team will perform and present a code review of another team’s code. Undergraduates are encouraged but not required to either join a team or develop their own project.
