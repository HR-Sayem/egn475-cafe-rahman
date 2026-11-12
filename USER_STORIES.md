# User stories

1. **[MUST]** As a Cafe customer, I want to view the available food and drink menu, so that I can decide what to order before visiting the cafe.
  - Given I am a customer visiting the cafe website, when I open the menu page, then I can see the available food and drink items with their names and prices.
  - Given No food or drink items are currently available, when I open the menu page, then I see a message saying no items are currently available.

2. **[MUST]** As a Cafe customer, I want to view the details and price of a food item, so that I can choose the food that best matches my preferences and budget.
  - Given I am viewing the cafe menu, when I select an available food item, then I can see its name, description, and price.
  - Given A food item is no longer available, when I open its details, then I see an unavailable message and cannot add it to my order.

3. **[MUST]** As a cafe customer, I want to select the quantity of each food item, so that I can order the exact amount of food I need.
  - Given I am viewing an available food item, when I select a quantity of 2, then The order shows 2 units of that food item.
  - Given I am selecting the quantity of a food item, when I enter a quantity of 0 or a negative number, then The website does not accept the quantity and shows an error message.

4. **[MUST]** As a cafe customer, I want to review my order and see the total price, so that I can know how much I need to pay before placing my order.
  - Given I have added food items to my order, when I open my order summary, then I can see each item's price, quantity, and the total price.
  - Given My order contains no food items, when I open my order summary, then The total price shows zero and I see a message asking me to add items.

5. **[MUST]** As a cafe customer, I want to enter my name and phone number for pickup, so that the cafe staff can identify my order when I arrive.
  - Given I have added food items to my order, when I enter my name and a valid phone number, then My pickup information is saved with my order.
  - Given I am entering my pickup information, when I leave the name or phone number empty, then The website shows an error message and does not accept the information.

6. **[MUST]** As a kitchen staff member, I want to view all incoming customer orders, so that I can prepare customer orders in the correct order.
  - Given A customer has placed an order, when I open the kitchen order board, then I can see the new order with its items and order details.
  - Given No customer orders have been placed, when I open the kitchen order board, then I see a message saying there are no incoming orders.

7. **[MUST]** As a kitchen staff member, I want to update an order's preparation status, so that customers can know when their food is being prepared or ready for pickup.
  - Given A customer order has been received, when I mark the order as preparing, then The order status changes to preparing on the kitchen board.
  - Given I am not logged in as a kitchen staff member, when I try to update an order status, then The website denies access and shows an error message.

8. **[SHOULD]** As a cafe customer, I want to receive a confirmation after placing my order, so that I know my order was successfully submitted.
  - Given I have entered valid pickup information and selected food items, when I successfully place my order, then I see an order confirmation with my order number and pickup details.
  - Given My order submission fails, when I try to place my order, then I see an error message and my order is not shown as confirmed.
