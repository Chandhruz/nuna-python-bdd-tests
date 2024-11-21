Feature: Payment Journey for tavopets product

  @kevin
  Scenario: Buy a product on tavopets 
    Given I am on the tavopets ecommerce portal
    Then I click on the ACCEPT-COOKIES button
    Then I click on the SHOP-NOW button
    Then I click on DUPREE product
    Then I add DUPREE product to basket
    Then I click on BASKET
    Then I click PROCEED-TO-CHECKOUT button
    Then I enter email