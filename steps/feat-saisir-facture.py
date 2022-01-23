from behave import *

use_step_matcher("re")


@given("un contributeur ayant payé une épicerie")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given un contributeur ayant payé une épicerie')


@step("il revient à la maison avec sa facture")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And il revient à la maison avec sa facture')


@step("il la donne au consignateur pour qu'il saisisse")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And il la donne au consignateur pour qu\'il saisisse')


@when("le consignateur saisie (?P<information>.+) et la (?P<valeur>.+)")
def step_impl(context, information, valeur):
    """
    :type context: behave.runner.Context
    :type information: str
    :type valeur: str
    """
    raise NotImplementedError(u'STEP: When le consignateur saisie <information> et la <valeur>')


@then("le total de contribution pour cette personne est mis à jour")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then le total de contribution pour cette personne est mis à jour')


@when("il confirme la saisie de tous les détails")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When il confirme la saisie de tous les détails')


@then("le (?P<montant>.+) est ajouté au (?P<solde>.+) courant")
def step_impl(context, montant, solde):
    """
    :type context: behave.runner.Context
    :type montant: str
    :type solde: str
    """
    raise NotImplementedError(u'STEP: Then le <montant> est ajouté au <solde> courant')


@step("le (?P<total>.+) de contribution a été ajouté du montant")
def step_impl(context, total):
    """
    :type context: behave.runner.Context
    :type total: str
    """
    raise NotImplementedError(u'STEP: And le <total> de contribution a été ajouté du montant')