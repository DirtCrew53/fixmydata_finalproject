1. Project Overview

Our group is developing fixmydata, a Python library focused on simplifying data cleaning tasks for data science workflows. The goal of this project is to provide an object-oriented, easy-to-use toolkit that helps users automatically clean, validate, and prepare tabular datasets before analysis.

The library applies the four core OOP principles:

Encapsulation – using protected attributes such as _df and providing safe access through methods and properties.

Abstraction – exposing only simplified interfaces for cleaning while hiding internal implementation details.

Inheritance – extending base classes such as StatsEngine with child classes like CorrelationEngine.

Polymorphism – method overriding (e.g., child class modifies parent behavior).

The project will follow the required structure of a Python package, later published on PyPI during Week 5.

2. Chosen Library Focus

After group discussion, we selected the category Data Cleaning because:

It directly matches the name fixmydata, which implies repairing or improving data quality.

It is widely needed in almost every data science workflow.

It provides clear opportunities for applying OOP design, especially abstraction and inheritance.

The scope is wide enough for 5 weeks of development, yet manageable for group collaboration.

3. Planned Features (Week 1 Requirements)

We identified five core features that will be implemented throughout the project:

Handle Missing Values

Functions to drop missing rows or fill them with user-defined values.

Remove Duplicates

Automatically delete duplicate entries to improve data integrity.

Detect Outliers

Identify extreme numeric values using IQR or z-score methods.

Normalize Columns

Scale numeric features either to 0–1 or standardized distribution.

Data Quality Summary

Provide counts and percentages of missing values, duplicates, and outliers.

These features will be distributed across different classes such as DataCleaner, DataValidator, and StatsEngine.

4. Class Design (UML Summary)

For Week 1, the team drafted a UML class diagram showcasing the structure of the fixmydata library using abstraction and inheritance:

DataCleaner – main class holding the dataset and performing cleaning operations.

DataValidator – abstract dependency used to check data conditions (missing values, numeric validation, etc.).

StatsEngine – parent class for computing basic statistical summaries.

CorrelationEngine – child class overriding methods for specialized statistical analysis.

Visualizer – uses abstraction to create plots using any object with a .df attribute.

The UML diagram illustrates the relationships:

DataCleaner → DataValidator (dependency via abstraction)

StatsEngine → CorrelationEngine (inheritance)

Visualizer → DataCleaner/StatsEngine (dependency through abstraction)

The diagram will be refined in Week 2 once more methods are implemented.

5. Group Meeting Summary

Date: Week 1
Mode: Online meeting (Messenger/Google Classroom)

Discussion Highlights

Agreed on selecting Data Cleaning as the library focus.

Reviewed Week 1 requirements and assigned tasks.

Finalized the 3–5 features required for the library.

Drafted the initial UML diagram and discussed OOP applications.

Set up the GitHub repository and assigned roles such as coder, documenter, and reviewer.

Task Assignments :

Leader: Johann Lloyd Megalbio

Design & UML: Albrien Dealino

Core Class Coding: Johann Lloyd Megalbio

Documentation & README: Shawn B. Sillote

Testing & Demo Script: Rafael Calingin

6. Plans for Week 2

In the next development phase, the group will:

Implement the main classes (DataCleaner, DataValidator, StatsEngine)

Apply encapsulation using protected attributes

Begin writing docstrings

ensure early testing of cleaning methods

Update GitHub repo with initial codebase

We will also refine the UML diagram with class relationships and method lists.

7. Conclusion

Week 1 focused on establishing the foundation for the fixmydata library. The team successfully decided on the project concept, identified key features, created an OOP-based class structure, drafted a UML diagram, and organized workflow roles. This strong start will guide the development work in Weeks 2–5 as we gradually build a functional and publishable Python library
