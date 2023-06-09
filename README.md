# punto_de_venta_mtg
Punto de venta en línea para cartas de mtg

# RESTful Structure


||__GET__|__POST__|__PUT__|__DELETE__|
|---|----|----|----|----|
|/cards/|Show all cards|Add Card|Update all cards| N/A|
|/cards/\<pk\>|N/A|N/A|Update card|Delete Card|
|/cart/|Show cards in cart|Add card to cart|Update cards in cart|Empty Cart|
|/cart/\<pk\>|Show cards|N/A|Update card \<pk\> in cart|Remove \<pk\> from cart|


