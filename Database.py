# -*- coding: utf-8 -*-
"""
Spyder Editor

This is the Database for FindMyTutor.
"""
import numpy as np
import pandas as pd
#Database Creation
Tutor_Name = ["Yasmean Abdullah", "Alejandra Lopez", "Annabel Lopez", "Eric Lopez", "Martin Loughney", "Jacob Luzadder", "Brendan Mahood-MacDonald", "Ismael Maldonado", "Jacob Malinoff", "Matthew Maltese", "Frankie Mannerino", "Christian Be Manzano", "Caleb Marconi", "Michaela Mariotti", "Joseph Markasovic", "Angela Marquez", "Melanie Marquez", "Kaitlin Martin", "Savannah Martin", "Adriana Martinez", "Angel Martinez", "Evelyn Martinez", "Kassandra Martinez", "Marco Martinez", "Nancy Martinez", "Alan Martinez-Lopez", "Heather Mayhew", "Sean McClory", "Raelen McCoyne", "Julia McKee", "Meghan McKibbin", "Kathleen McLoughlin", "Kevin McQuillan", "Maria Medina", "Natalie Medina", "Grace Medlicott", "Sandra Mendoza", "Vivian Mendoza", "Kaitlin Mikols", "Nicholas Miller" ]
Course_Name = ["CMPSC-206 Web Applications 1", "CMPSC-306 Web Applications 2", "CMPSC-255 Introduction to Networks", "CMPSC-200 Virtual Worlds", "CMPSC-202 Programming I ", "CMPSC-203 Programming II", "CMPSC-345 Computer Systems & Organization", "CMPSC-311 Data Structures & Algorithms", "MATH-200 Discrete Mathematics", "RELST-266 Suffering & Death", "CMPSC-390 Software Engineering", "CMPSC-309 Issues in Computing", "BIOL-117 Exercise Physiology", "CMPSC-321 Databases", "ART-119 Digital Imagery", "Comms 221 Digital Video Production", "MATH-135 Introduction to Statistics", "ART-111 Intro to Film Analysis", "CMPSC-301 Operating Systems", "ART 220: Graphic Design II", "COMM-205 Mediated Message Production", "ART 322: Advertising in Marketing", "BIOL 213: Interactions in the Environment", "CMPSC-360 Usability and Design", "CHEM 331: Physical Chemistry", "PSYCH-101 Introduction to Psychology", "CHEM-111 General Chemistry", "MATH 202: Calculus with Analytic Geometry", "HIST-103 U.S. History to 1877", "COMM 220: Digital Audio Production", "Psych-200 child development", "Psych-199 lifespan development", "Psych-204 abnormal psychology", "MKTG 355 Digital Marketing", "BIOL-206 microbiology", "MGMT 370 IT Management", "BIOL-202 Human Anatomy", "ENGL 208: Study of Rhetoric", "BIOL-203 Human physiology", "CMPSC-260 Clojure"]
In_Person_Meeting_Times = ["11:10 am", "1:50 pm", "6:50 pm", "4:20 pm", "12:10 pm", "1:40 pm", "3:40 pm", "12:20 pm", "1:40 pm", "12:30 pm", "4:20 pm", "12:50 pm", "12:30 pm", "6:30 pm", "4:00 pm", "4:00 pm", "11:00 am", "1:40 pm", "1:30 pm", "5:40 pm", "12:00 pm", "12:50 pm", "10:40 am", "3:10 pm", "11:00 am", "7:50 pm", "4:20 pm", "2:50 pm", "7:20 pm", "10:30 am", "7:20 pm", "4:00 pm", "5:20 pm", "1:50 pm", "7:10 pm", "10:50 am", "5:30 pm", "12:40 pm", "2:00 pm", "12:00 pm"]
Tutor_Name
Online_Meeting_Times = ["11:40 am", "7:30 pm", "12:20 pm", "12:00 pm", "9:50 pm", "1:10 pm", "4:30 pm", "4:10 pm", "2:50 pm", "4:10 pm", "10:20 pm", "10:50 pm", "4:10 pm", "4:20 pm", "5:40 pm", "3:00 pm", "12:30 pm", "6:30 pm", "11:20 am", "6:50 pm", "2:10 pm", "6:00 pm", "11:50 am", "10:20 pm", "4:00 pm", "7:10 pm", "12:00 pm", "9:50 pm", "10:00 pm", "1:20 pm", "10:40 pm", "2:50 pm", "8:30 pm", "11:20 am", "12:40 pm", "5:20 pm", "12:00 pm", "3:10 pm", "11:10 am", "6:20 pm"]
Online_Meeting_Times
Contact_Information = ["grady@mymail.sxu.edu", "jesse@mymail.sxu.edu", "sharon@mymail.sxu.edu", "rande@mymail.sxu.edu", "eegsa@mymail.sxu.edu", "jonadab@mymail.sxu.edu", "knorr@mymail.sxu.edu", "yruan@mymail.sxu.edu", "tromey@mymail.sxu.edu", "codex@mymail.sxu.edu", "mcnihil@mymail.sxu.edu", "lstaf@mymail.sxu.edu", "jdray@mymail.sxu.edu", "choset@mymail.sxu.edu", "oechslin@mymail.sxu.edu", "bryam@mymail.sxu.edu", "miturria@mymail.sxu.edu", "tangsh@mymail.sxu.edu", "bader@mymail.sxu.edu", "gastown@mymail.sxu.edu", "ribet@mymail.sxu.edu", "jmcnamara@mymail.sxu.edu", "boftx@mymail.sxu.edu", "wiseb@mymail.sxu.edu", "crobles@mymail.sxu.edu", "payned@mymail.sxu.edu", "conteb@mymail.sxu.edu", "timtroyr@mymail.sxu.edu", "doormat@mymail.sxu.edu", "thrymm@mymail.sxu.edu", "bebing@mymail.sxu.edu", "lukka@mymail.sxu.edu", "ducasse@mymail.sxu.edu", "mkearl@mymail.sxu.edu", "marcs@mymail.sxu.edu", "yumpy@mymail.sxu.edu", "lpalmer@mymail.sxu.edu", "jespley@mymail.sxu.edu", "noneme@mymail.sxu.edu", "jgmyers@mymail.sxu.edu"]
Contact_Information
Online_Space = ["Zoom ", "MS Teams", "Big Blue Button " "Discord", "MS Teams", "MS Teams", "Zoom ", "MS Teams ", "Discord", "Big Blue Button", "Zoom ", "Zoom ", "Zoom ", "Big Blue Button", "Zoom", "Discord", "Zoom ", "Zoom ", "Big Blue Button ", "Big Blue Button", "MS Teams", "Big Blue Button", "Discord", "Zoom ", "Big Blue Button", "MS Teams", "Discord", "Big Blue Button", "Big Blue Button", "Zoom ", "Zoom ", "Zoom ", "Big Blue Button", "Zoom", "Zoom", "Zoom", "Zoom", "Big Blue Button", "Big Blue Button", "Big Blue Button", "Discord"]
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "b1", "b2", "b3", "b4", "b5"]
ser = pd.Series(data=Tutor_Name , index=labels)
ser
ser1 = pd.Series(data=Course_Name, index=labels)
ser1
ser2 = pd.Series(data=In_Person_Meeting_Times , index=labels)
ser2
ser3 = pd.Series(data=Online_Meeting_Times , index=labels)
ser3
ser4 = pd.Series(data=Contact_Information, index=labels)
ser4
ser5 = pd.Series(data=Online_Space, index=labels)
ser5
df = pd.DataFrame()
df['Tutor Names']= ser
df['Course Name']= ser1
df['In Person Meeting Time']= ser2
df['Online Meeting Time']= ser3
df['Contact Information']= ser4
df['Online Space']= ser5
#Test the Data Frame
df
#Exports the DataFrame to a .csv file
df.to_csv('Tutors_DB.csv', index=False)

