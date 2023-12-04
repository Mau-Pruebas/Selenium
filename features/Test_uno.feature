Feature: Nuestro primer Demo

  Background:
     Given Abriendo navegador

  Scenario Outline: Corriendo nuestro primer Test

    When Introducimos el valor "<user>" en los campos
    Then Enter the message and click Show Message
    Then Enter A "<n1>" value
    Then Enter B "<n2>" value
    Then Click Get Total button

    Examples:
    | user | n1 | n2 |
    | Mau  | 50 | 50 |
    | Tiny  | 20 | 30 |