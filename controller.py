# IMPORTING LIBRARIES

import jwt
import pytz
import datetime
import mysql.connector


# IMPORTING MYSQL MECHANISM

from sql import *


# IMPORTING MICROSERVICES

import person_service as pserv
import education_service as eduserv
import address_service as adserv
import professional_service as profserv
import auth_service as autserv


# CONNECTING APPLICATION SERVICES
    
    ## PERSON:
    
def Save_Sql_person(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class):
    
    pserv.Save_Sql(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class)

    
    ## EDUCATION:

def Save_Sql_education(Identity, Educational_level, Course, Institution, Year_of_course_completion, English_language):

    eduserv.Save_Sql(Identity, Educational_level, Course, Institution, Year_of_course_completion, English_language)
    
    
    ## ADDRESS:

def Save_Sql_address(Identity, Street, City, State, Postal_code, Country, Avaliable_for_change):
    
    adserv.Save_Sql(Identity, Street, City, State, Postal_code, Country, Avaliable_for_change)
    
    
    ## PROFESSIONAL:     

def Save_Sql_professional(Identity, Chemical_industry_years, Last_position, Performed_activities):

    profserv.Save_Sql(Identity, Chemical_industry_years, Last_position, Performed_activities)


    ## AUTH:

def login_inf(email, password):
    
    autserv.login_informations (email, password)


def register_new_user(name, email, password):
    
    autserv.register_users(name, email, password)
