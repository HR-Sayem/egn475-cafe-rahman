# User stories

1. **[MUST]** As a Cafe customer, I want to view the available food and drink menu, so that I can decide what to order before visiting the cafe.
  - Given I am a customer visiting the cafe website, when I open the menu page, then I can see the available food and drink items with their names and prices.
  - Given No food or drink items are currently available, when I open the menu page, then I see a message saying no items are currently available.

2. **[MUST]** As a Cafe customer, I want to view the details and price of a food item, so that I can compare the food description and price before choosing what to order.
  - Given I am viewing the cafe menu, when I select an available food item, then I can see its name, description, and price.
  - Given A food item is no longer available, when I open its details, then I see a message saying the food item is currently unavailable

3. **[MUST]** As a cafe customer, I want to select the quantity of each food item, so that I can order the exact amount of food I need.
  - Given I am viewing an available food item, when I select a quantity of 2, then The order shows 2 units of that food item.
  - Given I am selecting the quantity of a food item, when I enter a quantity of 0, a negative number, or more than 10, then the website rejects the quantity and shows an error message.
4. **[MUST]** As a cafe customer, I want to review my order and see the total price, so that I can know how much I need to pay before placing my order.
  - Given I have added food items to my order, when I open my order summary, then I can see each item's price, quantity, and the total price.
  - Given My order contains no food items, when I open my order summary, then The total price shows zero and I see a message asking me to add items.

5. **[MUST]** As a cafe customer, I want to enter my name and phone number for pickup, so that the cafe staff can identify my order when I arrive.
  - Given I have added food items to my order, when I enter my name and a valid 10-digit US phone number, then my pickup information is saved with my order.
  - Given I am entering my pickup information, when I leave the name or phone number empty, then The website shows an error message and does not accept the information.

6. **[MUST]** As a kitchen staff member, I want to view all incoming customer orders, so that I can prepare customer orders in the order they were received.
  - Given A customer has placed an order, when I open the kitchen order board, then I can see incoming orders with their items, quantities, and pickup names, listed from oldest to newest.
  - Given No customer orders have been placed, when I open the kitchen order board, then I see a message saying there are no incoming orders.

7. **[MUST]** As a kitchen staff member, I want to update an order's preparation status, so that customers can know when their food is being prepared or ready for pickup.
  - Given A customer order has been received, when I mark the order as preparing or ready for pickup, then the updated status appears on both the kitchen board and the customer's order status page.
  - Given I am not logged in as a kitchen staff member, when I try to update an order status, then The website denies access and shows an error message.

8. **[SHOULD]** As a cafe customer, I want to receive a confirmation after placing my order, so that I know my order was successfully submitted.
  - Given I have entered valid pickup information and selected food items, when I successfully place my order, then I see an order confirmation with my order number and pickup details.
  - Given I have entered valid pickup information but the order submission fails because of a server error, when I try to place my order, then I see a message saying "Unable to place your order. Please try again." and my order is not shown as confirmed.
 # AI Review Log

## Copilot Review Prompt

Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.

## Copilot Feedback and Decisions

| Story | Copilot Feedback | Decision | Reason |
|---|---|---|---|
| 1 | No clear size or testability problem. | Accepted | No changes were necessary. |
| 2 | The goal was subjective and unavailable-item behavior went beyond the story. | Accepted | I clarified the goal and separated viewing details from ordering behavior. |
| 3 | Maximum quantity was not specified. | Accepted | I specified a maximum quantity of 10. |
| 4 | Currency rounding, taxes, and fees were unspecified. | Rejected | The prototype focuses on item prices and total price without taxes or additional fees. |
| 5 | Valid phone number was undefined. | Accepted | I specified a valid 10-digit US phone number. |
| 6 | Incoming orders and correct order were ambiguous. | Accepted | I specified that orders appear from oldest to newest with items, quantities, and pickup names. |
| 7 | Customer status visibility and order status lifecycle were unclear. | Accepted | I added customer status visibility and the Ready for Pickup status. |
| 8 | Order submission failure and error messages were not specific. | Accepted | I specified a server error and an example error message. |
# Assignment Questions

## 1. Which story did you split into smaller stories, and why?

I separated the food item details and ordering behavior in Story 2. I kept the story focused on viewing food item information, such as the name, description, and price. This made the story smaller, clearer, and easier to test.

## 2. Which story was hardest to write acceptance criteria for? What made it hard?

Story 7 was the hardest to write acceptance criteria for because it involved two different users: kitchen staff and customers. Kitchen staff need to update the order status, while customers need to see the updated status. I also needed to consider unauthorized users who should not be allowed to change order statuses.