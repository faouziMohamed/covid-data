from PyQt5.QtSql import QSqlQuery, QSqlDatabase
import pandas as pd
from pandas import DataFrame as DtFrame
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtCore import QObject


def create_connection(df: pd.DataFrame, db_name: str):
    db = QSqlDatabase.addDatabase("QSLITE")
    db.setDatabaseName(db_name)

    tr = QObject.tr
    message = "Unable to establish a database connection.\n" \
              "This example needs SQLite support. Please read " \
              "the Qt SQL driver documentation for information how " \
              "to build it.\n\n Click Cancel to exit."
    if not db.open():
        QMessageBox.critical(QWidget(), tr("Cannot open database"), tr(message),
                             QMessageBox.cancel)


def create_table_for(col_name: str, df: pd.DataFrame) -> pd.DataFrame:
    data = df[col_name].unique()
    table = pd.DataFrame(data)
    table.rename(columns={0: col_name}, inplace=True)
    table.sort_values(col_name, inplace=True)
    table['id'] = sorted(table[col_name].argsort())
    table = table[['id', col_name]]
    return table


def create_continent_table(df: pd.DataFrame) -> pd.DataFrame:
    continent = create_table_for('continent', df)
    return continent


# DtFrame is pd.DataFrame

def create_country_table(df: pd.DataFrame, continent: pd.DataFrame) -> DtFrame:
    columns = ['idl', 'location', 'continent']
    countries = df[columns[1:]]
    countries.set_index(columns[1:], inplace=True)
    unique_rows = list(countries.index.unique())
    countries = pd.DataFrame(unique_rows, columns=columns[1:])
    countries['idl'] = sorted(countries.location.argsort())
    countries = countries[columns]
    countries.rename(columns={'continent': 'idc'}, inplace=True)
    countries.replace(list(continent.continent), continent.id, inplace=True)
    return countries


def create_cases_table(df: pd.DataFrame, countries: pd.DataFrame) -> DtFrame:
    cases = df[['location', 'date', 'new_tests', 'new_cases', 'total_deaths']]
    cases = cases.replace(list(countries.location), countries.idc)
    cases.rename(columns={'location': 'idl'}, inplace=True)
    cases.sort_values('date', ascending=False, inplace=True)
    return cases
