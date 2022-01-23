Feature: FEAT : Saisir facture

  In Order to compiler le montant des factures qui entrent
  As a consigneure
  I want to entrer les montants, leur date, leur origine et qui a payé

  Scenario Outline: Saisir la facture
    Given un contributeur ayant payé une épicerie
    And il revient à la maison avec sa facture
    And il la donne au consignateur pour qu'il saisisse
    When le consignateur saisie <information> et la <valeur>
    Then le total de contribution pour cette personne est mis à jour
    
    Examples:
      | information   | valeur          |
      | établissement | IGA             |
      | personne      | Éric            |
      | date          | 12 janvier 2022 |
      | montant       | 233             |

  Scenario Outline: La contribution d'une personne est mise à jour
    Given une contribution saisie par le consignateur
    When il confirme la saisie de tous les détails
    Then le <montant> est ajouté au <solde> courant
    And le <total> de contribution a été ajouté du montant
    Examples:
      |montant|solde| total|
      | 345   |55   | 400  |
