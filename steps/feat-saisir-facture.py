from behave import *

use_step_matcher("re")


@given("un contributeur ayant payé une épicerie")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Given un contributeur ayant payé une épicerie')


@step("il revient à la maison avec sa facture")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And il revient à la maison avec sa facture')


@step("il la donne au consignateur pour qu'il saisisse")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And il la donne au consignateur pour qu\'il saisisse')


@when("le consignateur saisie (?P<information>.+) et la (?P<valeur>.+)")
def step_impl(context, information, valeur):
    """
    :type context: behave.runner.Context
    :type information: str
    :type valeur: str
    """
    print(f"STEP: When le consignateur saisie l'information de :  {information} qui est :  {valeur}")


@then("le total de contribution pour cette personne est mis à jour")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then le total de contribution pour cette personne est mis à jour')

@given("une contribution saisie par le consignateur")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Given une contribution saisie par le consignateur')

@when("il confirme la saisie de tous les détails")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When il confirme la saisie de tous les détails')


@then("le (?P<montant>.+) est ajouté au (?P<solde>.+) courant")
def step_impl(context, montant, solde):
    """
    :type context: behave.runner.Context
    :type montant: str
    :type solde: str
    """
    print(f"STEP: Then le montant : {montant} est ajouté au solde : {solde} courant")


@step("le (?P<total>.+) de contribution a été ajouté du montant")
def step_impl(context, total):
    """
    :type context: behave.runner.Context
    :type total: str
    """
    print(f"STEP: And le total : {total} de contribution a été ajouté du montant")


