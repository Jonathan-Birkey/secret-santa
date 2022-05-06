#!/usr/bin/env python3
__author__ = 'Jonathan Birkey'
__email__ = 'jonathan.birkey@gmail.com'
__date__ = '05May2022'

import click
import csv
import mysql.connector


def send_email():
    pass


def create_list():
    pass


def add_list_to_db():
    pass


def get_list_from_db():
    pass


def init_santas():
    # take in csv
    # skip header
    # create random list
    # save to db
    # send initial email
    pass


def send_reminder():
    # get current year
    # get all emails and secret santas
    # send reminder email
    pass


@click.command()
def main() -> None:
    click.echo('hello world')


if __name__ == '__main__':
    main()
