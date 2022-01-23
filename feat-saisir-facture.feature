Feature: FEAT : Saisir facture

  In Order to compiler le montant des factures qui entrent
  As a consigneure
  I want to entrer les montants, leur date, leur origine et qui a payé

  Scenario: saisir le montant d'une facture
    Given un contributeur ayant payé une épicerie
    And il revient à la maison avec sa facture
    When il la donne au consignateur pour qu'il la saisisse
    Then la date est enregistrée
    And l'établissement de l'achat
    And le montant en dollars
    And le nom de la personne qui a payé l'achat

  @ORPHAN
  Scenario: Saisir le nom de facture
    Given un contributeur ayant payé une épicerie
    And il revient à la maison avec sa facture
    When il la donne au consignateur pour qu'il la saisisse
    Then le consignateur saisie le nom de l'établissement de la facture
