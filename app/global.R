library(tidyverse)
library(shiny)
library(stringi)
library(odbc)
library(DBI)
library(pool)

con = dbPool(
  odbc(),
  Driver = "PostgreSQL ANSI", 
  Database = Sys.getenv("SF_DB"), 
  Port = "5432", 
  Server = Sys.getenv("SF_SERVER"), 
  UID = Sys.getenv("SF_UN"), 
  PWD = Sys.getenv("SF_PW"), 
  sslmode = "require"
)

data = con %>% 
  tbl("") %>%
  collect()


